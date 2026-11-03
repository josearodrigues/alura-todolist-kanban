"""Testes unitários para as operações de negócio em services.py."""

import pytest
from todolist.services import (
    criar_tarefa,
    editar_tarefa,
    excluir_tarefa,
    mover_tarefa,
    obter_novo_id,
    obter_timestamp_utc_atual,
    reindexar_coluna,
    reordenar_tarefa,
)

UUID_1 = "11111111-1111-4111-8111-111111111111"
UUID_2 = "22222222-2222-4222-8222-222222222222"
UUID_3 = "33333333-3333-4333-8333-333333333333"

TS_1 = "2026-11-02T10:00:00.000Z"
TS_2 = "2026-11-02T11:00:00.000Z"
TS_3 = "2026-11-02T12:00:00.000Z"


def test_obter_novo_id_e_timestamp():
    """Testa geração de ID e timestamp sem injeção."""
    novo_id = obter_novo_id()
    assert len(novo_id) == 36
    ts = obter_timestamp_utc_atual()
    assert ts.endswith("Z")
    assert "T" in ts


def test_criar_tarefa_sucesso():
    """Testa criação de tarefa no estado obrigatório 'a_fazer' e contiguidade de ordem."""
    tarefas = []
    tarefas, ts1, t1 = criar_tarefa(
        tarefas=tarefas,
        titulo="Primeira Tarefa",
        descricao="Descrição 1",
        prioridade="alta",
        data_limite="2026-11-10",
        id_injetado=UUID_1,
        timestamp_injetado=TS_1,
    )
    assert len(tarefas) == 1
    assert t1["id"] == UUID_1
    assert t1["estado"] == "a_fazer"
    assert t1["ordem"] == 0
    assert t1["data_criacao"] == TS_1
    assert t1["data_atualizacao"] == TS_1
    assert t1["data_conclusao"] is None
    assert ts1 == TS_1

    # Criar segunda tarefa
    tarefas, ts2, t2 = criar_tarefa(
        tarefas=tarefas,
        titulo="Segunda Tarefa",
        id_injetado=UUID_2,
        timestamp_injetado=TS_2,
    )
    assert len(tarefas) == 2
    assert t2["id"] == UUID_2
    assert t2["ordem"] == 1
    assert t2["prioridade"] == "media"


def test_editar_tarefa_com_alteracao_real():
    """Testa edição com modificação efetiva: atualiza data_atualizacao e timestamp global."""
    tarefas, _, _ = criar_tarefa(
        [], "Título Original", "Desc", "media", "2026-11-10", UUID_1, TS_1
    )

    novas_tarefas, novo_ts_global, t_editada = editar_tarefa(
        tarefas=tarefas,
        tarefa_id=UUID_1,
        titulo="Título Atualizado",
        descricao="Desc Nova",
        prioridade="alta",
        data_limite="2026-11-20",
        timestamp_injetado=TS_2,
        timestamp_global_atual=TS_1,
    )

    assert novo_ts_global == TS_2
    assert t_editada["titulo"] == "Título Atualizado"
    assert t_editada["descricao"] == "Desc Nova"
    assert t_editada["prioridade"] == "alta"
    assert t_editada["data_limite"] == "2026-11-20"
    assert t_editada["data_atualizacao"] == TS_2

    # Metadados imutáveis preservados
    assert t_editada["id"] == UUID_1
    assert t_editada["data_criacao"] == TS_1
    assert t_editada["estado"] == "a_fazer"
    assert t_editada["ordem"] == 0
    assert t_editada["data_conclusao"] is None


