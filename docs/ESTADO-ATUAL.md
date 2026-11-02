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
  - *Repositório remoto:* `josearodrigues/alura-todolist-kanban`
  - *Branch confirmada:* `main`
  - *Branch remota:* `main`.
  - *Histórico remoto:* as correções da Fase 1 foram registradas diretamente no GitHub após o commit `f351004`, culminando no commit `0ef5cf4`.
  - *Situação local/remota:* o usuário confirmou o `pull` de `origin/main` até `0ef5cf4`; a cópia local está sincronizada com a branch remota nesse commit.
  - *Ações realizadas nesta revisão:* correções de código, testes e documentação registradas diretamente na branch `main`. Nenhuma tag, release ou publicação da aplicação foi criada.
- **Mockup Oficial de Referência:**
  - `docs/design/referencias/todolist-kanban-1.0-mockup.png`: Presente, verificado e preservado intacto em sua forma binária original.

---

## 3. Estado da Governança Documental

A tríade documental mandatória encontra-se plenamente estabelecida e atualizada:
- **`docs/REQUISITOS.md`:** Atualizado (Versão 1.7 — RNF06 alinhado aos critérios normativos de contraste WCAG 2.2 AA).
- **`docs/PLANO-IMPLEMENTACAO.md`:** Atualizado (Versão 2.1 — plano aprovado; situação da Etapa 4 e autorização da Fase 1 alinhadas ao estado real, com registro da revisão corretiva).
- **`docs/ESTADO-ATUAL.md`:** Atualizado com o estado operacional corrente (este documento).

---

## 4. Situação de Cada Etapa e Fase do Projeto

| Etapa / Fase | Situação | Descrição / Entregáveis |
| :--- | :--- | :--- |
| **Etapa 1 — Descoberta e Requisitos** | **Concluída e Aprovada** | Levantamento via método Grill Me; requisitos aprovados. |
| **Etapa 2 — Planejamento Funcional** | **Concluída e Aprovada** | Especificação consolidada de RF01–RF15, RNF01–RNF07 e regras de negócio. |
| **Etapa 3 — Arquitetura Técnica** | **Concluída e Aprovada** | Sete decisões técnicas aprovadas, arquitetura modular e critérios de testes definidos. |
| **Etapa 4 — Plano de Implementação** | **Concluída e Aprovada** | Plano de Implementação (versão 2.1) formalmente aprovado pelo usuário. |
| **Etapa 5 — Implementação Controlada** | **Em andamento** | Fase 1 concluída; Fase 2 implementada, com validação formal pendente; Fases 3 a 6 não iniciadas. |
| ↳ *Fase 1: Domínio Python e Testes* | **Concluída e Validada** | Pacote `src/todolist/`, `pyproject.toml`, testes automatizados (`tests/`) e `scripts/verify_coverage.py` implementados. Após a revisão corretiva, o procedimento oficial aprovou 48/48 testes, com 96,16% de cobertura de linhas e 92,78% de branches. |
| ↳ *Fase 2: HTML e Acessibilidade* | **Implementada; validação pendente** | `index.html` criado com estrutura semântica, três colunas, widgets, formulários, diálogos nativos, controles acessíveis e atalhos básicos. Nu HTML Checker e checklist manual de teclado/foco ainda não executados. |
| ↳ *Fase 3: CSS e Validação Visual* | Não iniciada | Design system, temas, `check_contrast.py` e versão visual corrigida. |
| ↳ *Fase 4: WebAssembly e Persistência* | Não iniciada | Carregamento Pyodide no virtual FS e `storage.js` com rollback. |
| ↳ *Fase 5: Interações (Pointer Events)* | Não iniciada | Drag and drop unificado, touch, menu acessível, busca e calendário. |
| ↳ *Fase 6: Relatórios e Backup JSON* | Não iniciada | Modal de relatórios, exportação e importação atômica estrita. |
| **Etapa 6 — Validação Final** | **Não iniciada** | Homologação integrada e testes de aceitação. |

---

## 5. Matriz de Rastreabilidade

