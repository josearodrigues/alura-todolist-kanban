# Estado Atual do Projeto — To-Do List Kanban

**Data da última atualização:** 2026-11-02

## 1. Identificação do Desafio e Objetivo

- **Projeto:** Desafio 3 – Construção de uma aplicação To-Do List Kanban com Python e hospedagem no GitHub Pages.
- **Programa:** Imersão Engenharia de Software: Dev na Era da IA (Alura + Google for Startups).
- **Princípio Pedagógico:** Compreender, planejar, implementar, validar e explicar.
- **Linguagem Central:** Python (executado via WebAssembly no navegador).
- **Ambiente de Hospedagem:** GitHub Pages (aplicação 100% estática).

---

## 2. Estado Operacional do Repositório e Ambiente

- **Diretório Local de Trabalho:**
  - *Caminho absoluto:* `/home/joserodrigues/1h/Alura/20261026-Imersão Engenharia de Software- Dev na Era da IA/projetos/alura-kanban-python`
  - *Nome da pasta local:* `alura-kanban-python`
- **Repositório Remoto no GitHub:**
  - *Proprietário:* `josearodrigues`
  - *Nome do repositório:* `alura-todolist-kanban`
  - *URL Canônica:* `https://github.com/josearodrigues/alura-todolist-kanban`
  - *Relação de Nomenclatura:* A distinção entre o nome da pasta de trabalho local (`alura-kanban-python`) e o repositório remoto (`alura-todolist-kanban`) é intencional e preservada, sem exigência de renomeação.
- **Controle de Versão (Git):**
  - *Branch atual e commit confirmado:* Pendentes de verificação via terminal devido a restrições operacionais do sandbox nesta sessão.
  - *Ações realizadas:* Nenhuma operação de commit, push, tag ou publicação remota foi executada.
- **Mockup Oficial de Referência:**
  - `docs/design/referencias/todolist-kanban-1.0-mockup.png`: Presente, verificado e preservado intacto em sua forma binária original.

---

## 3. Estado da Governança Documental

A tríade documental mandatória encontra-se plenamente estabelecida e atualizada:
- **`docs/REQUISITOS.md`:** Atualizado (Versão 1.5 Corrigida).
- **`docs/PLANO-IMPLEMENTACAO.md`:** Atualizado e consolidado com as 7 decisões da Etapa 3.
- **`docs/ESTADO-ATUAL.md`:** Atualizado com o estado operacional corrente (este documento).

---

## 4. Situação de Cada Etapa e Fase do Projeto

| Etapa / Fase | Situação | Descrição / Entregáveis |
| :--- | :--- | :--- |
| **Etapa 1 — Descoberta e Requisitos** | **Concluída** | Levantamento via método Grill Me; requisitos aprovados. |
| **Etapa 2 — Planejamento Funcional** | **Concluída e Aprovada** | Especificação consolidada de RF01–RF15, RNF01–RNF07 e regras de negócio. |
| **Etapa 3 — Arquitetura Técnica** | **Concluída e Aprovada** | Sete decisões técnicas aprovadas, arquitetura modular e critérios de testes definidos. |
| **Etapa 4 — Plano de Implementação** | **Pendente** | Detalhamento final das fases antes de codificar. |
| **Etapa 5 — Implementação Controlada** | **Não iniciada** | Zero código de aplicação implementado. Aguarda autorização expressa. |
| ↳ *Fase 1: Domínio Python e Testes* | Não iniciada | Pacote `src/todolist/`, `pyproject.toml`, testes e `verify_coverage.py`. |
| ↳ *Fase 2: HTML e Acessibilidade* | Não iniciada | Estrutura semântica `index.html` e validação Nu HTML Checker. |
| ↳ *Fase 3: CSS e Validação Visual* | Não iniciada | Design system, temas, `check_contrast.py` e versão visual corrigida. |
| ↳ *Fase 4: WebAssembly e Persistência* | Não iniciada | Carregamento Pyodide no virtual FS e `storage.js` com rollback. |
| ↳ *Fase 5: Interações (Pointer Events)* | Não iniciada | Drag and drop unificado, touch, menu acessível, busca e calendário. |
| ↳ *Fase 6: Relatórios e Backup JSON* | Não iniciada | Modal de relatórios, exportação e importação atômica estrita. |
| **Etapa 6 — Validação Final** | **Não iniciada** | Homologação integrada e testes de aceitação. |