def test_editar_tarefa_sem_alteracao_noop():
    """Testa edição sem alteração real (no-op): não altera data_atualizacao nem timestamp global."""
    tarefas, _, _ = criar_tarefa(
        [], "Título", "Desc", "media", "2026-11-10", UUID_1, TS_1
    )

    novas_tarefas, ts_global, t_retornada = editar_tarefa(
        tarefas=tarefas,
        tarefa_id=UUID_1,
        titulo="  Título  ",  # Mesmo valor após strip
        descricao="Desc",
        prioridade="media",
        data_limite="2026-11-10",
        timestamp_injetado=TS_2,
        timestamp_global_atual=TS_1,
    )

    assert ts_global == TS_1  # Mantém global inalterado
    assert t_retornada["data_atualizacao"] == TS_1  # Não gerou novo timestamp


def test_editar_tarefa_erros():
    """Testa validações de erro na edição."""
    tarefas, _, _ = criar_tarefa([], "Título", "Desc", "media", None, UUID_1, TS_1)

    # Tarefa inexistente
    with pytest.raises(ValueError, match="não encontrada para edição"):
        editar_tarefa(tarefas, UUID_2, "Novo Título", "", "media", None)

    # Título inválido (< 3)
    with pytest.raises(ValueError, match="entre 3 e 100 caracteres"):
        editar_tarefa(tarefas, UUID_1, "oi", "", "media", None)

    # Descrição inválida (> 500)
    with pytest.raises(ValueError, match="no máximo 500 caracteres"):
        editar_tarefa(tarefas, UUID_1, "Título Válido", "x" * 501, "media", None)

    # Prioridade inválida
    with pytest.raises(ValueError, match="Campo 'prioridade' inválido"):
        editar_tarefa(tarefas, UUID_1, "Título Válido", "", "urgente", None)

    # Data limite inválida
    with pytest.raises(ValueError, match="formato YYYY-MM-DD"):
        editar_tarefa(tarefas, UUID_1, "Título Válido", "", "media", "data-invalida")


def test_mover_tarefa_as_6_transicoes_de_estado():
    """Valida as 6 transições de estado aprovadas na Seção 6.1 do REQUISITOS.md."""
    # Cenário 1: a_fazer -> em_andamento
    tarefas, _, _ = criar_tarefa([], "Tarefa 1", "", "media", None, UUID_1, TS_1)
    tarefas, ts, t = mover_tarefa(tarefas, UUID_1, "em_andamento", timestamp_injetado=TS_2)
    assert t["estado"] == "em_andamento"
    assert t["data_atualizacao"] == TS_2
    assert t["data_conclusao"] is None

    # Cenário 4: em_andamento -> concluida
    tarefas, ts, t = mover_tarefa(tarefas, UUID_1, "concluida", timestamp_injetado=TS_3)
    assert t["estado"] == "concluida"
    assert t["data_atualizacao"] == TS_3
    assert t["data_conclusao"] == TS_3

    # Cenário 5: concluida -> a_fazer (reabertura)
    TS_4 = "2026-11-02T13:00:00.000Z"
    tarefas, ts, t = mover_tarefa(tarefas, UUID_1, "a_fazer", timestamp_injetado=TS_4)
    assert t["estado"] == "a_fazer"
    assert t["data_atualizacao"] == TS_4
    assert t["data_conclusao"] is None

    # Cenário 2: a_fazer -> concluida
    TS_5 = "2026-11-02T14:00:00.000Z"
    tarefas, ts, t = mover_tarefa(tarefas, UUID_1, "concluida", timestamp_injetado=TS_5)
    assert t["estado"] == "concluida"
    assert t["data_atualizacao"] == TS_5
    assert t["data_conclusao"] == TS_5

    # Cenário 6: concluida -> em_andamento (reabertura)
    TS_6 = "2026-11-02T15:00:00.000Z"
    tarefas, ts, t = mover_tarefa(tarefas, UUID_1, "em_andamento", timestamp_injetado=TS_6)
    assert t["estado"] == "em_andamento"
    assert t["data_atualizacao"] == TS_6
    assert t["data_conclusao"] is None

    # Cenário 3: em_andamento -> a_fazer
    TS_7 = "2026-11-02T16:00:00.000Z"
    tarefas, ts, t = mover_tarefa(tarefas, UUID_1, "a_fazer", timestamp_injetado=TS_7)
    assert t["estado"] == "a_fazer"
    assert t["data_atualizacao"] == TS_7
    assert t["data_conclusao"] is None


