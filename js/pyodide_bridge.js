/**
 * Ponte entre JavaScript e o domínio Python executado pelo Pyodide.
 * Os módulos do domínio são carregados individualmente no virtual filesystem.
 */

export const PYODIDE_VERSION = "314.0.7";
const PYODIDE_INDEX_URL = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;
const PYTHON_MODULES = [
  "__init__.py",
  "models.py",
  "services.py",
  "metrics.py",
  "schema.py",
];

let runtimePromise;

function carregarScriptPyodide() {
  if (typeof globalThis.loadPyodide === "function") return Promise.resolve();

  return new Promise((resolve, reject) => {
    const existente = document.querySelector('script[data-pyodide-runtime="true"]');
    const script = existente || document.createElement("script");

    script.addEventListener("load", () => {
      if (typeof globalThis.loadPyodide === "function") resolve();
      else reject(new Error("O CDN foi carregado, mas loadPyodide não está disponível."));
    }, { once: true });

    script.addEventListener("error", () => {
      script.remove();
      reject(new Error("Não foi possível carregar o runtime Pyodide pelo CDN."));
    }, { once: true });

    if (!existente) {
      script.src = `${PYODIDE_INDEX_URL}pyodide.js`;
      script.async = true;
      script.dataset.pyodideRuntime = "true";
      document.head.append(script);
    }
  });
}

async function carregarModulosPython(pyodide) {
  const diretorioVirtual = "/home/pyodide/todolist";
  pyodide.FS.mkdirTree(diretorioVirtual);

  for (const nomeArquivo of PYTHON_MODULES) {
    const url = new URL(`../src/todolist/${nomeArquivo}`, import.meta.url);
    const resposta = await fetch(url);

    if (!resposta.ok) {
      throw new Error(`Falha ao carregar ${nomeArquivo}: HTTP ${resposta.status}.`);
    }

    const codigo = await resposta.text();
    pyodide.FS.writeFile(`${diretorioVirtual}/${nomeArquivo}`, codigo);
  }

  pyodide.runPython(`
import sys
if "/home/pyodide" not in sys.path:
    sys.path.insert(0, "/home/pyodide")
import todolist
`);

  const apiDisponivel = pyodide.runPython(`
import todolist
_funcoes_kanban = (
    "criar_tarefa",
    "editar_tarefa",
    "mover_tarefa",
    "excluir_tarefa",
    "validar_envelope_backup",
    "gerar_envelope_backup",
    "calcular_relatorio_completo",
    "obter_timestamp_utc_atual",
    "preparar_importacao_backup",
    "preparar_estado_importado",
)
all(callable(getattr(todolist, nome, None)) for nome in _funcoes_kanban)
`);

  if (!apiDisponivel) {
    throw new Error("O pacote todolist foi importado, mas sua API pública está incompleta.");
  }
}

