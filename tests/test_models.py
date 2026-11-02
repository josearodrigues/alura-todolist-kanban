"""Testes unitários para o modelo Tarefa e funções de validação em models.py."""

import pytest
from todolist.models import (
    Tarefa,
    validar_data_limite,
    validar_iso_utc_ms,
    validar_uuid_v4,
)

UUID_VALIDO = "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
TS_CRIACAO = "2026-11-02T10:00:00.000Z"
TS_ATUALIZACAO = "2026-11-02T12:00:00.000Z"
TS_CONCLUSAO = "2026-11-02T12:00:00.000Z"


def test_tarefa_criacao_valida_a_fazer():
    """Valida instanciação bem-sucedida de tarefa em estado 'a_fazer'."""
    t = Tarefa(
        id=UUID_VALIDO,
        titulo="  Implementar testes  ",
        descricao="  Descrição detalhada  ",
        estado="a_fazer",
        prioridade="alta",
        data_criacao=TS_CRIACAO,
        data_limite="2026-11-10",
        data_atualizacao=TS_CRIACAO,
        data_conclusao=None,
        ordem=0,
    )
    assert t.titulo == "Implementar testes"
    assert t.descricao == "Descrição detalhada"
    assert t.estado == "a_fazer"
    assert t.prioridade == "alta"
    assert t.ordem == 0
    assert t.data_conclusao is None


def test_tarefa_criacao_valida_concluida():
    """Valida instanciação bem-sucedida de tarefa concluída respeitando invariantes."""
    t = Tarefa(
        id=UUID_VALIDO,
        titulo="Tarefa Concluída",
        descricao="",
        estado="concluida",
        prioridade="media",
        data_criacao=TS_CRIACAO,
        data_limite=None,
        data_atualizacao=TS_ATUALIZACAO,
        data_conclusao=TS_CONCLUSAO,
        ordem=1,
    )
    assert t.estado == "concluida"
    assert t.data_conclusao == TS_CONCLUSAO


def test_tarefa_to_dict_e_from_dict():
    """Valida conversão bidirecional to_dict e from_dict com integridade estrita."""
    dados_originais = {
        "id": UUID_VALIDO,
        "titulo": "Tarefa de Teste",
        "descricao": "Texto descritivo",
        "estado": "em_andamento",
        "prioridade": "baixa",
        "data_criacao": TS_CRIACAO,
        "data_limite": "2026-12-01",
        "data_atualizacao": TS_ATUALIZACAO,
        "data_conclusao": None,
        "ordem": 2,
    }
    t = Tarefa.from_dict(dados_originais)
    assert t.to_dict() == dados_originais


def test_tarefa_from_dict_rejeita_tipo_invalido():
    """Rejeita entrada que não seja dicionário."""
    with pytest.raises(ValueError, match="Dados para reconstituição de Tarefa devem ser um dicionário"):
        Tarefa.from_dict("não é dicionário")


def test_tarefa_from_dict_rejeita_campo_desconhecido():
    """Rejeita dicionário com campos extras não permitidos (ex: responsavel)."""
    dados = {
        "id": UUID_VALIDO,
        "titulo": "Tarefa com campo extra",
        "descricao": "",
        "estado": "a_fazer",
        "prioridade": "baixa",
        "data_criacao": TS_CRIACAO,
        "data_limite": None,
        "data_atualizacao": TS_CRIACAO,
        "data_conclusao": None,
        "ordem": 0,
        "responsavel": "João",
    }
    with pytest.raises(ValueError, match="Campos desconhecidos detectados"):
        Tarefa.from_dict(dados)


def test_tarefa_from_dict_rejeita_campo_faltante():
    """Rejeita dicionário sem atributos obrigatórios."""
    dados = {
        "id": UUID_VALIDO,
        "titulo": "Tarefa incompleta",
        "estado": "a_fazer",
    }
    with pytest.raises(ValueError, match="Campos obrigatórios ausentes"):
        Tarefa.from_dict(dados)


def test_validar_uuid_v4():
    """Testa validações de UUID v4."""
    validar_uuid_v4(UUID_VALIDO)

    with pytest.raises(ValueError, match="ID inválido"):
        validar_uuid_v4("não-uuid")

    with pytest.raises(ValueError, match="ID inválido"):
        validar_uuid_v4(12345)

    # UUID v1 (versão diferente de 4)
    with pytest.raises(ValueError, match="ID inválido"):
        validar_uuid_v4("a0eebc99-9c0b-1ef8-bb6d-6bb9bd380a11")


def test_validar_iso_utc_ms():
    """Testa validação de timestamp ISO 8601 UTC com milissegundos."""
    dt = validar_iso_utc_ms(TS_CRIACAO, "campo_teste")
    assert dt.year == 2026

    # Sem 'Z'
    with pytest.raises(ValueError, match="formato ISO 8601 UTC"):
        validar_iso_utc_ms("2026-11-02T10:00:00.000", "campo_teste")

    # Sem milissegundos
    with pytest.raises(ValueError, match="formato ISO 8601 UTC"):
        validar_iso_utc_ms("2026-11-02T10:00:00Z", "campo_teste")

    # Tipo inválido
    with pytest.raises(ValueError, match="formato ISO 8601 UTC"):
        validar_iso_utc_ms(12345, "campo_teste")

    # Data inexistente no calendário (ex: 30 de fevereiro)
    with pytest.raises(ValueError, match="data/hora inexistente"):
        validar_iso_utc_ms("2026-02-30T10:00:00.000Z", "campo_teste")


