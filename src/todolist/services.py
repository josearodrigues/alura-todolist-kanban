"""Serviços de negócio e manipulação de estado do Kanban.

Implementação funcional sem efeitos colaterais e com injeção de dependências
(id e timestamp_utc) para total determinismo.
"""

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
import uuid

from todolist.models import (
    ESTADOS_VALIDOS,
    PRIORIDADES_VALIDAS,
    Tarefa,
    validar_data_limite,
)


def obter_timestamp_utc_atual() -> str:
    """Gera o timestamp ISO 8601 UTC no formato canônico YYYY-MM-DDTHH:MM:SS.sssZ."""
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def obter_novo_id() -> str:
    """Gera um UUID v4 canônico em minúsculas com hífens."""
    return str(uuid.uuid4())


def criar_tarefa(
    tarefas: List[Dict[str, Any]],
    titulo: str,
    descricao: str = "",
    prioridade: str = "media",
    data_limite: Optional[str] = None,
    id_injetado: Optional[str] = None,
    timestamp_injetado: Optional[str] = None,
) -> Tuple[List[Dict[str, Any]], str, Dict[str, Any]]:
    """Cria uma nova tarefa no estado obrigatório 'a_fazer'.

    Calcula a ordem contígua como len(tarefas_a_fazer).
    Retorna: (novas_tarefas, novo_timestamp_global, tarefa_criada_dict).
    """
    ts = timestamp_injetado if timestamp_injetado is not None else obter_timestamp_utc_atual()
    tid = id_injetado if id_injetado is not None else obter_novo_id()
    if any(t.get("id") == tid for t in tarefas):
        raise ValueError(f"Já existe uma tarefa com o ID '{tid}'.")

    # Calcular a próxima ordem da coluna 'a_fazer'
    tarefas_a_fazer = [t for t in tarefas if t.get("estado") == "a_fazer"]
    proxima_ordem = len(tarefas_a_fazer)

    nova_tarefa = Tarefa(
        id=tid,
        titulo=titulo,
        descricao=descricao,
        estado="a_fazer",
        prioridade=prioridade,
        data_criacao=ts,
        data_limite=data_limite,
        data_atualizacao=ts,
        data_conclusao=None,
        ordem=proxima_ordem,
    )

    novas_tarefas = [dict(t) for t in tarefas] + [nova_tarefa.to_dict()]
    return novas_tarefas, ts, nova_tarefa.to_dict()


def editar_tarefa(
    tarefas: List[Dict[str, Any]],
    tarefa_id: str,
    titulo: str,
    descricao: str,
    prioridade: str,
    data_limite: Optional[str],
    timestamp_injetado: Optional[str] = None,
    timestamp_global_atual: Optional[str] = None,
) -> Tuple[List[Dict[str, Any]], Optional[str], Dict[str, Any]]:
    """Edita os campos mutáveis de uma tarefa existente (RF03).

    Campos editáveis: titulo, descricao, prioridade, data_limite.
    Campos imutáveis preservados: id, data_criacao, estado, ordem, data_conclusao.

    Se houver alteração real de conteúdo:
      - Atualiza data_atualizacao da tarefa para o timestamp gerado.
      - Retorna novo timestamp_global.
    Se for operação sem alteração (no-op):
      - Preserva data_atualizacao da tarefa intacta.
      - Retorna timestamp_global_atual inalterado (sem novo timestamp).
    """
    tarefa_alvo = None
    indice_alvo = -1
    for i, t in enumerate(tarefas):
        if t.get("id") == tarefa_id:
            tarefa_alvo = Tarefa.from_dict(t)
            indice_alvo = i
            break

    if tarefa_alvo is None:
        raise ValueError(f"Tarefa com ID '{tarefa_id}' não encontrada para edição.")

    titulo_limpo = titulo.strip() if isinstance(titulo, str) else ""
    descricao_limpa = descricao.strip() if isinstance(descricao, str) else ""

    # Validar campos antes de verificar alteração
    if len(titulo_limpo) < 3 or len(titulo_limpo) > 100:
        raise ValueError(
            f"Campo 'titulo' deve ter entre 3 e 100 caracteres (após strip). Tamanho: {len(titulo_limpo)}."
        )
    if len(descricao_limpa) > 500:
        raise ValueError(
            f"Campo 'descricao' deve ter no máximo 500 caracteres (após strip). Tamanho: {len(descricao_limpa)}."
        )
    if not isinstance(prioridade, str) or prioridade not in PRIORIDADES_VALIDAS:
        raise ValueError(
            f"Campo 'prioridade' inválido: '{prioridade}'. Valores: {sorted(list(PRIORIDADES_VALIDAS))}."
        )
    validar_data_limite(data_limite)

    # Detectar se houve alteração real de conteúdo
    houve_alteracao = (
        tarefa_alvo.titulo != titulo_limpo
        or tarefa_alvo.descricao != descricao_limpa
        or tarefa_alvo.prioridade != prioridade
        or tarefa_alvo.data_limite != data_limite
    )

    if not houve_alteracao:
        # No-op: retorna estado idêntico e o timestamp_global_atual recebido
        return [dict(t) for t in tarefas], timestamp_global_atual, tarefa_alvo.to_dict()

    # Houve alteração: gera novo timestamp
    ts = timestamp_injetado if timestamp_injetado is not None else obter_timestamp_utc_atual()

    # Cria Tarefa editada preservando imutáveis
    tarefa_editada = Tarefa(
        id=tarefa_alvo.id,
        titulo=titulo_limpo,
        descricao=descricao_limpa,
        estado=tarefa_alvo.estado,
        prioridade=prioridade,
        data_criacao=tarefa_alvo.data_criacao,
        data_limite=data_limite,
        data_atualizacao=ts,
        data_conclusao=tarefa_alvo.data_conclusao,
        ordem=tarefa_alvo.ordem,
    )

    novas_tarefas = [dict(t) for t in tarefas]
    novas_tarefas[indice_alvo] = tarefa_editada.to_dict()

    return novas_tarefas, ts, tarefa_editada.to_dict()


