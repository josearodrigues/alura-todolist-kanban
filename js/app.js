import {
  executeDomainOperation,
  initializePythonRuntime,
  validateState,
  calculateMetrics,
} from "./pyodide_bridge.js";
import { createKanbanUI } from "./kanban_ui.js";
import { initializeDragDrop } from "./drag_drop.js";
import { initializeCalendar } from "./calendar_ui.js";
import { createStorage } from "./storage.js";

const STORAGE = createStorage();
let estadoAtual = { tarefas: [], timestamp_ultima_alteracao: null };
let runtimeDisponivel = false;
let persistenciaDisponivel = false;
let kanbanUI = null;
let calendarioUI = null;

function copiarEstado(estado) {
  return {
    tarefas: estado.tarefas.map((tarefa) => ({ ...tarefa })),
    timestamp_ultima_alteracao: estado.timestamp_ultima_alteracao,
  };
}

function atualizarStatusRuntime(tipo, mensagem = "") {
  const indicador = document.getElementById("pyodide-status");
  if (!indicador) return;

  indicador.classList.remove("loaded", "runtime-error");
  if (tipo === "success") {
    indicador.classList.add("loaded");
    indicador.textContent = "✓ Carregado";
    indicador.removeAttribute("title");
  } else if (tipo === "error") {
    indicador.classList.add("runtime-error");
    indicador.textContent = "⚠ Erro";
    indicador.title = mensagem;
  } else {
    indicador.textContent = "Inicializando...";
  }
}

let avisoTimeout = null;

function notificarUsuario(mensagem, tipo = "error") {
  let aviso = document.getElementById("app-notice");

  if (!aviso) {
    aviso = document.createElement("div");
    aviso.id = "app-notice";
    aviso.className = "app-notice";
    document.body.append(aviso);
  }

  if (avisoTimeout !== null) {
    window.clearTimeout(avisoTimeout);
  }

  aviso.dataset.type = tipo;
  aviso.setAttribute("role", tipo === "error" ? "alert" : "status");
  aviso.setAttribute("aria-live", tipo === "error" ? "assertive" : "polite");
  aviso.textContent = mensagem;
  aviso.hidden = false;

  avisoTimeout = window.setTimeout(() => {
    aviso.hidden = true;
    avisoTimeout = null;
  }, 5000);
}

function formatarTimestamp(timestamp) {
  if (!timestamp) return null;
  const data = new Date(timestamp);
  if (Number.isNaN(data.getTime())) return null;

  return {
    datetime: data.toISOString(),
    texto: new Intl.DateTimeFormat("pt-BR", {
      dateStyle: "short",
      timeStyle: "short",
    }).format(data),
  };
}

function atualizarTimestampInterface(timestamp) {
  const formatado = formatarTimestamp(timestamp);
  const elementos = [
    document.getElementById("ultima-alteracao"),
    document.querySelector(".footer-meta time"),
  ].filter(Boolean);

  elementos.forEach((elemento) => {
    if (!formatado) {
      elemento.removeAttribute("datetime");
      elemento.textContent = "Sem alterações";
      return;
    }

    elemento.dateTime = formatado.datetime;
    elemento.textContent = formatado.texto;
  });
}

function renderizarQuadro(estado) {
  if (kanbanUI) kanbanUI.render(estado);
}

async function validarEGravarEstado(candidato) {
  if (!persistenciaDisponivel) {
    throw new Error("A persistência não foi inicializada com segurança.");
  }

  await validateState(candidato);
  const estadoAnterior = copiarEstado(estadoAtual);
  const brutoAnterior = STORAGE.readRaw();

  try {
    // Persistência preventiva: setItem precisa concluir antes da confirmação.
    STORAGE.writeState(candidato);
  } catch (erroGravacao) {
    estadoAtual = estadoAnterior;
    throw erroGravacao;
  }

  try {
    estadoAtual = copiarEstado(candidato);
    renderizarQuadro(estadoAtual);
    atualizarTimestampInterface(estadoAtual.timestamp_ultima_alteracao);
  } catch (erroInterface) {
    estadoAtual = estadoAnterior;
    try {
      STORAGE.restoreRaw(brutoAnterior);
    } catch (erroRollback) {
      console.error("Falha adicional ao restaurar o documento anterior:", erroRollback);
    }
    renderizarQuadro(estadoAnterior);
    throw new Error(
      `A gravação foi revertida porque a interface não pôde ser atualizada: ${erroInterface.message}`,
    );
  }

  return true;
}