def test_mover_tarefa_reindexacao_origem_e_destino():
    """Testa que movimentar entre colunas reindexa origem e destino preservando datas originais."""
    t1 = {"id": UUID_1, "titulo": "Tarefa 1", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 0}
    t2 = {"id": UUID_2, "titulo": "Tarefa 2", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 1}
    t3 = {"id": UUID_3, "titulo": "Tarefa 3", "descricao": "", "estado": "em_andamento", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 0}

    tarefas = [t1, t2, t3]

    # Move T1 de a_fazer para em_andamento na posição 0
    novas_tarefas, ts, t_mov = mover_tarefa(
        tarefas=tarefas,
        tarefa_id=UUID_1,
        novo_estado="em_andamento",
        nova_ordem=0,
        timestamp_injetado=TS_2,
    )

    mapa = {t["id"]: t for t in novas_tarefas}
    # T2 na origem reindexado de 1 para 0 mantendo data_atualizacao TS_1
    assert mapa[UUID_2]["ordem"] == 0
    assert mapa[UUID_2]["data_atualizacao"] == TS_1

    # T1 no destino ficou em ordem 0 com data_atualizacao TS_2
    assert mapa[UUID_1]["ordem"] == 0
    assert mapa[UUID_1]["data_atualizacao"] == TS_2

    # T3 no destino deslocado de 0 para 1 mantendo data_atualizacao TS_1
    assert mapa[UUID_3]["ordem"] == 1
    assert mapa[UUID_3]["data_atualizacao"] == TS_1


def test_mover_tarefa_erros_e_mesmo_estado():
    """Testa validações de erro e movimentação para a mesma coluna."""
    tarefas, _, _ = criar_tarefa([], "Tarefa 1", "", "media", None, UUID_1, TS_1)

    # Estado inválido
    with pytest.raises(ValueError, match="Estado de destino inválido"):
        mover_tarefa(tarefas, UUID_1, "estado_inexistente")

    # Tarefa inexistente
    with pytest.raises(ValueError, match="não encontrada para movimentação"):
        mover_tarefa(tarefas, UUID_2, "concluida")

    # Mover para o mesmo estado e mesma ordem (no-op via reordenar)
    novas, ts, t = mover_tarefa(tarefas, UUID_1, "a_fazer", nova_ordem=0, timestamp_global_atual=TS_1)
    assert ts == TS_1


def test_reordenar_tarefa_regras_metadados():
    """Testa as regras de metadados da reordenação da Seção 6.2."""
    t1 = {"id": UUID_1, "titulo": "Tarefa 1", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 0}
    t2 = {"id": UUID_2, "titulo": "Tarefa 2", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 1}
    t3 = {"id": UUID_3, "titulo": "Tarefa 3", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 2}

    tarefas = [t1, t2, t3]

    # Reordenar T1 da posição 0 para a posição 2
    novas_tarefas, novo_ts, t_mov = reordenar_tarefa(
        tarefas=tarefas,
        tarefa_id=UUID_1,
        nova_ordem=2,
        timestamp_injetado=TS_2,
        timestamp_global_atual=TS_1,
    )

    mapa = {t["id"]: t for t in novas_tarefas}
    # T1 atualizou ordem para 2 e data_atualizacao para TS_2
    assert mapa[UUID_1]["ordem"] == 2
    assert mapa[UUID_1]["data_atualizacao"] == TS_2

    # T2 reindexado para 0, mantendo data_atualizacao original TS_1
    assert mapa[UUID_2]["ordem"] == 0
    assert mapa[UUID_2]["data_atualizacao"] == TS_1

    # T3 reindexado para 1, mantendo data_atualizacao original TS_1
    assert mapa[UUID_3]["ordem"] == 1
    assert mapa[UUID_3]["data_atualizacao"] == TS_1

    assert novo_ts == TS_2

    # Reordenação no-op (posição igual)
    tarefas_noop, ts_noop, t_noop = reordenar_tarefa(
        tarefas=novas_tarefas,
        tarefa_id=UUID_1,
        nova_ordem=2,
        timestamp_injetado=TS_3,
        timestamp_global_atual=TS_2,
    )
    assert ts_noop == TS_2
    assert t_noop["data_atualizacao"] == TS_2


