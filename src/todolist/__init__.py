"""Pacote todolist - Núcleo de domínio e regras de negócio do To-Do List Kanban.

Exportações públicas dos modelos, serviços, métricas e schemas.
"""

from todolist.models import (
    CAMPOS_OBRIGATORIOS_TAREFA,
    ESTADOS_VALIDOS,
    PRIORIDADES_VALIDAS,
    Tarefa,
    validar_data_limite,
    validar_iso_utc_ms,
    validar_uuid_v4,
)
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
from todolist.metrics import (
    calcular_foco_hoje,
    calcular_relatorio_completo,
    calcular_resumo_projeto,
)
from todolist.schema import (
    APLICACAO_ESPERADA,
    CAMPOS_OBRIGATORIOS_ENVELOPE,
    VERSAO_SCHEMA_ESPERADA,
    gerar_envelope_backup,
    validar_envelope_backup,
    preparar_importacao_backup,
    preparar_estado_importado,
)

__all__ = [
    "Tarefa",
    "ESTADOS_VALIDOS",
    "PRIORIDADES_VALIDAS",
    "CAMPOS_OBRIGATORIOS_TAREFA",
    "validar_uuid_v4",
    "validar_iso_utc_ms",
    "validar_data_limite",
    "criar_tarefa",
    "editar_tarefa",
    "mover_tarefa",
    "reordenar_tarefa",
    "excluir_tarefa",
    "obter_timestamp_utc_atual",
    "obter_novo_id",
    "reindexar_coluna",
    "calcular_resumo_projeto",
    "calcular_foco_hoje",
    "calcular_relatorio_completo",
    "validar_envelope_backup",
    "gerar_envelope_backup",
    "preparar_importacao_backup",
    "preparar_estado_importado",
    "VERSAO_SCHEMA_ESPERADA",
    "APLICACAO_ESPERADA",
    "CAMPOS_OBRIGATORIOS_ENVELOPE",
]
