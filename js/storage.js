/**
 * Persistência local do estado consolidado do Kanban.
 * A gravação é síncrona; o chamador só confirma memória/UI após writeState retornar.
 */

export const STORAGE_KEY = "kanban_app_state";

export function createStorage({ storage = null, key = STORAGE_KEY } = {}) {
  function obterStorage() {
    const instancia = storage ?? globalThis.localStorage;
    if (!instancia) {
      throw new Error("O armazenamento local não está disponível neste navegador.");
    }
    return instancia;
  }

  function readRaw() {
    return obterStorage().getItem(key);
  }

  function readState(validate) {
    const bruto = readRaw();

    if (bruto === null) {
      return {
        state: { tarefas: [], timestamp_ultima_alteracao: null },
        exists: false,
        raw: null,
      };
    }

    let estado;
    try {
      estado = JSON.parse(bruto);
    } catch {
      throw new Error("Os dados salvos do Kanban não contêm um JSON válido.");
    }

    if (
      !estado ||
      typeof estado !== "object" ||
      Array.isArray(estado) ||
      Object.keys(estado).sort().join(",") !== "tarefas,timestamp_ultima_alteracao"
    ) {
      throw new Error("A estrutura dos dados salvos do Kanban é inválida.");
    }

    if (typeof validate === "function") validate(estado);
    if (!Array.isArray(estado.tarefas)) {
      throw new Error("O campo tarefas dos dados salvos deve ser uma lista.");
    }

    return {
      state: {
        tarefas: estado.tarefas.map((tarefa) => ({ ...tarefa })),
        timestamp_ultima_alteracao: estado.timestamp_ultima_alteracao,
      },
      exists: true,
      raw: bruto,
    };
  }

  function writeState(estado) {
    const payload = JSON.stringify({
      tarefas: estado.tarefas,
      timestamp_ultima_alteracao: estado.timestamp_ultima_alteracao,
    });

    if (typeof payload !== "string") {
      throw new Error("Não foi possível serializar o estado do Kanban.");
    }

    obterStorage().setItem(key, payload);
    return payload;
  }

  function restoreRaw(valorAnterior) {
    const instancia = obterStorage();
    if (valorAnterior === null) instancia.removeItem(key);
    else instancia.setItem(key, valorAnterior);
  }

  return Object.freeze({ key, readRaw, readState, writeState, restoreRaw });
}