- **Planejado:** Aplicação To-Do Kanban estática com Python via WebAssembly (Pyodide), 3 colunas, drag and drop via Pointer Events, calendário integrado, métricas em tempo real e backup JSON.
- **Aprovado:** Versão 1.7 de Requisitos (RNF06 alinhado à WCAG 2.2 AA), Etapa 3 (Arquitetura Técnica) e Etapa 4 (Plano de Implementação, versão 2.1) formalmente aprovadas.
- **Implementado:** Fase 1 implementada: pacote Python `src/todolist/` (`models.py`, `services.py`, `metrics.py`, `schema.py`, `__init__.py`), configuração `pyproject.toml`, suíte `tests/` e script `scripts/verify_coverage.py`. Fases 2 a 6 não implementadas.
- **Testado:** Fase 1: procedimento oficial `pytest && python scripts/verify_coverage.py`, com 48/48 testes aprovados, 96,16% de cobertura de linhas e 92,78% de branches. Fase 2: inspeção estática do arquivo e confirmação de três botões de criação, IDs e mecanismos de diálogo/atalho; Nu HTML Checker e testes manuais em navegador ainda pendentes.
- **Validado:** critérios CA1.1 a CA1.7 aceitos conforme evidências informadas pelo usuário. Na Fase 2, a implementação estrutural foi revisada, mas CA2.2 a CA2.6 ainda não podem ser declarados validados sem o relatório Nu e o checklist manual em navegador.
- **Commitado / Enviado ao GitHub:** Fase 2 registrada diretamente na branch remota `main`: `e03fd94` (criação de `index.html`) e `92c3eed` (ajustes de rótulos e atalhos). A cópia local precisa sincronizar esses commits. Nenhuma tag, release ou publicação da aplicação foi criada.

---

## 6. Resumo das Decisões Técnicas Aprovadas (Etapa 3)

1. **Decisão 3.1 (Motor WebAssembly):** Pyodide Direto com carregamento individual dos módulos Python via `fetch()` assíncrono no virtual filesystem (`pyodide.FS`), mantendo o Python puro e desacoplado do DOM.
2. **Decisão 3.2 (Persistência):** Documento JSON único no `localStorage` com persistência preventiva: validação e gravação síncrona antes da confirmação em memória e atualização visual; em caso de falha, rollback em memória e notificação ao usuário.
3. **Decisão 3.3 (Domínio Python):** Abordagem híbrida no pacote `src/todolist/`: entidade `Tarefa` estruturada com `@dataclass` e validações defensivas explícitas, combinada com serviços funcionais sem efeitos colaterais e com suporte a injeção determinística de datas e identificadores.
4. **Decisão 3.4 (Identificadores e Invariantes):** UUID v4 nativo em string canônica, contiguidade ordinal estrita por coluna iniciando em zero (sem normalização silenciosa na importação) e 8 invariantes temporais em formato ISO 8601 UTC com milissegundos.
5. **Decisão 3.5 (Estratégia de Testes):** Procedimento oficial `pytest && python scripts/verify_coverage.py`, exigindo 100% de aprovação de testes, $\ge 90,0\%$ de declarações (`percent_covered`) e $\ge 85,0\%$ de ramos (`percent_branches_covered`) via `coverage.json`.
6. **Decisão 3.6 (Frontend e Acessibilidade):** Validação de HTML pelo Nu HTML Checker (v.Nu local), auditoria matemática de contraste via script `check_contrast.py` (WCAG 2.2 AA, critérios 1.4.3 e 1.4.11), checklist manual estruturado de teclado e adoção de **Pointer Events** para unificar mouse, toque e caneta no drag and drop.
7. **Decisão 3.7 (Arquitetura Modular):** Organização completa em pastas com `pyproject.toml` na raiz, pacote `src/todolist/`, módulos JavaScript ES6+ desacoplados, CSS modular e scripts de suporte.

---

## 7. Informações e Pendências de Confirmação

- **Ambiente Git:** Repositório remoto `josearodrigues/alura-todolist-kanban`, branch `main`, commit `0ef5cf4`. O usuário confirmou a sincronização da cópia local com `origin/main`.
- **Implementação:** Fase 1 concluída e validada; Fase 2 implementada em `index.html`. Pendências da Fase 2: validar o documento no Nu HTML Checker e executar checklist manual de teclado, foco, diálogos e menus em navegador. Fases 3 a 6 permanecem não iniciadas.

---

## 8. Próxima Ação Recomendada

1. **Fase 1 encerrada:** implementação e validação concluídas; 48/48 testes aprovados, cobertura de linhas de 96,16% e branches de 92,78%.
2. **Fase 2:** executar validação Nu HTML Checker e checklist manual de acessibilidade; registrar os resultados antes de declarar os critérios CA2.2–CA2.6 validados.
3. Após a validação da Fase 2, aguardar a autorização correspondente para iniciar a Fase 3.
