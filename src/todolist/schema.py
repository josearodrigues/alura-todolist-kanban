"""Validação de schema JSON para importação e exportação de backups.

Implementa a política estrita de rejeição integral em caso de campos
desconhecidos ou ausentes, sem correções silenciosas (RF13, RF14, Seção 5).
"""

from typing import Any, Dict, List, Set, Tuple
from todolist.models import (
    CAMPOS_OBRIGATORIOS_TAREFA,
    Tarefa,
    validar_iso_utc_ms,
)

CAMPOS_OBRIGATORIOS_ENVELOPE: Set[str] = {
    "versao_schema",
    "aplicacao",
    "data_exportacao",
    "total_tarefas",
    "tarefas",
}
VERSAO_SCHEMA_ESPERADA = "1.0"
APLICACAO_ESPERADA = "To-Do List Kanban"


def validar_envelope_backup(dados: Dict[str, Any]) -> Tuple[bool, str]:
    """Valida o documento JSON de backup (envelope e tarefas).

    Retorna: (is_valido, mensagem_erro).
    Se for válido, mensagem_erro será "".
    """
    if not isinstance(dados, dict):
        return False, "O backup JSON deve ser um objeto JSON (dicionário)."

    chaves_envelope = set(dados.keys())

    # Rejeição de campos desconhecidos no envelope
    campos_desconhecidos = chaves_envelope - CAMPOS_OBRIGATORIOS_ENVELOPE
    if campos_desconhecidos:
        return False, f"Envelope contém campos desconhecidos: {sorted(list(campos_desconhecidos))}."

    # Verificação de campos faltantes no envelope
    campos_faltantes = CAMPOS_OBRIGATORIOS_ENVELOPE - chaves_envelope
    if campos_faltantes:
        return False, f"Envelope possui campos obrigatórios ausentes: {sorted(list(campos_faltantes))}."

    # Validação de valores do envelope
    if dados["versao_schema"] != VERSAO_SCHEMA_ESPERADA:
        return False, f"versao_schema inválida: '{dados['versao_schema']}'. Esperado: '{VERSAO_SCHEMA_ESPERADA}'."

    if dados["aplicacao"] != APLICACAO_ESPERADA:
        return False, f"aplicacao inválida: '{dados['aplicacao']}'. Esperado: '{APLICACAO_ESPERADA}'."

    try:
        validar_iso_utc_ms(dados["data_exportacao"], "data_exportacao")
    except ValueError as e:
        return False, f"data_exportacao inválida no envelope: {e}"

    tarefas = dados["tarefas"]
    if not isinstance(tarefas, list):
        return False, "Campo 'tarefas' deve ser uma lista."

    if not isinstance(dados["total_tarefas"], int) or isinstance(dados["total_tarefas"], bool):
        return False, "Campo 'total_tarefas' deve ser um inteiro."

    if dados["total_tarefas"] != len(tarefas):
        return (
            False,
            f"Divergência de contagem: total_tarefas ({dados['total_tarefas']}) != len(tarefas) ({len(tarefas)}).",
        )

    # Validar individualmente cada tarefa e garantir unicidade de id
    ids_vistos: Set[str] = set()
    ordens_por_coluna: Dict[str, List[int]] = {"a_fazer": [], "em_andamento": [], "concluida": []}

    for idx, t in enumerate(tarefas):
        if not isinstance(t, dict):
            return False, f"Item {idx} da lista de tarefas não é um objeto JSON."

        # Validação estrita via Tarefa.from_dict
        try:
            obj_tarefa = Tarefa.from_dict(t)
        except (ValueError, TypeError) as e:
            return False, f"Erro na tarefa de índice {idx}: {e}"

        if obj_tarefa.id in ids_vistos:
            return False, f"ID duplicado detectado: '{obj_tarefa.id}' na tarefa de índice {idx}."
        ids_vistos.add(obj_tarefa.id)

        ordens_por_coluna[obj_tarefa.estado].append(obj_tarefa.ordem)

    # Validar contiguidade de ordem por coluna iniciando em zero: 0, 1, 2...
    for estado, ordens in ordens_por_coluna.items():
        ordens_ordenadas = sorted(ordens)
        ordens_esperadas = list(range(len(ordens)))
        if ordens_ordenadas != ordens_esperadas:
            return (
                False,
                f"Coluna '{estado}' possui sequência de ordem inválida: recebido {ordens_ordenadas}, esperado {ordens_esperadas}.",
            )

    return True, ""


def gerar_envelope_backup(
    tarefas: List[Dict[str, Any]],
    timestamp_exportacao: str,
) -> Dict[str, Any]:
    """Gera o envelope JSON oficial de exportação (RF13)."""
    validar_iso_utc_ms(timestamp_exportacao, "timestamp_exportacao")

    # Valida todas as tarefas antes de empacotar
    for t in tarefas:
        Tarefa.from_dict(t)

    return {
        "versao_schema": VERSAO_SCHEMA_ESPERADA,
        "aplicacao": APLICACAO_ESPERADA,
        "data_exportacao": timestamp_exportacao,
        "total_tarefas": len(tarefas),
        "tarefas": [dict(t) for t in tarefas],
    }


def preparar_importacao_backup(
    conteudo_json: str,
    timestamp_importacao: str = None,
) -> Dict[str, Any]:
    """Lê, valida estritamente e prepara o estado de uma importação (RF14).

    Chaves JSON duplicadas e constantes não padronizadas (NaN/Infinity) são
    rejeitadas. Nenhum estado da aplicação é alterado por esta função.
    """
    import json

    if not isinstance(conteudo_json, str):
        raise ValueError("O conteúdo do backup deve ser texto.")

    def rejeitar_chaves_duplicadas(pares):
        objeto = {}
        for chave, valor in pares:
            if chave in objeto:
                raise ValueError(f"O JSON contém chave duplicada: '{chave}'.")
            objeto[chave] = valor
        return objeto

    def rejeitar_constante(valor):
        raise ValueError(f"Constante não permitida no JSON: {valor}.")

    try:
        envelope = json.loads(
            conteudo_json,
            object_pairs_hook=rejeitar_chaves_duplicadas,
            parse_constant=rejeitar_constante,
        )
    except (json.JSONDecodeError, TypeError, ValueError) as erro:
        raise ValueError(f"Arquivo JSON inválido: {erro}") from erro

    valido, mensagem = validar_envelope_backup(envelope)
    if not valido:
        raise ValueError(mensagem)

    if timestamp_importacao is not None:
        validar_iso_utc_ms(timestamp_importacao, "timestamp_importacao")
    return {
        "tarefas": [dict(tarefa) for tarefa in envelope["tarefas"]],
        "timestamp_ultima_alteracao": timestamp_importacao,
    }


def preparar_estado_importado(
    tarefas: List[Dict[str, Any]],
    timestamp_importacao: str,
) -> Dict[str, Any]:
    """Valida tarefas já aprovadas e gera o estado candidato no momento da confirmação."""
    validar_iso_utc_ms(timestamp_importacao, "timestamp_importacao")
    envelope = gerar_envelope_backup(tarefas, timestamp_importacao)
    valido, mensagem = validar_envelope_backup(envelope)
    if not valido:
        raise ValueError(mensagem)
    return {
        "tarefas": envelope["tarefas"],
        "timestamp_ultima_alteracao": timestamp_importacao,
    }
