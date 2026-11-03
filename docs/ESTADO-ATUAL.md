# Estado Atual do Projeto — To-Do List Kanban

**Data da última atualização:** 2026-11-03

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
  - *Histórico remoto:* a Fase 1 culminou no commit `0ef5cf4`. A Fase 2 foi registrada em `main` por meio dos commits de implementação HTML e atualizações documentais; a pipeline Nu HTML Checker foi adicionada no commit `11f6cdf`; a correção HTML foi registrada em `a6c7495` e o diagnóstico detalhado da pipeline em `58558ad`. A implementação CSS da Fase 3 e a auditoria de contraste foram adicionadas diretamente à `main` nesta sessão.
  - *Situação local/remota:* a branch remota `main` foi verificada após as alterações desta sessão. A situação da cópia local não foi verificada nesta sessão; sua sincronização permanece sob controle do usuário.
  - *Ações realizadas nesta revisão:* correções de código, testes e documentação registradas diretamente na branch `main`. Nenhuma tag, release ou publicação da aplicação foi criada.
- **Mockup Oficial de Referência:**
  - Arquivo `Painel Kanban de Tarefas Pastel.png`, localizado na Biblioteca do projeto Desafios Alura e consultado durante a revisão visual de 2026-11-02/03.
  - O PNG histórico versionado em `docs/design/referencias/todolist-kanban-1.0-mockup.png` permanece preservado intacto.

---

## 3. Estado da Governança Documental

A tríade documental mandatória encontra-se plenamente estabelecida e atualizada:
- **`docs/REQUISITOS.md`:** Atualizado (Versão 1.7 — RNF06 alinhado aos critérios normativos de contraste WCAG 2.2 AA).
- **`docs/PLANO-IMPLEMENTACAO.md`:** Atualizado (Versão 2.1 — plano aprovado; situação da Etapa 4 e autorização da Fase 1 alinhadas ao estado real, com registro da revisão corretiva).
- **`docs/ESTADO-ATUAL.md`:** Atualizado com o estado operacional corrente (este documento).
- **`README.md`:** Atualizado com tecnologias, estrutura do projeto, instruções de execução, testes, roteiro manual da Fase 2 e roteiro de inspeção visual da Fase 3.\n- **`CHANGELOG.md`:** Registra as alterações implementadas por fase.\n- **`LICENSE`:** Licença MIT.

---

## 4. Situação de Cada Etapa e Fase do Projeto

| Etapa / Fase | Situação | Descrição / Entregáveis |
| :--- | :--- | :--- |
| **Etapa 1 — Descoberta e Requisitos** | **Concluída e Aprovada** | Levantamento via método Grill Me; requisitos aprovados. |
| **Etapa 2 — Planejamento Funcional** | **Concluída e Aprovada** | Especificação consolidada de RF01–RF15, RNF01–RNF07 e regras de negócio. |
| **Etapa 3 — Arquitetura Técnica** | **Concluída e Aprovada** | Sete decisões técnicas aprovadas, arquitetura modular e critérios de testes definidos. |
| **Etapa 4 — Plano de Implementação** | **Concluída e Aprovada** | Plano de Implementação (versão 2.1) formalmente aprovado pelo usuário. |
| **Etapa 5 — Implementação Controlada** | **Em andamento** | Fase 1 concluída; Fase 2 implementada, com checklist manual pendente; Fase 3 com revisão visual implementada e workflow automatizado aprovado, mas inspeção visual e aceite formal pendentes. Fases 4 a 6 não iniciadas. |
| ↳ *Fase 1: Domínio Python e Testes* | **Concluída e Validada** | Pacote `src/todolist/`, `pyproject.toml`, testes automatizados (`tests/`) e `scripts/verify_coverage.py` implementados. Após a revisão corretiva, o procedimento oficial aprovou 48/48 testes, com 96,16% de cobertura de linhas e 92,78% de branches. |
| ↳ *Fase 2: HTML e Acessibilidade* | **Implementada; validação formal parcial** | `index.html` contém estrutura semântica, três colunas, widgets, formulários, seis diálogos nativos, template de cartão, nomes acessíveis, atalhos e contenção explícita do foco nos diálogos. Foram aprovadas 20 verificações automatizadas gerais em Chromium; os seis diálogos também foram exercitados individualmente. Pipeline `.github/workflows/validar-html.yml` criada para submeter `index.html` ao Nu HTML Checker em pushes/PRs relevantes e sob acionamento manual. Execução `41520632228` concluída com sucesso: zero erros e zero avisos. `README.md` documenta o servidor local, o comando de execução e o roteiro manual. Permanece pendente o checklist manual humano. |
| ↳ *Fase 3: CSS e Validação Visual* | **Implementação visual em revisão; validação pendente** | Interface reorganizada para aproximar o mockup oficial: sidebar, navegação, banner `Olá!`, três colunas, cartões, painel de informações, rodapé e diálogos preservados. CSS modular, temas, breakpoints e movimento reduzido mantidos. Workflow `41550901785` concluído com sucesso: auditoria de contraste e etapa de validação HTML aprovadas. Não foi realizada inspeção em navegador nos seis cenários (três breakpoints × dois temas); A evidência automatizada de CA3.4 foi aprovada; CA3.1–CA3.3 e CA3.5 ainda dependem de inspeção visual. Calendário, métricas dinâmicas e operações permanecem placeholders/desabilitados conforme as fases de integração. |
| ↳ *Fase 4: WebAssembly e Persistência* | Não iniciada | Carregamento Pyodide no virtual FS e `storage.js` com rollback. |
| ↳ *Fase 5: Interações (Pointer Events)* | Não iniciada | Drag and drop unificado, touch, menu acessível, busca e calendário. |
| ↳ *Fase 6: Relatórios e Backup JSON* | Não iniciada | Modal de relatórios, exportação e importação atômica estrita. |
| **Etapa 6 — Validação Final** | **Não iniciada** | Homologação integrada e testes de aceitação. |