def test_reordenar_tarefa_erros():
    """Testa erros de reordenação."""
    tarefas, _, _ = criar_tarefa([], "Tarefa 1", "", "media", None, UUID_1, TS_1)
    with pytest.raises(ValueError, match="não encontrada para reordenação"):
        reordenar_tarefa(tarefas, UUID_2, 0)


def test_excluir_tarefa_sucesso_e_reindexacao():
    """Testa exclusão de tarefa com reindexação da coluna afetada e preservação das datas."""
    t1 = {"id": UUID_1, "titulo": "Tarefa 1", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 0}
    t2 = {"id": UUID_2, "titulo": "Tarefa 2", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 1}

    tarefas = [t1, t2]
    novas_tarefas, ts, excluida = excluir_tarefa(tarefas, UUID_1, timestamp_injetado=TS_2)

    assert len(novas_tarefas) == 1
    assert excluida["id"] == UUID_1
    assert ts == TS_2
    assert novas_tarefas[0]["id"] == UUID_2
    assert novas_tarefas[0]["ordem"] == 0  # Reindexado para 0
    assert novas_tarefas[0]["data_atualizacao"] == TS_1  # Data original preservada


def test_excluir_tarefa_inexistente():
    """Testa erro ao tentar excluir tarefa inexistente."""
    with pytest.raises(ValueError, match="não encontrada para exclusão"):
        excluir_tarefa([], UUID_1)

def test_criar_tarefa_rejeita_id_duplicado():
    """A criação não pode introduzir IDs duplicados no quadro."""
    tarefas, _, _ = criar_tarefa(
        [], "Primeira tarefa", id_injetado=UUID_1, timestamp_injetado=TS_1
    )
    with pytest.raises(ValueError, match="Já existe uma tarefa com o ID"):
        criar_tarefa(
            tarefas, "Tarefa duplicada", id_injetado=UUID_1, timestamp_injetado=TS_2
        )


def test_editar_tarefa_nao_aceita_campos_imutaveis():
    """Campos de identidade e ciclo de vida não fazem parte da API de edição."""
    tarefas, _, _ = criar_tarefa(
        [], "Título original", id_injetado=UUID_1, timestamp_injetado=TS_1
    )
    with pytest.raises(TypeError, match="unexpected keyword argument"):
        editar_tarefa(
            tarefas, UUID_1, "Título novo", "", "media", None, estado="concluida"
        )


def test_transicoes_atualizam_timestamp_global_nas_seis_combinacoes():
    """Cada transição efetiva retorna o timestamp aplicado à tarefa."""
    cenarios = [
        ("a_fazer", "em_andamento"),
        ("a_fazer", "concluida"),
        ("em_andamento", "a_fazer"),
        ("em_andamento", "concluida"),
        ("concluida", "a_fazer"),
        ("concluida", "em_andamento"),
    ]
    timestamps = [
        "2026-11-02T13:00:00.000Z",
        "2026-11-02T14:00:00.000Z",
        "2026-11-02T15:00:00.000Z",
        "2026-11-02T16:00:00.000Z",
        "2026-11-02T17:00:00.000Z",
        "2026-11-02T18:00:00.000Z",
    ]
    for indice, ((origem, destino), timestamp) in enumerate(
        zip(cenarios, timestamps), start=1
    ):
        tarefa_id = f"{indice:08d}-1111-4111-8111-111111111111"
        tarefa = {
            "id": tarefa_id,
            "titulo": "Tarefa de transição",
            "descricao": "",
            "estado": origem,
            "prioridade": "media",
            "data_criacao": TS_1,
            "data_limite": None,
            "data_atualizacao": TS_2 if origem == "concluida" else TS_1,
            "data_conclusao": TS_2 if origem == "concluida" else None,
            "ordem": 0,
        }
        novas, ts_global, atualizada = mover_tarefa(
            [tarefa],
            tarefa_id,
            destino,
            timestamp_injetado=timestamp,
            timestamp_global_atual=TS_1,
        )
        assert ts_global == timestamp
        assert atualizada["data_atualizacao"] == timestamp
        assert novas[0]["data_atualizacao"] == timestamp
        assert atualizada["estado"] == destino