async function executarOperacao(operacao, dados) {
  if (!runtimeDisponivel || !persistenciaDisponivel) {
    throw new Error("O núcleo Python e a persistência ainda não estão disponíveis.");
  }

  const resultado = await executeDomainOperation(operacao, estadoAtual, dados);
  const candidato = {
    tarefas: resultado.tarefas,
    timestamp_ultima_alteracao: resultado.timestamp_ultima_alteracao,
  };

  if (JSON.stringify(candidato) === JSON.stringify(estadoAtual)) {
    return { success: true, changed: false, tarefa: resultado.tarefa };
  }

  try {
    await validarEGravarEstado(candidato);
    return { success: true, changed: true, tarefa: resultado.tarefa };
  } catch (erro) {
    notificarUsuario(
      `Não foi possível salvar a alteração. Os dados anteriores foram preservados. ${erro.message}`,
    );
    return { success: false, changed: false, error: erro };
  }
}

function publicarApiAplicacao() {
  window.kanbanApp = Object.freeze({
    getState: () => copiarEstado(estadoAtual),
    createTask: (dados) => executarOperacao("criar", dados),
    editTask: (dados) => executarOperacao("editar", dados),
    moveTask: (dados) => executarOperacao("mover", dados),
    deleteTask: (dados) => executarOperacao("excluir", dados),
    replaceState: async (novoEstado) => {
      if (!runtimeDisponivel || !persistenciaDisponivel) {
        throw new Error("O núcleo Python e a persistência ainda não estão disponíveis.");
      }
      try {
        await validarEGravarEstado(novoEstado);
        return { success: true };
      } catch (erro) {
        notificarUsuario(
          `Não foi possível substituir os dados. O estado anterior foi preservado. ${erro.message}`,
        );
        return { success: false, error: erro };
      }
    },
    getMetrics: (dataLocal) => calculateMetrics(estadoAtual, dataLocal),
    validateState,
  });
}

async function inicializarAplicacao() {
  atualizarStatusRuntime("loading");

  try {
    await initializePythonRuntime();
    runtimeDisponivel = true;
    atualizarStatusRuntime("success");

    try {
      const recuperado = STORAGE.readState((estado) => {
        if (!estado || !Array.isArray(estado.tarefas)) {
          throw new Error("Estrutura de persistência inválida.");
        }
      });

      await validateState(recuperado.state);
      estadoAtual = copiarEstado(recuperado.state);
      persistenciaDisponivel = true;

      renderizarQuadro(estadoAtual);
      atualizarTimestampInterface(estadoAtual.timestamp_ultima_alteracao);
    } catch (erroPersistencia) {
      persistenciaDisponivel = false;
      notificarUsuario(
        `Não foi possível recuperar os dados salvos. Nenhum dado foi sobrescrito. ${erroPersistencia.message}`,
      );
      console.error("Falha ao recuperar estado persistido:", erroPersistencia);
    }

    publicarApiAplicacao();
    kanbanUI = createKanbanUI({
      getState: () => estadoAtual,
      actions: window.kanbanApp,
      notify: (mensagem) => notificarUsuario(mensagem),
      onStateRendered: () => calendarioUI?.render(),
    });
    kanbanUI.render(estadoAtual);
    calendarioUI = initializeCalendar({
      getTasks: () => estadoAtual.tarefas,
      onFocusTask: (id) => kanbanUI.focusTask(id),
    });
    initializeDragDrop({
      onMove: (dados) => window.kanbanApp.moveTask(dados),
      notify: (mensagem) => notificarUsuario(mensagem),
    });
    console.info("Aplicação inicializada. API disponível em window.kanbanApp.");
  } catch (erroRuntime) {
    const carregamento = document.getElementById("kanban-loading");
    if (carregamento) carregamento.textContent = "Não foi possível carregar as tarefas. Verifique sua conexão e recarregue a página.";
    document.getElementById("colunas-kanban")?.setAttribute("aria-busy", "false");
    atualizarStatusRuntime("error", erroRuntime.message);
    notificarUsuario(
      `Não foi possível inicializar o núcleo Python. Verifique sua conexão e recarregue a página. ${erroRuntime.message}`,
    );
    console.error("Falha na inicialização do Pyodide:", erroRuntime);
  }
}

