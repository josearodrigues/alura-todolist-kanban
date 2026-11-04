"""Testes unitários para cálculos estatísticos e métricas em metrics.py."""

import pytest
from todolist.metrics import (
    calcular_foco_hoje,
    calcular_relatorio_completo,
    calcular_resumo_projeto,
)

DATA_HOJE = "2026-11-02"


def test_calcular_resumo_projeto_vazio():
    """Testa proteção contra divisão por zero com 0 tarefas (RF09)."""
    resumo = calcular_resumo_projeto([])
    assert resumo["total"] == 0
    assert resumo["concluidas"] == 0
    assert resumo["pendentes"] == 0
    assert resumo["perc_concluidas"] == 0.0
    assert resumo["perc_pendentes"] == 0.0


def test_calcular_resumo_projeto_com_tarefas():
    """Testa percentual com uma casa decimal e pendentes por diferença."""
    tarefas = [
        {"estado": "concluida"},
        {"estado": "a_fazer"},
        {"estado": "em_andamento"},
    ]
    resumo = calcular_resumo_projeto(tarefas)
    assert resumo["total"] == 3
    assert resumo["concluidas"] == 1
    assert resumo["pendentes"] == 2
    # 1/3 = 33.3%, pendentes = 100 - 33.3 = 66.7%
    assert resumo["perc_concluidas"] == 33.3
    assert resumo["perc_pendentes"] == 66.7


def test_calcular_foco_hoje():
    """Testa contagem do banner Foco de Hoje (RF10): não concluídas com data_limite <= data_atual_local."""
    tarefas = [
        {"estado": "a_fazer", "data_limite": "2026-11-01"},  # Passada (atrasada) -> conta
        {"estado": "em_andamento", "data_limite": "2026-11-02"},  # Hoje -> conta
        {"estado": "a_fazer", "data_limite": "2026-11-03"},  # Futura -> não conta
        {"estado": "concluida", "data_limite": "2026-11-01"},  # Concluída -> não conta
        {"estado": "a_fazer", "data_limite": None},  # Sem data -> não conta
    ]
    foco = calcular_foco_hoje(tarefas, DATA_HOJE)
    assert foco == 2

    # Erro de data nula ou formato
    with pytest.raises(ValueError):
        calcular_foco_hoje(tarefas, None)

    with pytest.raises(ValueError):
        calcular_foco_hoje(tarefas, "02/11/2026")


def test_calcular_relatorio_completo_e_periodo_conclusao():
    """Testa módulo completo de relatórios e filtro estrito por data_conclusao (RF12)."""
    tarefas = [
        # Atrasada
        {"estado": "a_fazer", "prioridade": "alta", "data_limite": "2026-11-01", "data_conclusao": None},
        # Vence Hoje
        {"estado": "em_andamento", "prioridade": "media", "data_limite": "2026-11-02", "data_conclusao": None},
        # Vence nos Próximos 7 dias (ex: 2026-11-05)
        {"estado": "a_fazer", "prioridade": "baixa", "data_limite": "2026-11-05", "data_conclusao": None},
        # Concluída no período (data_conclusao 2026-11-02)
        {"estado": "concluida", "prioridade": "alta", "data_limite": "2026-10-25", "data_conclusao": "2026-11-02T10:00:00.000Z"},
        # Concluída fora do período (data_conclusao 2026-10-15)
        {"estado": "concluida", "prioridade": "media", "data_limite": "2026-10-10", "data_conclusao": "2026-10-15T10:00:00.000Z"},
    ]

    # Sem filtro de período de conclusão
    rel = calcular_relatorio_completo(tarefas, DATA_HOJE)
    assert rel["total"] == 5
    assert rel["por_estado"]["a_fazer"] == 2
    assert rel["por_estado"]["em_andamento"] == 1
    assert rel["por_estado"]["concluida"] == 2
    assert rel["por_prioridade"]["alta"] == 2
    assert rel["por_prioridade"]["media"] == 2
    assert rel["por_prioridade"]["baixa"] == 1
    assert rel["atrasadas"] == 1
    assert rel["vencem_hoje"] == 1
    assert rel["proximos_7_dias"] == 1
    assert rel["concluidas_no_periodo"] == 2

    # Com filtro de período de conclusão: apenas novembro de 2026
    rel_filtrado = calcular_relatorio_completo(
        tarefas,
        DATA_HOJE,
        periodo_conclusao_inicio="2026-11-01",
        periodo_conclusao_fim="2026-11-30",
    )
    assert rel_filtrado["concluidas_no_periodo"] == 1


def test_calcular_relatorio_erros():
    """Testa validações de erro no cálculo de relatórios."""
    with pytest.raises(ValueError):
        calcular_relatorio_completo([], None)

def test_calcular_relatorio_rejeita_limites_de_periodo_invalidos():
    """Os limites do filtro de conclusão precisam ser datas válidas e ordenadas."""
    with pytest.raises(ValueError, match="formato YYYY-MM-DD"):
        calcular_relatorio_completo(
            [], DATA_HOJE, periodo_conclusao_inicio="02/11/2026"
        )
    with pytest.raises(ValueError, match="data inexistente"):
        calcular_relatorio_completo(
            [], DATA_HOJE, periodo_conclusao_fim="2026-02-30"
        )
    with pytest.raises(ValueError, match="não pode ser posterior"):
        calcular_relatorio_completo(
            [],
            DATA_HOJE,
            periodo_conclusao_inicio="2026-11-30",
            periodo_conclusao_fim="2026-11-01",
        )



def test_preparar_apresentacao_kanban_ordena_por_coluna_e_ordem():
    from todolist.metrics import preparar_apresentacao_kanban
    tarefas = [
        {"id": "c", "estado": "concluida", "ordem": 0, "data_limite": None},
        {"id": "b", "estado": "a_fazer", "ordem": 1, "data_limite": None},
        {"id": "a", "estado": "a_fazer", "ordem": 0, "data_limite": None},
        {"id": "d", "estado": "em_andamento", "ordem": 0, "data_limite": None},
    ]
    resultado = preparar_apresentacao_kanban(tarefas, DATA_HOJE)
    assert [x["id"] for x in resultado["tarefas_ordenadas"]] == ["a", "b", "d", "c"]
    assert resultado["ids_atrasadas"] == []


def test_preparar_apresentacao_kanban_identifica_atrasadas():
    from todolist.metrics import preparar_apresentacao_kanban
    tarefas = [
        {"id": "atrasada", "estado": "a_fazer", "ordem": 0, "data_limite": "2026-11-01"},
        {"id": "hoje", "estado": "em_andamento", "ordem": 0, "data_limite": DATA_HOJE},
        {"id": "futura", "estado": "a_fazer", "ordem": 1, "data_limite": "2026-11-03"},
        {"id": "concluida", "estado": "concluida", "ordem": 0, "data_limite": "2026-11-01"},
        {"id": "sem_prazo", "estado": "a_fazer", "ordem": 2, "data_limite": None},
    ]
    assert preparar_apresentacao_kanban(tarefas, DATA_HOJE)["ids_atrasadas"] == ["atrasada"]


def test_preparar_apresentacao_kanban_rejeita_data_invalida():
    from todolist.metrics import preparar_apresentacao_kanban
    with pytest.raises(ValueError):
        preparar_apresentacao_kanban([], "02/11/2026")