def reindexar_coluna(tarefas_coluna: List[Tarefa]) -> List[Tarefa]:
    """Reindexa uma lista de tarefas da mesma coluna para ordens contíguas 0, 1, 2...

    Preserva a data_atualizacao original de cada tarefa.
    """
    resultado: List[Tarefa] = []
    for nova_ordem, t in enumerate(tarefas_coluna):
        if t.ordem != nova_ordem:
            t_reindexada = Tarefa(
                id=t.id,
                titulo=t.titulo,
                descricao=t.descricao,
                estado=t.estado,
                prioridade=t.prioridade,
                data_criacao=t.data_criacao,
                data_limite=t.data_limite,
                data_atualizacao=t.data_atualizacao,  # Preserva data_atualizacao original
                data_conclusao=t.data_conclusao,
                ordem=nova_ordem,
            )
            resultado.append(t_reindexada)
        else:
            resultado.append(t)
    return resultado


def mover_tarefa(
    tarefas: List[Dict[str, Any]],
    tarefa_id: str,
    novo_estado: str,
    nova_ordem: Optional[int] = None,
    timestamp_injetado: Optional[str] = None,
    timestamp_global_atual: Optional[str] = None,
) -> Tuple[List[Dict[str, Any]], Optional[str], Dict[str, Any]]:
    """Move uma tarefa para outra coluna ou entre estados (RF04).

    Executa as regras de transição de estado da Seção 6.1 do REQUISITOS.md:
    1. a_fazer -> em_andamento: data_atualizacao = ts, data_conclusao = null
    2. a_fazer -> concluida: data_atualizacao = ts, data_conclusao = ts
    3. em_andamento -> a_fazer: data_atualizacao = ts, data_conclusao = null
    4. em_andamento -> concluida: data_atualizacao = ts, data_conclusao = ts
    5. concluida -> a_fazer: data_atualizacao = ts, data_conclusao = null (reabertura)
    6. concluida -> em_andamento: data_atualizacao = ts, data_conclusao = null (reabertura)

    Reindexa a coluna de origem e a coluna de destino garantindo ordens contíguas
    iniciando em 0. Tarefas reindexadas mantêm suas datas originais.
    """
    if not isinstance(novo_estado, str) or novo_estado not in ESTADOS_VALIDOS:
        raise ValueError(
            f"Estado de destino inválido: '{novo_estado}'. Permitidos: {sorted(list(ESTADOS_VALIDOS))}."
        )

    # Localizar tarefa
    tarefa_movida: Optional[Tarefa] = None
    for t in tarefas:
        if t.get("id") == tarefa_id:
            tarefa_movida = Tarefa.from_dict(t)
            break

    if tarefa_movida is None:
        raise ValueError(f"Tarefa com ID '{tarefa_id}' não encontrada para movimentação.")

    estado_anterior = tarefa_movida.estado

    # Se mover para a mesma coluna e mesma ordem (ou ordem None), trata como reordenação ou no-op
    if novo_estado == estado_anterior:
        alvo_ordem = tarefa_movida.ordem if nova_ordem is None else nova_ordem
        return reordenar_tarefa(
            tarefas=tarefas,
            tarefa_id=tarefa_id,
            nova_ordem=alvo_ordem,
            timestamp_injetado=timestamp_injetado,
            timestamp_global_atual=timestamp_global_atual,
        )

    # Transição entre colunas diferentes
    ts = timestamp_injetado if timestamp_injetado is not None else obter_timestamp_utc_atual()

    # Definir nova data_conclusao conforme as 6 transições
    if novo_estado == "concluida":
        nova_data_conclusao: Optional[str] = ts
    else:
        nova_data_conclusao = None

    # Separar tarefas da coluna de origem, de destino e outras
    coluna_origem: List[Tarefa] = []
    coluna_destino: List[Tarefa] = []
    outras_tarefas: List[Tarefa] = []

    for t in tarefas:
        obj = Tarefa.from_dict(t)
        if obj.id == tarefa_id:
            continue
        if obj.estado == estado_anterior:
            coluna_origem.append(obj)
        elif obj.estado == novo_estado:
            coluna_destino.append(obj)
        else:
            outras_tarefas.append(obj)

    # Ordenar listas atuais por ordem
    coluna_origem.sort(key=lambda x: x.ordem)
    coluna_destino.sort(key=lambda x: x.ordem)

    # Reindexar coluna de origem
    coluna_origem_reindexada = reindexar_coluna(coluna_origem)

    # Determinar posição na coluna de destino
    if nova_ordem is None or nova_ordem >= len(coluna_destino):
        posicao_destino = len(coluna_destino)
    elif nova_ordem < 0:
        posicao_destino = 0
    else:
        posicao_destino = nova_ordem

    # Criar tarefa movida atualizada
    tarefa_movida_atualizada = Tarefa(
        id=tarefa_movida.id,
        titulo=tarefa_movida.titulo,
        descricao=tarefa_movida.descricao,
        estado=novo_estado,
        prioridade=tarefa_movida.prioridade,
        data_criacao=tarefa_movida.data_criacao,
        data_limite=tarefa_movida.data_limite,
        data_atualizacao=ts,
        data_conclusao=nova_data_conclusao,
        ordem=posicao_destino,
    )

    # Inserir na posição e reindexar coluna de destino
    coluna_destino.insert(posicao_destino, tarefa_movida_atualizada)
    coluna_destino_reindexada: List[Tarefa] = []
    for idx, t in enumerate(coluna_destino):
        if t.id == tarefa_id:
            coluna_destino_reindexada.append(tarefa_movida_atualizada)
        elif t.ordem != idx:
            coluna_destino_reindexada.append(
                Tarefa(
                    id=t.id,
                    titulo=t.titulo,
                    descricao=t.descricao,
                    estado=t.estado,
                    prioridade=t.prioridade,
                    data_criacao=t.data_criacao,
                    data_limite=t.data_limite,
                    data_atualizacao=t.data_atualizacao,
                    data_conclusao=t.data_conclusao,
                    ordem=idx,
                )
            )
        else:
            coluna_destino_reindexada.append(t)

    # Consolidar novo estado de tarefas
    todas_final = coluna_origem_reindexada + coluna_destino_reindexada + outras_tarefas
    novas_tarefas_dict = [t.to_dict() for t in todas_final]

    return novas_tarefas_dict, ts, tarefa_movida_atualizada.to_dict()


