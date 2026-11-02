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
  - *Histórico remoto:* correções da Fase 1 foram registradas diretamente no GitHub após o commit `f351004`; a sincronização da cópia local não foi verificada.
  - *Situação remota:* A referência acima corresponde ao commit verificado imediatamente antes desta atualização documental. A sincronização entre a árvore local e o repositório remoto não foi verificada.
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
| **Etapa 5 — Implementação Controlada** | **Em andamento** | Execução autorizada para a Fase 1. Fases 2 a 6 não iniciadas. |
| ↳ *Fase 1: Domínio Python e Testes* | Em andamento (Implementada e Testada) | Pacote `src/todolist/`, `pyproject.toml`, testes automatizados (`tests/`) e `scripts/verify_coverage.py` implementados; 41 testes aprovados na execução anterior à revisão corretiva. Foram adicionados 7 casos de teste e alterados os módulos de domínio; a suíte e as metas de cobertura precisam ser executadas novamente antes do aceite final. |
| ↳ *Fase 2: HTML e Acessibilidade* | Não iniciada | Estrutura semântica `index.html` e validação Nu HTML Checker. |
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
- **Testado:** antes da revisão corretiva, 41 testes passaram com cobertura de 96,05% de declarações e 92,47% de ramos. Após as correções, foram acrescentados 7 testes; a execução atualizada ainda está pendente.
- **Validado:** CA1.7 foi comprovado na execução anterior às correções. O aceite final de CA1.1 a CA1.7 permanece pendente da nova execução do procedimento oficial após as alterações.
- **Commitado / Enviado ao GitHub:** correções registradas diretamente na branch remota `main` por commits do GitHub. A sincronização da árvore local não foi verificada. Nenhuma tag, release ou publicação da aplicação foi criada.

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

- **Ambiente Git:** Repositório remoto `josearodrigues/alura-todolist-kanban`, branch `main`. Houve alterações remotas nesta revisão; o estado da árvore de trabalho local e sua sincronização com o remoto não foram avaliados.
- **Implementação:** Fase 1 do domínio Python implementada (`src/todolist/`, `tests/`, `scripts/verify_coverage.py` e `pyproject.toml`). Os diretórios e arquivos das fases subsequentes (`js/`, `css/`, `index.html`, `scripts/check_contrast.py`) não foram criados e aguardam autorização formal da Fase 2.

---

## 8. Próxima Ação Recomendada

1. Sincronizar a cópia local com a branch `main` remota e executar `pytest && python scripts/verify_coverage.py`.
2. Revisar os resultados atualizados e, se as metas forem atendidas, encerrar formalmente a Fase 1.
3. Manter as Fases 2 a 6 da Etapa 5 como não iniciadas até autorização expressa do usuário.
