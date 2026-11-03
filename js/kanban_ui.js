const ESTADOS = [
  ["a_fazer", "lista-a-fazer", "contador-a-fazer", "vazio-a-fazer", "A Fazer"],
  ["em_andamento", "lista-em-andamento", "contador-em-andamento", "vazio-em-andamento", "Em Andamento"],
  ["concluida", "lista-concluidas", "contador-concluidas", "vazio-concluidas", "Concluídas"],
];
const rotuloPrioridade = { alta: "Alta", media: "Média", baixa: "Baixa" };
const normalizar = (valor) => String(valor ?? "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("pt-BR");
const el = (tag, classe, texto) => { const node = document.createElement(tag); if (classe) node.className = classe; if (texto !== undefined) node.textContent = texto; return node; };
const dataHoje = () => { const d = new Date(); return [d.getFullYear(), String(d.getMonth()+1).padStart(2,"0"), String(d.getDate()).padStart(2,"0")].join("-"); };

export function createKanbanUI({ getState, actions, notify, onStateRendered = () => {} }) {
  let termo = "";
  let selecionada = null;
  const busca = document.getElementById("busca-tarefas");
  const nova = document.getElementById("dialog-nova-tarefa");
  const editar = document.getElementById("dialog-editar-tarefa");
  const excluir = document.getElementById("dialog-excluir-tarefa");
  const abrir = (dialog) => { if (dialog && !dialog.open) dialog.showModal(); };
  const fechar = (dialog) => { if (dialog?.open) dialog.close(); };

  function criarCartao(tarefa) {
    const item = el("li");
    const card = el("article", "task-card" + (tarefa.estado === "concluida" ? " is-completed" : ""));
    card.dataset.taskId = tarefa.id;
    card.tabIndex = -1;
    const checkbox = el("input", "task-check");
    checkbox.type = "checkbox"; checkbox.checked = tarefa.estado === "concluida"; checkbox.disabled = true;
    checkbox.setAttribute("aria-label", checkbox.checked ? "Tarefa concluída" : "Tarefa não concluída");
    const conteudo = el("div", "task-content");
    conteudo.append(el("h3", "", tarefa.titulo));
    if (tarefa.descricao) conteudo.append(el("p", "", tarefa.descricao));
    const meta = el("div", "task-meta" + (checkbox.checked ? " completed-meta" : ""));
    if (checkbox.checked) {
      meta.append(el("span", "completed-check", "✓"));
      const data = tarefa.data_conclusao ? new Date(tarefa.data_conclusao) : null;
      meta.append(document.createTextNode(data && !Number.isNaN(data.getTime()) ? "Concluída em " + new Intl.DateTimeFormat("pt-BR").format(data) : "Concluída"));
    } else {
      meta.append(el("span", "badge-prioridade priority-" + tarefa.prioridade, rotuloPrioridade[tarefa.prioridade] || tarefa.prioridade));
      if (tarefa.data_limite) {
        const prazo = el("span", "task-due");
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("class", "ui-icon"); svg.setAttribute("aria-hidden", "true");
        const use = document.createElementNS("http://www.w3.org/2000/svg", "use"); use.setAttribute("href", "#icon-calendar"); svg.append(use);
        const time = el("time", "", new Intl.DateTimeFormat("pt-BR").format(new Date(tarefa.data_limite + "T12:00:00")));
        time.dateTime = tarefa.data_limite; prazo.append(svg, document.createTextNode(" "), time); meta.append(prazo);
      }
    }
    conteudo.append(meta); card.append(checkbox, conteudo);
    {
      const menu = el("details", "task-menu");
      const summary = el("summary", "task-more", "Opções da tarefa");
      summary.setAttribute("aria-label", "Opções de " + tarefa.titulo); menu.append(summary);
      const lista = el("ul");
      const linhaEditar = el("li"); const botaoEditar = el("button", "", "Editar tarefa");
      botaoEditar.type = "button"; botaoEditar.dataset.taskAction = "edit"; linhaEditar.append(botaoEditar); lista.append(linhaEditar);
      const linhaMover = el("li"); const submenu = el("details", "task-move-menu"); submenu.append(el("summary", "", "Mover para..."));
      const destinos = el("ul");
      for (const [estado, , , , rotulo] of ESTADOS) {
        const li = el("li"); const botao = el("button", "", rotulo);
        botao.type = "button"; botao.dataset.taskAction = "move"; botao.dataset.moveTo = estado; li.append(botao); destinos.append(li);
      }
      submenu.append(destinos); linhaMover.append(submenu); lista.append(linhaMover);
      const linhaExcluir = el("li"); const botaoExcluir = el("button", "danger-action", "Excluir tarefa");
      botaoExcluir.type = "button"; botaoExcluir.dataset.taskAction = "delete"; linhaExcluir.append(botaoExcluir); lista.append(linhaExcluir);
      menu.append(lista); card.append(menu);
    }
    item.append(card); return item;
  }

  function aplicarBusca() {
    const termoNormalizado = normalizar(termo.trim());
    document.querySelectorAll(".task-card[data-task-id]").forEach((card) => {
      const texto = normalizar((card.querySelector("h3")?.textContent || "") + " " + (card.querySelector(".task-content p")?.textContent || ""));
      card.closest("li").hidden = Boolean(termoNormalizado) && !texto.includes(termoNormalizado);
    });
  }

  async function atualizarIndicadores() {
    const state = getState();
    const hoje = dataHoje();
    try {
      const metricas = await actions.getMetrics(hoje);
      const resumo = metricas.resumo;
      const set = (id, valor) => { const node = document.getElementById(id); if (node) node.textContent = String(valor); };
      set("total-tarefas", resumo.total);
      set("resumo-concluidas", resumo.concluidas);
      set("resumo-pendentes", resumo.pendentes);
      set("percentual-concluidas", resumo.perc_concluidas.toLocaleString("pt-BR") + "%");
      set("percentual-pendentes", resumo.perc_pendentes.toLocaleString("pt-BR") + "%");
      set("foco-hoje", metricas.foco_hoje);
      const bc = document.getElementById("barra-concluidas"), bp = document.getElementById("barra-pendentes");
      if (bc) { bc.value = resumo.perc_concluidas; bc.setAttribute("aria-label", resumo.perc_concluidas + "% concluídas"); }
      if (bp) { bp.value = resumo.perc_pendentes; bp.setAttribute("aria-label", resumo.perc_pendentes + "% pendentes"); }
    } catch (erro) { notify("Não foi possível atualizar os indicadores: " + erro.message); }

  }

  function render(state = getState()) {
    for (const [estado, listaId, contadorId, vazioId] of ESTADOS) {
      const lista = document.getElementById(listaId); if (!lista) continue;
      const tarefas = state.tarefas.filter(t => t.estado === estado).sort((a,b) => a.ordem-b.ordem);
      lista.replaceChildren(...tarefas.map(criarCartao));
      const contador = document.getElementById(contadorId); if (contador) contador.textContent = String(tarefas.length);
      const vazio = document.getElementById(vazioId); if (vazio) vazio.hidden = tarefas.length > 0;
    }
    void atualizarIndicadores(); aplicarBusca(); onStateRendered(state);
  }

  async function executar(operacao) {
    try {
      const resultado = await operacao();
      if (!resultado?.success) { notify(resultado?.error?.message || "A operação falhou. O estado anterior foi preservado."); return false; }
      if (resultado.changed) render();
      return true;
    } catch (erro) { notify(erro.message || "Não foi possível concluir a operação."); return false; }
  }
  function dadosForm(form) {
    const dados = new FormData(form);
    return { titulo: String(dados.get("titulo") || "").trim(), descricao: String(dados.get("descricao") || "").trim(), prioridade: String(dados.get("prioridade") || "media"), data_limite: String(dados.get("data_limite") || "") || null };
  }
  function abrirEdicao(id) {
    const tarefa = getState().tarefas.find(t => t.id === id); if (!tarefa) return;
    selecionada = id; const form = editar.querySelector("form");
    form.elements.titulo.value = tarefa.titulo; form.elements.descricao.value = tarefa.descricao;
    form.elements.prioridade.value = tarefa.prioridade; form.elements.data_limite.value = tarefa.data_limite || "";
    abrir(editar); form.elements.titulo.focus();
  }
  function abrirExclusao(id) {
    const tarefa = getState().tarefas.find(t => t.id === id); if (!tarefa) return;
    selecionada = id; document.getElementById("titulo-tarefa-exclusao").textContent = tarefa.titulo; abrir(excluir);
  }

  nova.querySelector("form").addEventListener("submit", async event => {
    event.preventDefault(); const form = event.currentTarget; if (!form.reportValidity()) return;
    if (await executar(() => actions.createTask(dadosForm(form)))) { form.reset(); fechar(nova); }
  });
  editar.querySelector("form").addEventListener("submit", async event => {
    event.preventDefault(); const form = event.currentTarget; if (!form.reportValidity() || !selecionada) return;
    if (await executar(() => actions.editTask({ tarefa_id: selecionada, ...dadosForm(form) }))) { fechar(editar); selecionada = null; }
  });
  excluir.querySelector("[data-confirm-delete]").addEventListener("click", async () => {
    if (!selecionada) return;
    if (await executar(() => actions.deleteTask({ tarefa_id: selecionada }))) { fechar(excluir); selecionada = null; }
  });

  document.addEventListener("click", async event => {
    const abrirBotao = event.target.closest("[data-dialog-open='dialog-nova-tarefa']");
    if (abrirBotao) { const form = nova.querySelector("form"); form.reset(); abrir(nova); nova.querySelector("#nova-tarefa-titulo").focus(); return; }
    const card = event.target.closest(".task-card[data-task-id]");
    const acao = event.target.closest("[data-task-action]");
    if (!card || !acao) return;
    if (acao.dataset.taskAction === "edit") abrirEdicao(card.dataset.taskId);
    if (acao.dataset.taskAction === "delete") abrirExclusao(card.dataset.taskId);
    if (acao.dataset.taskAction === "move") {
      const destino = ESTADOS.find(item => item[0] === acao.dataset.moveTo);
      const tarefaAtual = getState().tarefas.find(t => t.id === card.dataset.taskId);
      if (!destino || tarefaAtual?.estado === destino[0]) return;
      const lista = document.getElementById(destino[1]);
      const ordem = lista.querySelectorAll(".task-card").length;
      await executar(() => actions.moveTask({ tarefa_id: card.dataset.taskId, novo_estado: destino[0], nova_ordem: ordem }));
    }
  });
  busca?.addEventListener("input", () => { termo = busca.value; aplicarBusca(); });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && document.activeElement === busca && busca.value) { busca.value = ""; termo = ""; aplicarBusca(); }
  });

  return Object.freeze({
    render,
    focusTask(id) {
      const painelQuadro = document.querySelector('[data-view-panel="quadro"]');
      if (painelQuadro?.hidden) document.querySelector('[data-view="quadro"]')?.click();
      const card = [...document.querySelectorAll(".task-card[data-task-id]")].find(node => node.dataset.taskId === id);
      if (!card) return false;
      if (card.closest("li")?.hidden) card.closest("li").hidden = false;
      card.classList.add("is-calendar-focus");
      card.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "center" });
      card.focus({ preventScroll: true });
      window.setTimeout(() => card.classList.remove("is-calendar-focus"), 2200);
      return true;
    },
  });
}
