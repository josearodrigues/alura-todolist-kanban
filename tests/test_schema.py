"""Testes unitários para validação de schema JSON em schema.py."""

import pytest
from todolist.schema import (
    APLICACAO_ESPERADA,
    VERSAO_SCHEMA_ESPERADA,
    gerar_envelope_backup,
    validar_envelope_backup,
)

UUID_1 = "11111111-1111-4111-8111-111111111111"
UUID_2 = "22222222-2222-4222-8222-222222222222"
TS_EXPORT = "2026-11-02T12:00:00.000Z"


def criar_tarefa_valida(tid: str, estado: str, ordem: int) -> dict:
    return {
        "id": tid,
        "titulo": f"Tarefa {ordem}",
        "descricao": "",
        "estado": estado,
        "prioridade": "media",
        "data_criacao": TS_EXPORT,
        "data_limite": None,
        "data_atualizacao": TS_EXPORT,
        "data_conclusao": TS_EXPORT if estado == "concluida" else None,
        "ordem": ordem,
    }


def test_gerar_envelope_backup_valido():
    """Testa geração de envelope de backup estruturado (RF13)."""
    t1 = criar_tarefa_valida(UUID_1, "a_fazer", 0)
    envelope = gerar_envelope_backup([t1], TS_EXPORT)

    assert envelope["versao_schema"] == "1.0"
    assert envelope["aplicacao"] == "To-Do List Kanban"
    assert envelope["data_exportacao"] == TS_EXPORT
    assert envelope["total_tarefas"] == 1
    assert len(envelope["tarefas"]) == 1

    valido, msg = validar_envelope_backup(envelope)
    assert valido is True
    assert msg == ""


def test_validar_envelope_rejeita_tipo_invalido():
    """Rejeita quando raiz não é dicionário."""
    valido, msg = validar_envelope_backup(["não dicionário"])
    assert valido is False
    assert "deve ser um objeto JSON" in msg


def test_validar_envelope_rejeita_campos_desconhecidos_envelope():
    """Política de rejeição estrita: campos desconhecidos no envelope (RF14)."""
    envelope = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 0,
        "tarefas": [],
        "campo_extra": "invalido",
    }
    valido, msg = validar_envelope_backup(envelope)
    assert valido is False
    assert "Envelope contém campos desconhecidos" in msg


def test_validar_envelope_rejeita_campos_faltantes_envelope():
    """Rejeita envelope incompleto."""
    envelope = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "tarefas": [],
    }
    valido, msg = validar_envelope_backup(envelope)
    assert valido is False
    assert "Envelope possui campos obrigatórios ausentes" in msg


def test_validar_envelope_rejeita_versao_ou_aplicacao_invalidas():
    """Valida correspondência exata de versão e aplicação."""
    env1 = {
        "versao_schema": "2.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 0,
        "tarefas": [],
    }
    valido, msg = validar_envelope_backup(env1)
    assert valido is False
    assert "versao_schema inválida" in msg

    env2 = {
        "versao_schema": "1.0",
        "aplicacao": "Outra Aplicacao",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 0,
        "tarefas": [],
    }
    valido, msg = validar_envelope_backup(env2)
    assert valido is False
    assert "aplicacao inválida" in msg


def test_validar_envelope_rejeita_data_exportacao_invalida():
    """Valida data_exportacao ISO 8601 UTC."""
    env = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": "data-invalida",
        "total_tarefas": 0,
        "tarefas": [],
    }
    valido, msg = validar_envelope_backup(env)
    assert valido is False
    assert "data_exportacao inválida" in msg


def test_validar_envelope_rejeita_divergencia_contagem_ou_tipo_tarefas():
    """Valida coerência de total_tarefas e tipo do campo tarefas."""
    env1 = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": "0",  # String em vez de int
        "tarefas": [],
    }
    valido, msg = validar_envelope_backup(env1)
    assert valido is False
    assert "total_tarefas" in msg

    env2 = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 1,
        "tarefas": [],  # len 0 != 1
    }
    valido, msg = validar_envelope_backup(env2)
    assert valido is False
    assert "Divergência de contagem" in msg

    env3 = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 0,
        "tarefas": "não é lista",
    }
    valido, msg = validar_envelope_backup(env3)
    assert valido is False
    assert "deve ser uma lista" in msg


def test_validar_envelope_rejeita_tarefa_invalida_ou_com_campos_desconhecidos():
    """Valida rejeição de tarefas inválidas ou com atributos desconhecidos."""
    t_invalida = criar_tarefa_valida(UUID_1, "a_fazer", 0)
    t_invalida["campo_estranho"] = 123

    env = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 1,
        "tarefas": [t_invalida],
    }
    valido, msg = validar_envelope_backup(env)
    assert valido is False
    assert "Erro na tarefa de índice 0" in msg

    # Item não-objeto
    env_nao_dict = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 1,
        "tarefas": ["não é objeto"],
    }
    valido, msg = validar_envelope_backup(env_nao_dict)
    assert valido is False
    assert "não é um objeto JSON" in msg


def test_validar_envelope_rejeita_id_duplicado():
    """Valida unicidade de ID entre as tarefas."""
    t1 = criar_tarefa_valida(UUID_1, "a_fazer", 0)
    t2 = criar_tarefa_valida(UUID_1, "a_fazer", 1)  # Mesmo ID

    env = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 2,
        "tarefas": [t1, t2],
    }
    valido, msg = validar_envelope_backup(env)
    assert valido is False
    assert "ID duplicado detectado" in msg


def test_validar_envelope_rejeita_ordem_nao_contigua_por_coluna():
    """Valida rejeição de sequências ordinais com lacunas (sem normalização silenciosa)."""
    t1 = criar_tarefa_valida(UUID_1, "a_fazer", 0)
    t2 = criar_tarefa_valida(UUID_2, "a_fazer", 2)  # Lacuna: falta ordem 1

    env = {
        "versao_schema": "1.0",
        "aplicacao": "To-Do List Kanban",
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 2,
        "tarefas": [t1, t2],
    }
    valido, msg = validar_envelope_backup(env)
    assert valido is False
    assert "sequência de ordem inválida" in msg

def test_validar_envelope_rejeita_enum_nao_hashable_sem_excecao():
    """Enum com tipo incompatível é rejeitado pelo validador do backup."""
    tarefa = criar_tarefa_valida(UUID_1, "a_fazer", 0)
    tarefa["estado"] = []
    envelope = {
        "versao_schema": VERSAO_SCHEMA_ESPERADA,
        "aplicacao": APLICACAO_ESPERADA,
        "data_exportacao": TS_EXPORT,
        "total_tarefas": 1,
        "tarefas": [tarefa],
    }
    valido, mensagem = validar_envelope_backup(envelope)
    assert valido is False
    assert "Erro na tarefa de índice 0" in mensagem
    assert "Campo 'estado' inválido" in mensagem