const PYTHON_DISPATCHER = `
import json
import todolist

def _kanban_dispatch(payload_json):
    payload = json.loads(payload_json)
    operacao = payload["operacao"]
    dados = payload.get("dados", {})
    tarefas = dados.get("tarefas", [])
    timestamp_atual = dados.get("timestamp_ultima_alteracao")

    if operacao == "metricas":
        data_local = dados["data_local_referencia"]
        return json.dumps({
            "resumo": todolist.calcular_resumo_projeto(tarefas),
            "foco_hoje": todolist.calcular_foco_hoje(tarefas, data_local),
        }, ensure_ascii=False)

    if operacao == "relatorio":
        return json.dumps(
            todolist.calcular_relatorio_completo(
                tarefas,
                dados["data_local_referencia"],
                dados.get("periodo_conclusao_inicio"),
                dados.get("periodo_conclusao_fim"),
            ),
            ensure_ascii=False,
        )

    if operacao == "exportar_backup":
        timestamp_exportacao = todolist.obter_timestamp_utc_atual()
        envelope = todolist.gerar_envelope_backup(tarefas, timestamp_exportacao)
        valido, mensagem = todolist.validar_envelope_backup(envelope)
        if not valido:
            raise ValueError(mensagem)
        return json.dumps(envelope, ensure_ascii=False)

    if operacao == "validar_backup":
        estado_candidato = todolist.preparar_importacao_backup(dados["conteudo"])
        return json.dumps(estado_candidato, ensure_ascii=False)

    if operacao == "confirmar_importacao":
        timestamp_importacao = todolist.obter_timestamp_utc_atual()
        estado_candidato = todolist.preparar_estado_importado(
            dados["tarefas"], timestamp_importacao
        )
        return json.dumps(estado_candidato, ensure_ascii=False)

    if operacao == "validar_estado":
        estado = dados.get("estado", {})
        if not isinstance(estado, dict) or set(estado) != {"tarefas", "timestamp_ultima_alteracao"}:
            raise ValueError("Estrutura do estado persistido inválida.")
        lista = estado["tarefas"]
        timestamp = estado["timestamp_ultima_alteracao"]
        if not isinstance(lista, list):
            raise ValueError("O campo tarefas deve ser uma lista.")
        if timestamp is None:
            if lista:
                raise ValueError("Estado com tarefas exige timestamp global.")
            return json.dumps({"valido": True})
        todolist.validar_iso_utc_ms(timestamp, "timestamp_ultima_alteracao")
        envelope = todolist.gerar_envelope_backup(lista, timestamp)
        valido, mensagem = todolist.validar_envelope_backup(envelope)
        if not valido:
            raise ValueError(mensagem)
        return json.dumps({"valido": True})

    if operacao == "criar":
        novas, timestamp, tarefa = todolist.criar_tarefa(
            tarefas,
            dados["titulo"],
            dados.get("descricao", ""),
            dados.get("prioridade", "media"),
            dados.get("data_limite"),
            timestamp_injetado=dados.get("timestamp_injetado"),
        )
    elif operacao == "editar":
        novas, timestamp, tarefa = todolist.editar_tarefa(
            tarefas,
            dados["tarefa_id"],
            dados["titulo"],
            dados.get("descricao", ""),
            dados["prioridade"],
            dados.get("data_limite"),
            timestamp_injetado=dados.get("timestamp_injetado"),
            timestamp_global_atual=timestamp_atual,
        )
    elif operacao == "mover":
        novas, timestamp, tarefa = todolist.mover_tarefa(
            tarefas,
            dados["tarefa_id"],
            dados["novo_estado"],
            nova_ordem=dados.get("nova_ordem"),
            timestamp_injetado=dados.get("timestamp_injetado"),
            timestamp_global_atual=timestamp_atual,
        )
    elif operacao == "excluir":
        novas, timestamp, tarefa = todolist.excluir_tarefa(
            tarefas,
            dados["tarefa_id"],
            timestamp_injetado=dados.get("timestamp_injetado"),
        )
    else:
        raise ValueError("Operação de domínio desconhecida: " + str(operacao))

    return json.dumps({
        "tarefas": novas,
        "timestamp_ultima_alteracao": timestamp,
        "tarefa": tarefa,
    }, ensure_ascii=False)
`;

export async function initializePythonRuntime() {
  if (!runtimePromise) {
    runtimePromise = (async () => {
      await carregarScriptPyodide();
      const pyodide = await globalThis.loadPyodide({ indexURL: PYODIDE_INDEX_URL });
      await carregarModulosPython(pyodide);
      pyodide.runPython(PYTHON_DISPATCHER);
      console.info(`Pyodide ${PYODIDE_VERSION}: pacote todolist carregado.`);
      return pyodide;
    })().catch((erro) => {
      runtimePromise = undefined;
      throw erro;
    });
  }

  return runtimePromise;
}

async function executarPython(operacao, dados) {
  const pyodide = await initializePythonRuntime();
  pyodide.globals.set("_kanban_payload_json", JSON.stringify({ operacao, dados }));

  try {
    return JSON.parse(pyodide.runPython("_kanban_dispatch(_kanban_payload_json)"));
  } finally {
    pyodide.globals.delete("_kanban_payload_json");
  }
}

export async function validateState(estado) {
  await executarPython("validar_estado", { estado });
  return true;
}

export async function calculateReport(estado, dataLocalReferencia, periodoInicio = null, periodoFim = null) {
  return executarPython("relatorio", {
    tarefas: estado.tarefas,
    data_local_referencia: dataLocalReferencia,
    periodo_conclusao_inicio: periodoInicio,
    periodo_conclusao_fim: periodoFim,
  });
}

export async function createBackup(estado) {
  return executarPython("exportar_backup", { tarefas: estado.tarefas });
}

export async function prepareImportedState(tarefas) {
  return executarPython("confirmar_importacao", { tarefas });
}

export async function validateBackup(conteudo) {
  if (typeof conteudo !== "string") {
    throw new TypeError("O conteúdo do arquivo deve ser texto.");
  }
  return executarPython("validar_backup", { conteudo });
}

export async function calculateMetrics(estado, dataLocalReferencia) {
  return executarPython("metricas", {
    tarefas: estado.tarefas,
    timestamp_ultima_alteracao: estado.timestamp_ultima_alteracao,
    data_local_referencia: dataLocalReferencia,
  });
}

export async function executeDomainOperation(operacao, estado, dados) {
  const resultado = await executarPython(operacao, {
    tarefas: estado.tarefas,
    timestamp_ultima_alteracao: estado.timestamp_ultima_alteracao,
    ...dados,
  });

  return {
    tarefas: resultado.tarefas,
    timestamp_ultima_alteracao: resultado.timestamp_ultima_alteracao,
    tarefa: resultado.tarefa,
  };
}