(() => {
      const search = document.getElementById("busca-tarefas");
      const themeButton = document.getElementById("alternar-tema");
      const themeStorageKey = "kanban-theme";
      const sidebar = document.getElementById("sidebar");
      const mobileNavButton = document.getElementById("mobile-nav-toggle");
      const mobileNavBackdrop = document.getElementById("mobile-nav-backdrop");
      const mobileNavMedia = window.matchMedia("(max-width: 960px)");

      const setMobileNav = (open, restoreFocus = false) => {
        if (!mobileNavMedia.matches) {
          sidebar.classList.remove("is-open");
          sidebar.inert = false;
          sidebar.setAttribute("aria-hidden", "false");
          mobileNavBackdrop.hidden = true;
          mobileNavButton.setAttribute("aria-expanded", "false");
          mobileNavButton.setAttribute("aria-label", "Abrir navegação");
          return;
        }

        sidebar.classList.toggle("is-open", open);
        sidebar.inert = !open;
        sidebar.setAttribute("aria-hidden", String(!open));
        mobileNavBackdrop.hidden = !open;
        mobileNavButton.setAttribute("aria-expanded", String(open));
        mobileNavButton.setAttribute("aria-label", open ? "Fechar navegação" : "Abrir navegação");

        if (open) {
          sidebar.querySelector("[data-view]")?.focus();
        } else if (restoreFocus) {
          mobileNavButton.focus();
        }
      };

      setMobileNav(false);
      mobileNavMedia.addEventListener("change", () => setMobileNav(false));

      const applyTheme = (theme, persist = false) => {
        const isDark = theme === "dark";
        document.documentElement.dataset.theme = isDark ? "dark" : "light";
        themeButton.setAttribute("aria-pressed", String(isDark));
        
        themeButton.setAttribute(
          "aria-label",
          isDark ? "Ativar tema claro" : "Ativar tema escuro"
        );
        if (persist) {
          try {
            localStorage.setItem(themeStorageKey, theme);
          } catch {
            // A preferência continua ativa nesta sessão se o armazenamento estiver indisponível.
          }
        }
      };

      let savedTheme = null;
      try {
        savedTheme = localStorage.getItem(themeStorageKey);
      } catch {
        // A preferência do sistema será usada como alternativa.
      }
      const preferredTheme = savedTheme === "light" || savedTheme === "dark"
        ? savedTheme
        : (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      applyTheme(preferredTheme);

      themeButton.addEventListener("click", () => {
        const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        applyTheme(nextTheme, true);
      });

      mobileNavButton.addEventListener("click", () => {
        setMobileNav(mobileNavButton.getAttribute("aria-expanded") !== "true");
      });
      mobileNavBackdrop.addEventListener("click", () => setMobileNav(false, true));

      document.addEventListener("click", (event) => {
        const viewButton = event.target.closest("[data-view]");
        if (viewButton) {
          const view = viewButton.dataset.view;
          document.querySelectorAll("[data-view-panel]").forEach((element) => { element.hidden = view !== "quadro"; });
          document.querySelectorAll("[data-page-view]").forEach((element) => { element.hidden = element.dataset.pageView !== view; });
          document.querySelector("[data-board-insights]").hidden = view !== "quadro";
          document.querySelectorAll("[data-view]").forEach((button) => {
            if (button.dataset.view === view) button.setAttribute("aria-current", "page");
            else button.removeAttribute("aria-current");
          });
          document.querySelector(".workspace").scrollTo({ top: 0, behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
          if (mobileNavMedia.matches && mobileNavButton.getAttribute("aria-expanded") === "true") {
            setMobileNav(false, true);
          }
          return;
        }

        const openButton = event.target.closest("[data-dialog-open]");
        if (openButton) {
          const dialog = document.getElementById(openButton.dataset.dialogOpen);
          if (dialog instanceof HTMLDialogElement && !dialog.open) {
            dialog.showModal();
          }
          return;
        }

        const closeButton = event.target.closest("[data-dialog-close]");
        if (closeButton) {
          const dialog = closeButton.closest("dialog");
          if (dialog instanceof HTMLDialogElement && dialog.open) {
            dialog.close();
          }
        }
      });

      document.addEventListener("keydown", (event) => {
        const openDialog = [...document.querySelectorAll("dialog[open]")].at(-1);

        if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
          event.preventDefault();
          if (!openDialog) {
            search.focus();
          }
          return;
        }

        if (event.key === "Tab" && mobileNavMedia.matches && mobileNavButton.getAttribute("aria-expanded") === "true") {
          const focusable = [...sidebar.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])')]
            .filter((element) => element.getClientRects().length > 0 && !element.closest("[inert]"));
          const first = focusable[0];
          const last = focusable[focusable.length - 1];

          if (first && last && event.shiftKey && (document.activeElement === first || !sidebar.contains(document.activeElement))) {
            event.preventDefault();
            last.focus();
          } else if (first && last && !event.shiftKey && (document.activeElement === last || !sidebar.contains(document.activeElement))) {
            event.preventDefault();
            first.focus();
          }
          return;
        }

        if (event.key === "Tab" && openDialog) {
          const focusableElements = [
            ...openDialog.querySelectorAll(
              'a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, [contenteditable="true"], summary, [tabindex]:not([tabindex="-1"])'
            )
          ].filter((element) =>
            element.getClientRects().length > 0 &&
            getComputedStyle(element).visibility !== "hidden" &&
            !element.closest("[inert]")
          );

          const firstElement = focusableElements[0];
          const lastElement = focusableElements[focusableElements.length - 1];

          if (!firstElement) {
            event.preventDefault();
            openDialog.focus();
            return;
          }

          if (
            event.shiftKey &&
            (document.activeElement === firstElement || !openDialog.contains(document.activeElement))
          ) {
            event.preventDefault();
            lastElement.focus();
          } else if (
            !event.shiftKey &&
            (document.activeElement === lastElement || !openDialog.contains(document.activeElement))
          ) {
            event.preventDefault();
            firstElement.focus();
          }
          return;
        }

        if (event.key !== "Escape") {
          return;
        }

        if (openDialog) {
          event.preventDefault();
          openDialog.close();
          return;
        }

        if (mobileNavMedia.matches && mobileNavButton.getAttribute("aria-expanded") === "true") {
          event.preventDefault();
          setMobileNav(false, true);
          return;
        }

        const activeMenu = document.activeElement.closest?.("details[open]");
        const openMenu = activeMenu || [...document.querySelectorAll("details[open]")].at(-1);
        if (openMenu) {
          event.preventDefault();
          const summary = openMenu.querySelector(":scope > summary");
          openMenu.open = false;
          summary?.focus();
          return;
        }

        if (document.activeElement === search && search.value !== "") {
          event.preventDefault();
          search.value = "";
          search.dispatchEvent(new Event("input", { bubbles: true }));
        }
      });
    })();

inicializarAplicacao();
