"""Cálculos estatísticos, métricas e relatórios do To-Do List Kanban.

Implementação das métricas do RF09, RF10 e RF12 com total determinismo temporal.
"""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from todolist.models import Tarefa, validar_data_limite


def calcular_resumo_projeto(tarefas: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calcula o resumo geral do projeto (RF09).

    - total: total de tarefas.
    - concluidas: contagem de tarefas no estado 'concluida'.
    - pendentes: contagem de tarefas nos estados 'a_fazer' e 'em_andamento'.
    - perc_concluidas: percentual com uma casa decimal (0 tarefas = 0.0%).
    - perc_pendentes: calculado estritamente por diferença (100.0% - perc_concluidas).
    """
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t.get("estado") == "concluida")
    pendentes = total - concluidas

    if total == 0:
        perc_concluidas = 0.0
        perc_pendentes = 0.0
    else:
        # 1 casa decimal
        perc_concluidas = round((concluidas / total) * 100.0, 1)
        perc_pendentes = round(100.0 - perc_concluidas, 1)

    return {
        "total": total,
        "concluidas": concluidas,
        "pendentes": pendentes,
        "perc_concluidas": perc_concluidas,
        "perc_pendentes": perc_pendentes,
    }


def calcular_foco_hoje(
    tarefas: List[Dict[str, Any]],
    data_local_referencia: str,
) -> int:
    """Calcula o total do banner 'Foco de Hoje' (RF10).

    Critério: Tarefas não concluídas com data_limite <= data_atual_local.
    Exige data_local_referencia no formato YYYY-MM-DD.
    """
    validar_data_limite(data_local_referencia)
    if data_local_referencia is None:
        raise ValueError("data_local_referencia não pode ser nula.")

    total_foco = 0
    for t in tarefas:
        estado = t.get("estado")
        data_limite = t.get("data_limite")
        if estado != "concluida" and data_limite is not None:
            if data_limite <= data_local_referencia:
                total_foco += 1

    return total_foco


def calcular_relatorio_completo(
    tarefas: List[Dict[str, Any]],
    data_local_referencia: str,
    periodo_conclusao_inicio: Optional[str] = None,
    periodo_conclusao_fim: Optional[str] = None,
) -> Dict[str, Any]:
    """Calcula todos os indicadores do módulo de relatórios (RF12).

    Indicadores:
    - total: total geral de tarefas
    - por_estado: contagem por estado (a_fazer, em_andamento, concluida)
    - por_prioridade: contagem por prioridade (baixa, media, alta)
    - atrasadas: data_limite < data_local_referencia e estado != "concluida"
    - vencem_hoje: data_limite == data_local_referencia e estado != "concluida"
    - proximos_7_dias: data_local_referencia + 1 <= data_limite <= data_local_referencia + 7 e estado != "concluida"
    - concluidas_no_periodo: tarefas concluídas filtradas estritamente por data_conclusao
    """
    validar_data_limite(data_local_referencia)
    if data_local_referencia is None:
        raise ValueError("data_local_referencia é obrigatória.")

    # Validar os limites opcionais e impedir intervalos invertidos.
    if periodo_conclusao_inicio is not None:
        validar_data_limite(periodo_conclusao_inicio)
    if periodo_conclusao_fim is not None:
        validar_data_limite(periodo_conclusao_fim)
    if (
        periodo_conclusao_inicio is not None
        and periodo_conclusao_fim is not None
        and periodo_conclusao_inicio > periodo_conclusao_fim
    ):
        raise ValueError("periodo_conclusao_inicio não pode ser posterior a periodo_conclusao_fim.")

    dt_ref = datetime.strptime(data_local_referencia, "%Y-%m-%d").date()
    dt_amanha = dt_ref + timedelta(days=1)
    dt_limite_7_dias = dt_ref + timedelta(days=7)

    str_amanha = dt_amanha.strftime("%Y-%m-%d")
    str_7_dias = dt_limite_7_dias.strftime("%Y-%m-%d")

    total = len(tarefas)
    por_estado = {"a_fazer": 0, "em_andamento": 0, "concluida": 0}
    por_prioridade = {"baixa": 0, "media": 0, "alta": 0}
    atrasadas = 0
    vencem_hoje = 0
    proximos_7_dias = 0

    for t in tarefas:
        estado = t.get("estado")
        prioridade = t.get("prioridade")
        data_limite = t.get("data_limite")

        if estado in por_estado:
            por_estado[estado] += 1
        if prioridade in por_prioridade:
            por_prioridade[prioridade] += 1

        if estado != "concluida" and data_limite is not None:
            if data_limite < data_local_referencia:
                atrasadas += 1
            elif data_limite == data_local_referencia:
                vencem_hoje += 1
            elif str_amanha <= data_limite <= str_7_dias:
                proximos_7_dias += 1

    # Concluídas no período (baseado estritamente em data_conclusao)
    concluidas_no_periodo = 0
    for t in tarefas:
        if t.get("estado") == "concluida":
            dt_conc = t.get("data_conclusao")
            if dt_conc is not None:
                # Extrai a parte da data YYYY-MM-DD do ISO UTC para comparação de período
                data_conc_dia = dt_conc[:10]
                if periodo_conclusao_inicio and data_conc_dia < periodo_conclusao_inicio:
                    continue
                if periodo_conclusao_fim and data_conc_dia > periodo_conclusao_fim:
                    continue
                concluidas_no_periodo += 1

    return {
        "total": total,
        "por_estado": por_estado,
        "por_prioridade": por_prioridade,
        "atrasadas": atrasadas,
        "vencem_hoje": vencem_hoje,
        "proximos_7_dias": proximos_7_dias,
        "concluidas_no_periodo": concluidas_no_periodo,
    }
