/**
 * Exportação e importação estrita de backups JSON.
 * A validação e a preparação do estado candidato são executadas pelo domínio Python.
 */
export function initializeBackupUI({ actions, notify }) {
  const exportButton = document.getElementById("executar-exportacao");
  const fileInput = document.getElementById("arquivo-importacao");
  const selectedFile = document.getElementById("arquivo-selecionado");
  const validateButton = document.getElementById("validar-arquivo-importacao");
  const importStatus = document.getElementById("importacao-status");
  const importDialog = document.getElementById("dialog-importar");
  const exportDialog = document.getElementById("dialog-exportar");
  const confirmationDialog = document.getElementById("dialog-confirmar-importacao");
  const currentCount = document.getElementById("quantidade-atual-importacao");
  const newCount = document.getElementById("quantidade-nova-importacao");
  const confirmationStatus = document.getElementById("confirmacao-importacao-status");
  const confirmButton = document.getElementById("confirmar-substituicao-importacao");
  const cancelConfirmationButton = confirmationDialog?.querySelector("[data-dialog-close]");

  if (
    !exportButton || !fileInput || !selectedFile || !validateButton || !importStatus ||
    !importDialog || !exportDialog || !confirmationDialog || !currentCount ||
    !newCount || !confirmationStatus || !confirmButton || !cancelConfirmationButton
  ) {
    throw new Error("A estrutura de importação/exportação está incompleta.");
  }

  let estadoCandidato = null;

  async function exportarBackup() {
    exportButton.disabled = true;
    try {
      const envelope = await actions.createBackup();
      const conteudo = JSON.stringify(envelope, null, 2);
      const arquivo = new Blob([conteudo], { type: "application/json;charset=utf-8" });
      const url = URL.createObjectURL(arquivo);
      const link = document.createElement("a");
      const identificador = envelope.data_exportacao.replace(/[:.]/g, "-");

      link.href = url;
      link.download = "kanban-backup-" + identificador + ".json";
      link.hidden = true;
      document.body.append(link);
      link.click();
      link.remove();
      window.setTimeout(() => URL.revokeObjectURL(url), 1000);

      exportDialog.close();
      notify("Backup JSON exportado com sucesso.", "success");
    } catch (erro) {
      notify("Não foi possível exportar o backup: " + erro.message, "error");
    } finally {
      exportButton.disabled = false;
    }
  }

  async function validarArquivo() {
    const arquivo = fileInput.files && fileInput.files[0];
    if (!arquivo) {
      importStatus.textContent = "Selecione um arquivo JSON antes de validar.";
      return;
    }

    validateButton.disabled = true;
    importStatus.textContent = "Lendo e validando o arquivo...";
    importStatus.dataset.state = "loading";
    estadoCandidato = null;

    try {
      const conteudo = await arquivo.text();
      const preparado = await actions.validateBackup(conteudo);

      if (!preparado || !Array.isArray(preparado.tarefas)) {
        throw new Error("O domínio Python não retornou um estado de importação válido.");
      }

      estadoCandidato = {
        tarefas: preparado.tarefas,
        timestamp_ultima_alteracao: preparado.timestamp_ultima_alteracao,
      };

      currentCount.textContent = String(actions.getState().tarefas.length);
      newCount.textContent = String(estadoCandidato.tarefas.length);
      confirmationStatus.textContent = "Arquivo validado. Nenhum dado foi alterado até a confirmação.";
      confirmationStatus.dataset.state = "success";
      importStatus.textContent = "Arquivo válido: " + arquivo.name;
      importStatus.dataset.state = "success";

      if (!confirmationDialog.open) confirmationDialog.showModal();
    } catch (erro) {
      console.error("Falha na validação do backup JSON:", erro);
      importStatus.textContent = "Não foi possível validar este arquivo. Verifique se ele é um backup JSON válido do To-Do List Kanban.";
      importStatus.dataset.state = "error";
      notify("Não foi possível importar este arquivo. Verifique se ele é um backup JSON válido do To-Do List Kanban. Seus dados atuais foram preservados.", "error");
    } finally {
      validateButton.disabled = !(fileInput.files && fileInput.files.length);
    }
  }

  async function confirmarSubstituicao() {
    if (!estadoCandidato) {
      confirmationStatus.textContent = "Valide novamente o arquivo antes de confirmar.";
      confirmationStatus.dataset.state = "error";
      return;
    }

    confirmButton.disabled = true;
    cancelConfirmationButton.disabled = true;
    confirmationStatus.textContent = "Gravando e atualizando o quadro...";
    confirmationStatus.dataset.state = "loading";

    try {
      const estadoConfirmado = await actions.prepareImportedState(estadoCandidato.tarefas);
      const resultado = await actions.replaceState(estadoConfirmado);
      if (!resultado.success) {
        confirmationStatus.textContent = "A substituição não foi concluída. Os dados anteriores permanecem preservados.";
        confirmationStatus.dataset.state = "error";
        return;
      }

      const totalImportado = estadoCandidato.tarefas.length;
      confirmationDialog.close();
      importDialog.close();
      estadoCandidato = null;
      fileInput.value = "";
      selectedFile.textContent = "Nenhum arquivo selecionado.";
      importStatus.textContent = "";
      notify("Backup importado com sucesso: " + totalImportado + " tarefa(s).", "success");
    } catch (erro) {
      confirmationStatus.textContent = "A substituição falhou. Os dados anteriores foram preservados. " + erro.message;
      confirmationStatus.dataset.state = "error";
      notify("Não foi possível importar o backup. " + erro.message, "error");
    } finally {
      confirmButton.disabled = false;
      cancelConfirmationButton.disabled = false;
    }
  }

  confirmationDialog.addEventListener("cancel", (event) => {
    if (confirmButton.disabled) event.preventDefault();
  });

  exportButton.addEventListener("click", () => void exportarBackup());
  validateButton.addEventListener("click", () => void validarArquivo());
  confirmButton.addEventListener("click", () => void confirmarSubstituicao());

  fileInput.addEventListener("change", () => {
    estadoCandidato = null;
    const arquivo = fileInput.files && fileInput.files[0];
    selectedFile.textContent = arquivo ? arquivo.name : "Nenhum arquivo selecionado.";
    importStatus.textContent = "";
    validateButton.disabled = !arquivo;
  });

  importDialog.addEventListener("close", () => {
    if (confirmationDialog.open) return;
    estadoCandidato = null;
    fileInput.value = "";
    selectedFile.textContent = "Nenhum arquivo selecionado.";
    importStatus.textContent = "";
    validateButton.disabled = true;
  });
}