---

## 5. Matriz de Rastreabilidade

- **Planejado:** Aplicação To-Do Kanban estática com Python via WebAssembly (Pyodide), 3 colunas, drag and drop via Pointer Events, calendário integrado, métricas em tempo real e backup JSON.
- **Aprovado:** Versão 1.7 de Requisitos (RNF06 alinhado à WCAG 2.2 AA), Etapa 3 (Arquitetura Técnica) e Etapa 4 (Plano de Implementação, versão 2.1) formalmente aprovadas.
- **Implementado:** Em 2026-11-03, a interface visual da Fase 3 foi reorganizada para maior proximidade com o mockup oficial; a saudação continua `Olá!`, e os diálogos existentes foram preservados. Fase 1 implementada: pacote Python `src/todolist/` (`models.py`, `services.py`, `metrics.py`, `schema.py`, `__init__.py`), configuração `pyproject.toml`, suíte `tests/` e script `scripts/verify_coverage.py`. Fase 2 implementada em `index.html`; workflow `.github/workflows/validar-html.yml` criado para validação Nu HTML Checker; `README.md` documenta execução e verificação manual. Fase 3 com revisão visual implementada, workflow aprovado e inspeção visual pendente; Fases 4 a 6 não iniciadas.
- **Testado:** Fase 1: procedimento oficial `pytest && python scripts/verify_coverage.py`, com 48/48 testes aprovados, 96,16% de cobertura de linhas e 92,78% de branches. Fase 2: 20 verificações automatizadas em Chromium foram aprovadas, cobrindo estrutura e nomes acessíveis, rótulos de campos, `Ctrl + K`, `Esc`, menus por teclado, abertura/fechamento de diálogos, foco inicial, contenção do foco com `Tab` e `Shift + Tab`, retorno do foco, link de salto e foco visível. Nenhum erro de JavaScript foi observado. Os seis diálogos foram testados individualmente quanto ao foco inicial, contenção bidirecional com `Tab`/`Shift + Tab`, fechamento com `Esc` e restauração do foco. A inspeção com parser HTML local não apontou erros, mas não substitui o Nu HTML Checker.
- **Validado:** critérios CA1.1 a CA1.7 aceitos conforme evidências informadas pelo usuário. Na Fase 2, CA2.1 foi verificado por inspeção estrutural e automatização no navegador. CA2.2 foi validado pelo Nu HTML Checker na execução `41520632228`, sem erros ou avisos. Os comportamentos previstos em CA2.3 a CA2.6 passaram pelas verificações automatizadas descritas acima; o aceite formal da Fase 2 permanece pendente do checklist manual humano previsto no plano.
- **Commitado / Enviado ao GitHub:** Revisão visual registrada diretamente na branch remota `main`: `d02c4fe` (estrutura visual) e `b5c3200` (ajustes de tema e foco). O workflow `41550901785`, acionado pelo commit `b5c3200`, concluiu com sucesso (auditoria de contraste e etapa de validação HTML). Fase 2 registrada diretamente na branch remota `main`. O workflow Nu HTML Checker foi adicionado no commit `11f6cdf`, seus diagnósticos foram aprimorados em `58558ad` e as correções HTML foram registradas em `a6c7495`. Na Fase 3, os arquivos `css/variables.css`, `css/base.css`, `css/layout.css`, `css/kanban.css`, `css/components.css` e `scripts/check_contrast.py` foram criados; `index.html` passou a carregar os estilos e a alternar temas. O workflow `.github/workflows/validar-html.yml` foi ampliado para auditar contraste e considerar alterações em CSS. A cópia local ainda precisa ser sincronizada pelo usuário. Nenhuma tag, release ou publicação da aplicação foi criada.

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

- **Ambiente Git:** Repositório remoto `josearodrigues/alura-todolist-kanban`, branch `main`; estado remoto conferido após a criação do `README.md`. A cópia local não foi inspecionada.
- **Implementação:** Fase 1 concluída e validada; Fase 2 implementada e submetida a 20 verificações automatizadas de navegador. A pipeline Nu HTML Checker foi executada com sucesso (zero erros e zero avisos). O `README.md` foi criado com o comando `python -m http.server 8000 --bind 127.0.0.1` e o roteiro manual; a execução desse checklist pelo usuário permanece pendente. Fase 3: estilos modulares, temas, responsividade, movimento reduzido e script de contraste implementados; workflow `41550901785` aprovado. A auditoria do script foi aprovada; inspeção visual nos seis cenários responsivos/temas permanece pendente. Fases 4 a 6 permanecem não iniciadas.

---

## 8. Próxima Ação Recomendada

1. **Fase 1 encerrada:** implementação e validação concluídas; 48/48 testes aprovados, cobertura de linhas de 96,16% e branches de 92,78%.
2. **Fase 2:** CA2.2 validado pela pipeline Nu HTML Checker (execução `41520632228`: zero erros e zero avisos). Executar o checklist manual documentado no `README.md`, previsto nos critérios CA2.3–CA2.6; não declarar a fase formalmente encerrada antes dessa evidência.
3. **Fase 3:** realizar inspeção visual em Desktop (>=1200 px), Tablet (768–1199 px) e Mobile (<768 px), nos temas Claro e Escuro, incluindo `prefers-reduced-motion`. A auditoria automatizada CA3.4 foi aprovada; verificar CA3.1–CA3.3 e CA3.5 visualmente e corrigir divergências antes do aceite final. O mockup da Biblioteca foi usado como referência; o PNG histórico versionado permanece preservado.