def test_servicos_rejeitam_enums_nao_string():
    """Serviços também devem normalizar tipos inválidos para ValueError."""
    tarefas, _, _ = criar_tarefa(
        [], "Tarefa válida", id_injetado=UUID_1, timestamp_injetado=TS_1
    )
    with pytest.raises(ValueError, match="Estado de destino inválido"):
        mover_tarefa(tarefas, UUID_1, [], timestamp_global_atual=TS_1)
    with pytest.raises(ValueError, match="Campo 'prioridade' inválido"):
        editar_tarefa(tarefas, UUID_1, "Novo título", "", [], None)

def test_excluir_tarefas_multiplas_colunas_preserva_metadados_e_entrada():
    from todolist.services import excluir_tarefas

    tarefas = [
        {"id": UUID_1, "titulo": "Tarefa 1", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 0},
        {"id": UUID_2, "titulo": "Tarefa 2", "descricao": "", "estado": "a_fazer", "prioridade": "alta", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_2, "data_conclusao": None, "ordem": 1},
        {"id": UUID_3, "titulo": "Tarefa 3", "descricao": "", "estado": "concluida", "prioridade": "baixa", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_3, "data_conclusao": TS_3, "ordem": 0},
    ]
    original = [dict(tarefa) for tarefa in tarefas]
    novas, timestamp, excluidas = excluir_tarefas(tarefas, [UUID_1, UUID_3], timestamp_injetado=TS_2)
    assert tarefas == original
    assert timestamp == TS_2
    assert [t["id"] for t in excluidas] == [UUID_1, UUID_3]
    assert [t["id"] for t in novas] == [UUID_2]
    assert novas[0]["ordem"] == 0
    assert novas[0]["data_atualizacao"] == TS_2
    assert novas[0]["prioridade"] == "alta"


@pytest.mark.parametrize("ids, mensagem", [
    ([], "ao menos uma"),
    ([UUID_1, UUID_1], "duplicados"),
    ([UUID_1, UUID_3], "não encontrada"),
])
def test_excluir_tarefas_rejeita_lista_vazia_duplicada_ou_id_inexistente(ids, mensagem):
    from todolist.services import excluir_tarefas
    tarefa = {"id": UUID_1, "titulo": "Tarefa 1", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 0}
    with pytest.raises(ValueError, match=mensagem):
        excluir_tarefas([tarefa], ids, timestamp_injetado=TS_2)


def test_excluir_tarefas_rejeita_ids_invalidos_e_nao_faz_exclusao_parcial():
    from todolist.services import excluir_tarefas
    tarefas = [
        {"id": UUID_1, "titulo": "Tarefa 1", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 0},
        {"id": UUID_2, "titulo": "Tarefa 2", "descricao": "", "estado": "a_fazer", "prioridade": "media", "data_criacao": TS_1, "data_limite": None, "data_atualizacao": TS_1, "data_conclusao": None, "ordem": 1},
    ]
    original = [dict(tarefa) for tarefa in tarefas]
    with pytest.raises(ValueError, match="não encontrada"):
        excluir_tarefas(tarefas, [UUID_1, UUID_3], timestamp_injetado=TS_2)
    assert tarefas == original
    with pytest.raises(ValueError, match="strings não vazias"):
        excluir_tarefas(tarefas, [UUID_1, None], timestamp_injetado=TS_2)

