"""Domínio da aplicação To-Do List Kanban.

Modelo de dados da entidade Tarefa e enums de validação.
"""

from dataclasses import asdict, dataclass
from datetime import datetime
import re
from typing import Any, Dict, Optional, Set
import uuid

# Constantes e Enums
ESTADOS_VALIDOS: Set[str] = {"a_fazer", "em_andamento", "concluida"}
PRIORIDADES_VALIDAS: Set[str] = {"baixa", "media", "alta"}
CAMPOS_OBRIGATORIOS_TAREFA: Set[str] = {
    "id",
    "titulo",
    "descricao",
    "estado",
    "prioridade",
    "data_criacao",
    "data_limite",
    "data_atualizacao",
    "data_conclusao",
    "ordem",
}

# Regex para validação de formatos
REGEX_UUID_V4 = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
REGEX_ISO_UTC_MS = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$"
)
REGEX_DATA_LIMITE = re.compile(
    r"^\d{4}-\d{2}-\d{2}$"
)


def validar_uuid_v4(valor: str) -> None:
    """Valida se a string é um UUID v4 canônico válido."""
    if not isinstance(valor, str) or not REGEX_UUID_V4.match(valor):
        raise ValueError(f"ID inválido: '{valor}' não é um UUID v4 canônico.")


def validar_iso_utc_ms(valor: str, campo: str) -> datetime:
    """Valida se a string está no formato estrito ISO 8601 UTC com milissegundos."""
    if not isinstance(valor, str) or not REGEX_ISO_UTC_MS.match(valor):
        raise ValueError(
            f"Campo '{campo}' inválido: '{valor}' deve estar no formato ISO 8601 UTC (YYYY-MM-DDTHH:MM:SS.sssZ)."
        )
    # Validar se a data/hora é matematicamente válida no calendário
    try:
        # Troca 'Z' por '+00:00' para parsing
        dt = datetime.fromisoformat(valor.replace("Z", "+00:00"))
        return dt
    except ValueError as e:
        raise ValueError(f"Campo '{campo}' possui data/hora inexistente no calendário: {e}")


