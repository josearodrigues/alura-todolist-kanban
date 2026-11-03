/**
 * Apresentação do relatório dinâmico calculado pelo domínio Python.
 * O período vazio representa todo o histórico de conclusões.
 */
function dataLocalHoje() {
  const agora = new Date();
  const ano = agora.getFullYear();
  const mes = String(agora.getMonth() + 1).padStart(2, "0");
  const dia = String(agora.getDate()).padStart(2, "0");
  return ano + "-" + mes + "-" + dia;
}

export function initializeReportsUI({ getReport }) {
  const dialog = document.getElementById("dialog-relatorios");
  const inicio = document.getElementById("relatorio-periodo-inicio");
  const fim = document.getElementById("relatorio-periodo-fim");
  const limpar = document.getElementById("limpar-periodo-relatorio");
  const status = document.getElementById("relatorios-status");

  if (!dialog || !inicio || !fim || !limpar || !status || typeof getReport !== "function") {
    throw new Error("A estrutura do modal de relatórios está incompleta.");
  }

  let requisicaoAtual = 0;

  function definirValor(chave, valor) {
    const elemento = dialog.querySelector('[data-report-value="' + chave + '"]');
    if (elemento) elemento.textContent = String(valor);
  }

  async function atualizar() {
    const requisicao = ++requisicaoAtual;
    status.textContent = "Calculando indicadores...";
    status.dataset.state = "loading";

    try {
      const relatorio = await getReport(
        dataLocalHoje(),
        inicio.value || null,
        fim.value || null,
      );

      if (requisicao !== requisicaoAtual) return;

      definirValor("total", relatorio.total);
      definirValor("a_fazer", relatorio.por_estado.a_fazer);
      definirValor("em_andamento", relatorio.por_estado.em_andamento);
      definirValor("concluida", relatorio.por_estado.concluida);
      definirValor("baixa", relatorio.por_prioridade.baixa);
      definirValor("media", relatorio.por_prioridade.media);
      definirValor("alta", relatorio.por_prioridade.alta);
      definirValor("atrasadas", relatorio.atrasadas);
      definirValor("vencem_hoje", relatorio.vencem_hoje);
      definirValor("proximos_7_dias", relatorio.proximos_7_dias);
      definirValor("concluidas_no_periodo", relatorio.concluidas_no_periodo);

      const periodoSelecionado = inicio.value || fim.value;
      status.textContent = periodoSelecionado
        ? "Indicadores atualizados para o período de conclusão informado."
        : "Indicadores atualizados considerando todo o histórico de conclusões.";
      status.dataset.state = "success";
    } catch (erro) {
      if (requisicao !== requisicaoAtual) return;
      status.textContent = "Não foi possível calcular os relatórios: " + erro.message;
      status.dataset.state = "error";
    }
  }

  function abrir() {
    if (!dialog.open) dialog.showModal();
    void atualizar();
  }

  inicio.addEventListener("change", () => void atualizar());
  fim.addEventListener("change", () => void atualizar());
  limpar.addEventListener("click", () => {
    inicio.value = "";
    fim.value = "";
    void atualizar();
  });

  return Object.freeze({ open: abrir, refresh: atualizar });
}