---

## 5. Matriz de Rastreabilidade

- **Planejado:** Aplicação To-Do Kanban estática com Python via WebAssembly (Pyodide), 3 colunas, drag and drop via Pointer Events, calendário integrado, métricas em tempo real e backup JSON.
- **Aprovado:** Versão 1.5 de Requisitos e Etapa 3 de Arquitetura e Planejamento Técnico formalmente aprovadas.
- **Implementado:** Zero código de aplicação implementado até o momento.
- **Testado:** Nenhum teste automatizado executado ainda (arquivos de teste não criados).
- **Validado:** Auditoria estrutural documental e integridade do mockup oficial.
- **Commitado / Enviado ao GitHub / Publicado:** Nenhuma alteração foi commitada ou publicada.

---

## 6. Resumo das Decisões Técnicas Aprovadas (Etapa 3)

1. **Decisão 3.1 (Motor WebAssembly):** Pyodide Direto com carregamento individual dos módulos Python via `fetch()` assíncrono no virtual filesystem (`pyodide.FS`), mantendo o Python puro e desacoplado do DOM.
2. **Decisão 3.2 (Persistência):** Documento JSON único no `localStorage` com persistência preventiva: validação e gravação síncrona antes da confirmação em memória e atualização visual; em caso de falha, rollback em memória e notificação ao usuário.
3. **Decisão 3.3 (Domínio Python):** Abordagem híbrida no pacote `src/todolist/`: entidade `Tarefa` estruturada com `@dataclass` e validações defensivas explícitas, combinada com serviços funcionais sem efeitos colaterais e com suporte a injeção determinística de datas e identificadores.
4. **Decisão 3.4 (Identificadores e Invariantes):** UUID v4 nativo em string canônica, contiguidade ordinal estrita por coluna iniciando em zero (sem normalização silenciosa na importação) e 8 invariantes temporais em formato ISO 8601 UTC com milissegundos.
5. **Decisão 3.5 (Estratégia de Testes):** Procedimento oficial `pytest && python scripts/verify_coverage.py`, exigindo 100% de aprovação de testes, $\ge 90,0\%$ de declarações (`percent_statements_covered`) e $\ge 85,0\%$ de ramos (`percent_branches_covered`) via `coverage.json`.
6. **Decisão 3.6 (Frontend e Acessibilidade):** Validação de HTML pelo Nu HTML Checker (v.Nu local), auditoria matemática de contraste via script `check_contrast.py` (WCAG 2.2 AA), checklist manual estruturado de teclado e adoção de **Pointer Events** para unificar mouse, toque e caneta no drag and drop.
7. **Decisão 3.7 (Arquitetura Modular):** Organização completa em pastas com `pyproject.toml` na raiz, pacote `src/todolist/`, módulos JavaScript ES6+ desacoplados, CSS modular e scripts de suporte.

---

## 7. Informações e Pendências de Confirmação

- **Ambiente Git:** O status exato da árvore de trabalho e do histórico do Git local não pôde ser auditado via comando de terminal devido ao bloqueio da interface sandbox nesta sessão. Nenhuma instrução Git foi executada.
- **Implementação:** Nenhum arquivo de código foi implementado; os diretórios de código (`src/`, `js/`, `css/`, `tests/`, `scripts/`) permanecem no planejamento aguardando a autorização para a Fase 1.

---

## 8. Próxima Ação Recomendada

- **Apresentar a consolidação documental conjunta para revisão do usuário.**
- **Aguardar a avaliação formal do usuário sobre a conclusão documental da Etapa 3.**
- **Solicitar autorização expressa para o início da Etapa 4 (Plano de Implementação Detalhado) ou autorização para a Fase 1 da implementação.**