def validar_data_limite(valor: Optional[str]) -> None:
    """Valida se data_limite é null ou string no formato estrito YYYY-MM-DD."""
    if valor is None:
        return
    if not isinstance(valor, str) or not REGEX_DATA_LIMITE.match(valor):
        raise ValueError(
            f"Campo 'data_limite' inválido: '{valor}' deve ser null ou formato YYYY-MM-DD."
        )
    try:
        datetime.strptime(valor, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Campo 'data_limite' possui data inexistente no calendário: {e}")


@dataclass
class Tarefa:
    """Entidade central representando uma tarefa no quadro Kanban."""

    id: str
    titulo: str
    descricao: str
    estado: str
    prioridade: str
    data_criacao: str
    data_limite: Optional[str]
    data_atualizacao: str
    data_conclusao: Optional[str]
    ordem: int

    def __post_init__(self) -> None:
        """Aplica validações rigorosas e defensivas nos atributos da Tarefa."""
        # 1. id: UUID v4 obrigatório
        validar_uuid_v4(self.id)

        # 2. titulo: 3 a 100 caracteres após strip/trim
        if not isinstance(self.titulo, str):
            raise ValueError("Campo 'titulo' deve ser uma string.")
        titulo_limpo = self.titulo.strip()
        if len(titulo_limpo) < 3 or len(titulo_limpo) > 100:
            raise ValueError(
                f"Campo 'titulo' deve ter entre 3 e 100 caracteres (após strip). Tamanho atual: {len(titulo_limpo)}."
            )
        self.titulo = titulo_limpo

        # 3. descricao: até 500 caracteres após strip/trim (padrão "")
        if not isinstance(self.descricao, str):
            raise ValueError("Campo 'descricao' deve ser uma string.")
        descricao_limpa = self.descricao.strip()
        if len(descricao_limpa) > 500:
            raise ValueError(
                f"Campo 'descricao' deve ter no máximo 500 caracteres (após strip). Tamanho atual: {len(descricao_limpa)}."
            )
        self.descricao = descricao_limpa

        # 4. estado: ["a_fazer", "em_andamento", "concluida"]
        if self.estado not in ESTADOS_VALIDOS:
            raise ValueError(
                f"Campo 'estado' inválido: '{self.estado}'. Valores permitidos: {sorted(list(ESTADOS_VALIDOS))}."
            )

        # 5. prioridade: ["baixa", "media", "alta"]
        if self.prioridade not in PRIORIDADES_VALIDAS:
            raise ValueError(
                f"Campo 'prioridade' inválido: '{self.prioridade}'. Valores permitidos: {sorted(list(PRIORIDADES_VALIDAS))}."
            )

        # 6. data_criacao: ISO 8601 UTC
        dt_criacao = validar_iso_utc_ms(self.data_criacao, "data_criacao")

        # 7. data_limite: YYYY-MM-DD ou null
        validar_data_limite(self.data_limite)

        # 8. data_atualizacao: ISO 8601 UTC
        dt_atualizacao = validar_iso_utc_ms(self.data_atualizacao, "data_atualizacao")

        # Invariante 1: data_atualizacao >= data_criacao
        if dt_atualizacao < dt_criacao:
            raise ValueError(
                f"Invariante temporal violada: data_atualizacao ({self.data_atualizacao}) anterior a data_criacao ({self.data_criacao})."
            )

        # 9. data_conclusao e invariantes de estado
        if self.estado == "concluida":
            if self.data_conclusao is None:
                raise ValueError("Invariante violada: tarefa com estado 'concluida' exige data_conclusao não nula.")
            dt_conclusao = validar_iso_utc_ms(self.data_conclusao, "data_conclusao")
            # Invariante 3: data_conclusao >= data_criacao
            if dt_conclusao < dt_criacao:
                raise ValueError(
                    f"Invariante temporal violada: data_conclusao ({self.data_conclusao}) anterior a data_criacao ({self.data_criacao})."
                )
            # Invariante 4: data_conclusao <= data_atualizacao
            if dt_conclusao > dt_atualizacao:
                raise ValueError(
                    f"Invariante temporal violada: data_conclusao ({self.data_conclusao}) posterior a data_atualizacao ({self.data_atualizacao})."
                )
        else:
            # Invariante 5: Quando estado != "concluida", data_conclusao == null
            if self.data_conclusao is not None:
                raise ValueError(
                    f"Invariante violada: tarefa com estado '{self.estado}' deve ter data_conclusao nula (valor recebido: '{self.data_conclusao}')."
                )

        # 10. ordem: inteiro não negativo
        if not isinstance(self.ordem, int) or isinstance(self.ordem, bool) or self.ordem < 0:
            raise ValueError(f"Campo 'ordem' deve ser um inteiro maior ou igual a zero. Valor recebido: {self.ordem}.")

    def to_dict(self) -> Dict[str, Any]:
        """Converte a entidade Tarefa para dicionário serializável."""
        return asdict(self)

    @classmethod
    def from_dict(cls, dados: Dict[str, Any]) -> "Tarefa":
        """Reconstitui uma entidade Tarefa a partir de um dicionário.

        Rejeita atributos desconhecidos ou faltantes.
        """
        if not isinstance(dados, dict):
            raise ValueError("Dados para reconstituição de Tarefa devem ser um dicionário.")

        chaves_fornecidas = set(dados.keys())
        campos_desconhecidos = chaves_fornecidas - CAMPOS_OBRIGATORIOS_TAREFA
        if campos_desconhecidos:
            raise ValueError(
                f"Campos desconhecidos detectados no objeto Tarefa: {sorted(list(campos_desconhecidos))}."
            )

        campos_faltantes = CAMPOS_OBRIGATORIOS_TAREFA - chaves_fornecidas
        if campos_faltantes:
            raise ValueError(
                f"Campos obrigatórios ausentes no objeto Tarefa: {sorted(list(campos_faltantes))}."
            )

        return cls(
            id=dados["id"],
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            estado=dados["estado"],
            prioridade=dados["prioridade"],
            data_criacao=dados["data_criacao"],
            data_limite=dados["data_limite"],
            data_atualizacao=dados["data_atualizacao"],
            data_conclusao=dados["data_conclusao"],
            ordem=dados["ordem"],
        )