def reordenar_tarefa(
    tarefas: List[Dict[str, Any]],
    tarefa_id: str,
    nova_ordem: int,
    timestamp_injetado: Optional[str] = None,
    timestamp_global_atual: Optional[str] = None,
) -> Tuple[List[Dict[str, Any]], Optional[str], Dict[str, Any]]:
    """Reordena uma tarefa dentro de sua própria coluna (RF05).

    Regras da Seção 6.2:
    - Tarefa diretamente movimentada: ordem alterada e data_atualizacao atualizada.
    - Demais tarefas reindexadas: ordem contígua atualizada, mas preservam suas respectivas
      data_atualizacao originais inalteradas.
    - Operação sem alteração real (drop na mesma ordem):
      nenhuma tarefa tem metadados alterados e o timestamp global não é atualizado.
    """
    tarefa_alvo: Optional[Tarefa] = None
    for t in tarefas:
        if t.get("id") == tarefa_id:
            tarefa_alvo = Tarefa.from_dict(t)
            break

    if tarefa_alvo is None:
        raise ValueError(f"Tarefa com ID '{tarefa_id}' não encontrada para reordenação.")

    estado_coluna = tarefa_alvo.estado

    # Coletar tarefas da mesma coluna
    tarefas_coluna: List[Tarefa] = []
    outras_tarefas: List[Tarefa] = []

    for t in tarefas:
        obj = Tarefa.from_dict(t)
        if obj.estado == estado_coluna:
            tarefas_coluna.append(obj)
        else:
            outras_tarefas.append(obj)

    tarefas_coluna.sort(key=lambda x: x.ordem)

    ordem_atual = -1
    for idx, t in enumerate(tarefas_coluna):
        if t.id == tarefa_id:
            ordem_atual = idx
            break

    # Ajustar limites de nova_ordem
    ordem_destino = max(0, min(nova_ordem, len(tarefas_coluna) - 1))

    # Operação sem alteração real (no-op)
    if ordem_atual == ordem_destino:
        return [dict(t) for t in tarefas], timestamp_global_atual, tarefa_alvo.to_dict()

    ts = timestamp_injetado if timestamp_injetado is not None else obter_timestamp_utc_atual()

    # Mover na lista
    item = tarefas_coluna.pop(ordem_atual)
    tarefa_movida_atualizada = Tarefa(
        id=item.id,
        titulo=item.titulo,
        descricao=item.descricao,
        estado=item.estado,
        prioridade=item.prioridade,
        data_criacao=item.data_criacao,
        data_limite=item.data_limite,
        data_atualizacao=ts,  # Apenas a diretamente movimentada atualiza data_atualizacao
        data_conclusao=item.data_conclusao,
        ordem=ordem_destino,
    )
    tarefas_coluna.insert(ordem_destino, tarefa_movida_atualizada)

    # Reindexar todas para contiguidade, preservando datas originais das demais
    coluna_reindexada: List[Tarefa] = []
    for idx, t in enumerate(tarefas_coluna):
        if t.id == tarefa_id:
            coluna_reindexada.append(tarefa_movida_atualizada)
        elif t.ordem != idx:
            coluna_reindexada.append(
                Tarefa(
                    id=t.id,
                    titulo=t.titulo,
                    descricao=t.descricao,
                    estado=t.estado,
                    prioridade=t.prioridade,
                    data_criacao=t.data_criacao,
                    data_limite=t.data_limite,
                    data_atualizacao=t.data_atualizacao,  # Preserva data original
                    data_conclusao=t.data_conclusao,
                    ordem=idx,
                )
            )
        else:
            coluna_reindexada.append(t)

    todas_final = coluna_reindexada + outras_tarefas
    return [t.to_dict() for t in todas_final], ts, tarefa_movida_atualizada.to_dict()