def test_validar_data_limite():
    """Testa validação de data_limite no formato YYYY-MM-DD ou None."""
    validar_data_limite(None)
    validar_data_limite("2026-11-05")

    with pytest.raises(ValueError, match="formato YYYY-MM-DD"):
        validar_data_limite("05/11/2026")

    with pytest.raises(ValueError, match="formato YYYY-MM-DD"):
        validar_data_limite(12345)

    # Data inexistente (ex: 31 de abril)
    with pytest.raises(ValueError, match="data inexistente"):
        validar_data_limite("2026-04-31")


def test_tarefa_validacoes_titulo():
    """Testa limites de tamanho e tipo do título."""
    # Menos de 3 caracteres após strip
    with pytest.raises(ValueError, match="entre 3 e 100 caracteres"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="  ab  ",
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=0,
        )

    # Mais de 100 caracteres
    with pytest.raises(ValueError, match="entre 3 e 100 caracteres"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="A" * 101,
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=0,
        )

    # Tipo não-string
    with pytest.raises(ValueError, match="deve ser uma string"):
        Tarefa(
            id=UUID_VALIDO,
            titulo=12345,
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=0,
        )


def test_tarefa_validacoes_descricao():
    """Testa limites de tamanho e tipo da descrição."""
    with pytest.raises(ValueError, match="no máximo 500 caracteres"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="D" * 501,
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=0,
        )

    with pytest.raises(ValueError, match="deve ser uma string"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao=None,
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=0,
        )


def test_tarefa_validacoes_estado_e_prioridade():
    """Testa enums de estado e prioridade."""
    with pytest.raises(ValueError, match="Campo 'estado' inválido"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="invalido",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=0,
        )

    with pytest.raises(ValueError, match="Campo 'prioridade' inválido"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="a_fazer",
            prioridade="urgente",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=0,
        )


def test_tarefa_invariantes_temporais():
    """Testa as 8 invariantes temporais obrigatórias."""
    # Invariante 1: data_atualizacao < data_criacao
    with pytest.raises(ValueError, match="data_atualizacao.*anterior a data_criacao"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao="2026-11-02T12:00:00.000Z",
            data_limite=None,
            data_atualizacao="2026-11-02T10:00:00.000Z",
            data_conclusao=None,
            ordem=0,
        )

    # Invariante 2: concluida sem data_conclusao
    with pytest.raises(ValueError, match="exige data_conclusao não nula"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="concluida",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_ATUALIZACAO,
            data_conclusao=None,
            ordem=0,
        )

    # Invariante 3: data_conclusao < data_criacao
    with pytest.raises(ValueError, match="data_conclusao.*anterior a data_criacao"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="concluida",
            prioridade="media",
            data_criacao="2026-11-02T12:00:00.000Z",
            data_limite=None,
            data_atualizacao="2026-11-02T12:00:00.000Z",
            data_conclusao="2026-11-02T10:00:00.000Z",
            ordem=0,
        )

    # Invariante 4: data_conclusao > data_atualizacao
    with pytest.raises(ValueError, match="data_conclusao.*posterior a data_atualizacao"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="concluida",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao="2026-11-02T11:00:00.000Z",
            data_conclusao="2026-11-02T12:00:00.000Z",
            ordem=0,
        )

    # Invariante 5: estado != concluida com data_conclusao não nula
    with pytest.raises(ValueError, match="deve ter data_conclusao nula"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=TS_CONCLUSAO,
            ordem=0,
        )


def test_tarefa_validacoes_ordem():
    """Testa validações do campo ordem."""
    with pytest.raises(ValueError, match="deve ser um inteiro maior ou igual a zero"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=-1,
        )

    with pytest.raises(ValueError, match="deve ser um inteiro maior ou igual a zero"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem=True,  # Em python bool é subclasse de int
        )

    with pytest.raises(ValueError, match="deve ser um inteiro maior ou igual a zero"):
        Tarefa(
            id=UUID_VALIDO,
            titulo="Título Válido",
            descricao="",
            estado="a_fazer",
            prioridade="media",
            data_criacao=TS_CRIACAO,
            data_limite=None,
            data_atualizacao=TS_CRIACAO,
            data_conclusao=None,
            ordem="0",
        )

def test_tarefa_rejeita_estado_e_prioridade_nao_hashable():
    """Entradas não hashable devem produzir ValueError, nunca TypeError."""
    dados_base = {
        "id": UUID_VALIDO, "titulo": "Título válido", "descricao": "",
        "estado": "a_fazer", "prioridade": "media",
        "data_criacao": TS_CRIACAO, "data_limite": None,
        "data_atualizacao": TS_CRIACAO, "data_conclusao": None, "ordem": 0,
    }
    for campo in ("estado", "prioridade"):
        dados = dict(dados_base)
        dados[campo] = []
        with pytest.raises(ValueError, match=f"Campo '{campo}' inválido"):
            Tarefa.from_dict(dados)