def excluir_tarefa(
    tarefas: List[Dict[str, Any]],
    tarefa_id: str,
    timestamp_injetado: Optional[str] = None,
) -> Tuple[List[Dict[str, Any]], str, Dict[str, Any]]:
    """Exclui uma tarefa e reindexa a coluna afetada para contiguidade (RF06).

    As demais tarefas reindexadas preservam suas respectivas data_atualizacao.
    Retorna: (novas_tarefas, novo_timestamp_global, tarefa_excluida_dict).
    """
    tarefa_excluida: Optional[Tarefa] = None
    for t in tarefas:
        if t.get("id") == tarefa_id:
            tarefa_excluida = Tarefa.from_dict(t)
            break

    if tarefa_excluida is None:
        raise ValueError(f"Tarefa com ID '{tarefa_id}' não encontrada para exclusão.")

    ts = timestamp_injetado if timestamp_injetado is not None else obter_timestamp_utc_atual()
    estado_afetado = tarefa_excluida.estado

    coluna_afetada: List[Tarefa] = []
    outras_tarefas: List[Tarefa] = []

    for t in tarefas:
        obj = Tarefa.from_dict(t)
        if obj.id == tarefa_id:
            continue
        if obj.estado == estado_afetado:
            coluna_afetada.append(obj)
        else:
            outras_tarefas.append(obj)

    coluna_afetada.sort(key=lambda x: x.ordem)
    coluna_reindexada = reindexar_coluna(coluna_afetada)

    todas_final = coluna_reindexada + outras_tarefas
    return [t.to_dict() for t in todas_final], ts, tarefa_excluida.to_dict()
