# Plano de Implementação — To-Do List Kanban

## 1. Visão Geral e Estrutura de Etapas

O desenvolvimento da aplicação é estruturado em etapas controladas, respeitando o princípio pedagógico e de engenharia de software: **Compreender, implementar, validar e explicar.**

- **Etapa 1 — Descoberta e levantamento de requisitos:** [Concluída]
- **Etapa 2 — Planejamento funcional e documentação:** [Concluída]
- **Etapa 3 — Arquitetura e planejamento técnico:** [Pendente de início/aprovação]
- **Etapa 4 — Plano de implementação detalhado:** [Pendente]
- **Etapa 5 — Implementação controlada (Fases 1 a 6):** [Pendente de autorização]
- **Etapa 6 — Validação final e homologação:** [Pendente]

---

## 2. Fases de Implementação Controlada

A execução da Etapa 5 será dividida em seis fases pequenas, sequenciais e verificáveis:

### Fase 1 — Fundação do Domínio Python e Testes Automatizados
- **Objetivo:** Construir o núcleo de regras de negócio, manipulação de estado do Kanban, métricas de relatórios, cálculos temporais e validação de schema JSON em Python puro.
- **Arquivos Previstos:** `src/python/` e `tests/`.
- **Atividades:**
  - Implementar estruturas de dados e regras para as tarefas (10 atributos).
  - Implementar operações de transição de estado, reordenação ordinal intra-coluna e regras de metadados (`data_atualizacao`, `data_conclusao`).
  - Implementar cálculo de indicadores para relatórios, vencimentos e atrasos dinâmicos.
  - Implementar validação preventiva de schema para importação e exportação JSON (rejeição de campos desconhecidos).
- **Dependências:** Ambiente de desenvolvimento Python e suíte `pytest`.
- **Critérios e Evidências de Conclusão:** Execução de `pytest -v` no terminal com 100% dos testes aprovados, cobrindo integralmente as 6 transições de estado, reordenações, partições temporais e rejeição de arquivos inválidos.

---

### Fase 2 — Estrutura HTML Semântica e Acessibilidade Estrutural
- **Objetivo:** Desenvolver a estrutura semântica da página (`index.html`), contemplando layout de 3 painéis, modais, formulários acessíveis e saudação neutra aprovada.
- **Arquivos Previstos:** `index.html`.
- **Atividades:**
  - Estruturar a barra lateral (Sidebar) com links funcionais e cartões informativos.
  - Implementar o cabeçalho com campo de busca (`Ctrl + K`), alternador de tema e status da aplicação.
  - Estruturar a área principal com o banner de saudação contendo o texto **"Olá!"** e as 3 colunas do Kanban (*A Fazer*, *Em Andamento*, *Concluídas*).
  - Estruturar a barra de widgets (Calendário, Resumo do Projeto, Status do Runtime).
  - Estruturar modais para Nova Tarefa/Editar Tarefa, Confirmação de Exclusão, Relatórios e Importar/Exportar.
  - Inserir semântica acessível: atributos ARIA, labels descritivos, focus trap e navegação lógica por teclado.
- **Dependências:** Conclusão da Fase 1.
- **Critérios e Evidências de Conclusão:**
  1. Relatório de validação HTML sem erros de estrutura ou semântica.
  2. Roteiro de testes de acessibilidade via teclado: tabulação lógica, funcionamento de formulários, abertura/fechamento de modais via `Esc` e menus acessíveis.

---

### Fase 3 — Design System, Estilos Responsivos e Validação Visual (CSS)
- **Objetivo:** Implementar o design system moderno em CSS puro, variáveis para os temas Claro e Escuro, adaptação fluida para Desktop, Tablet e Mobile, e produção do mockup visual com a saudação atualizada.
- **Arquivos Previstos:** `css/`.
- **Atividades:**
  - Definir variáveis CSS nativas (`:root`) para temas Claro e Escuro conforme paleta aprovada.
  - Estilizar painéis, cartões com cantos arredondados, elevações suaves, badges de prioridade e barras de progresso proporcionais.
  - Implementar regras de mídia responsivas (Desktop $\ge 1200\text{px}$, Tablet $768\text{px}-1199\text{px}$, Mobile $< 768\text{px}$ com rolagem horizontal de colunas e menu drawer retrátil).
  - **Atividade Específica do Mockup:** Produzir a versão visual de referência com a saudação corrigida para "Olá!", mantendo o arquivo PNG original intacto como referência histórica.
  - Aplicar suporte à diretiva `prefers-reduced-motion`.
- **Dependências:** Conclusão da Fase 2.
- **Critérios e Evidências de Conclusão:**
  1. Relatório de contraste de cores demonstrando razão $\ge 4.5:1$ nos temas Claro e Escuro (WCAG 2.2 AA).
  2. Evidência documental de inspeção visual confirmando integridade do layout nas resoluções de Desktop, Tablet e Mobile nos dois temas.

---

### Fase 4 — Integração WebAssembly e Persistência Segura com Garantia de Rollback
- **Objetivo:** Inicializar o runtime WebAssembly no navegador, carregar os módulos Python de domínio, estabelecer a ponte de comunicação bidirecional JS $\leftrightarrow$ Python e implementar o motor de persistência consistente no `localStorage`.
- **Arquivos Previstos:** `js/pyodide_bridge.js` (ou equivalente WebAssembly), `js/storage.js`, `js/app.js`.
- **Atividades:**
  - Carregar o interpretador WebAssembly via CDN e carregar o código Python de domínio.
  - Implementar a sincronização bidirecional entre a interface e o estado Python.
  - Implementar o salvamento persistente do estado das tarefas e do timestamp global da última alteração.
  - Implementar o mecanismo de proteção que reverte alterações em memória e na tela diante de falhas de gravação (ex.: `QuotaExceededError`).
- **Dependências:** Conclusão das Fases 1, 2 e 3.
- **Critérios e Evidências de Conclusão:**
  1. Indicador de status transicionando visualmente para `✓ Carregado`.
  2. Testes de ciclo de vida e persistência executados separadamente para criação, edição, movimentação e exclusão, com recarga da página (`F5`) comprovando retenção íntegra e atualização sincronizada do timestamp.
  3. Teste de falha de gravação simulada comprovando preservação do estado anterior e notificação de erro ao usuário.

---

### Fase 5 — Interações: Drag and Drop, Menus, Modais e Calendário
- **Objetivo:** Implementar as interações dinâmicas da interface: movimentação por arrastar e soltar (mouse e touch), ação acessível "Mover para...", busca em tempo real com atalhos de teclado e calendário integrado com popover.
- **Arquivos Previstos:** `js/drag_drop.js`, `js/calendar.js`, `js/modals.js`, `js/search.js`.
- **Atividades:**
  - Implementar eventos de drag and drop nativo para desktop com reordenação visual intra-coluna.
  - Implementar suporte específico para eventos de toque (*touch events*) em smartphones e tablets.
  - Implementar o submenu "Mover para..." no menu `⋮` de cada cartão como via alternativa de movimentação.
  - Implementar busca em tempo real nos campos `titulo` e `descricao` com normalização de acentos e atalhos (`Ctrl + K`, `Esc`).
  - Implementar navegação do calendário entre meses, marcadores de tarefas e popover de foco com scroll suave no Kanban.
- **Dependências:** Conclusão da Fase 4.
- **Critérios e Evidências de Conclusão:**
  1. Testes de movimentação realizados via mouse e via toque (*touch*), diferenciando-os explicitamente.
  2. Teste da movimentação acessível via menu `⋮`.
  3. Teste de busca com atalhos de teclado e teste do popover do calendário acionando foco e scroll no cartão correspondente.

---

### Fase 6 — Relatórios, Backup JSON (Import/Export) e Homologação Final
- **Objetivo:** Implementar o modal de relatórios com métricas dinâmicas em Python, o download de backup JSON versionado e a importação com validação atômica preventiva e confirmação explícita.
- **Arquivos Previstos:** `js/reports.js`, `js/backup.js`.
- **Atividades:**
  - Integrar o modal de relatórios com os cálculos estatísticos do núcleo Python (incluindo filtro por `data_conclusao`).
  - Implementar geração e download do arquivo JSON de backup estruturado (`versao_schema: "1.0"`).
  - Implementar upload e validação de schema antes da substituição de dados.
  - Implementar modal de confirmação com contadores de tarefas (atual vs. nova).
- **Dependências:** Conclusão de todas as fases anteriores.
- **Critérios e Evidências de Conclusão:**
  1. Conferência das métricas do relatório com conjunto de dados controlado.
  2. Validação do schema JSON gerado na exportação.
  3. Teste de importação de arquivo válido com substituição integral e atualização imediata do quadro.
  4. Teste de importação com campos desconhecidos no envelope ou nas tarefas, demonstrando rejeição integral e preservação dos dados existentes.
  5. Teste de cancelamento da importação comprovando ausência de alteração.
  6. Teste de falha de gravação durante a importação comprovando que o estado anterior é preservado e que os novos dados não são apresentados como salvos.

---

## 3. Estratégia de Testes Automatizados e Qualidade

A verificação do projeto baseia-se em três pilares fundamentais:
1. **Aprovação dos Testes:** 100% dos testes da suíte `pytest` devem passar sem falhas ou erros.
2. **Cobertura de Regras Críticas:** 100% das transições de estado, regras de prazos, semântica de `data_atualizacao`, reordenação manual e validações estruturais de JSON devem possuir testes automatizados dedicados.
3. **Cobertura de Código (Proposta para a Etapa 3):** Metas sugeridas de $\ge 90\%$ de linhas e $\ge 85\%$ de ramos em `pytest-cov`, a serem consolidadas no planejamento técnico.

---

## 4. Questões Técnicas Reservadas à Etapa 3 (Planejamento Técnico)

As seguintes definições técnicas não devem ser antecipadas e serão objeto formal da Etapa 3:
1. **Consolidação do Motor WebAssembly:** Comparativo e decisão definitiva entre **Pyodide direto** vs. **PyScript**.
2. **Formato do Identificador:** Avaliação técnica do padrão UUID v4 para o atributo `id`.
3. **Arquitetura de Persistência:** Definição entre persistência em documento JSON único vs. duas fases (shadow key) e especificação técnica dos mecanismos de rollback.
4. **Validação Sequencial de Ordem:** Regras formais para validação de sequências contíguas de `ordem` iniciando em zero ($0, 1, 2, \dots$) por coluna.
5. **Coerência Temporal:** Regras de validação cronológica entre `data_criacao`, `data_atualizacao` e `data_conclusao`.
6. **Estrutura do Domínio Python:** Definição entre classes orientadas a objetos, funções puras ou abordagem híbrida.
7. **Metas Quantitativas do RNF03:** Fixação formal dos índices de cobertura de código no `pytest-cov`.
8. **Ferramentas de Validação:** Escolha dos linters HTML e ferramentas de teste de acessibilidade do frontend.
9. **Arquitetura de Diretórios e Componentes:** Desenho modular de pastas e arquivos prévio à implementação da Fase 1.

---

## 5. Histórico de Alterações do Plano

| Versão | Data | Alterações Registradas | Justificativa |
| :--- | :--- | :--- | :--- |
| **1.0** | 2026-11-01 | Elaboração inicial das 6 fases de implementação. | Estruturar o roteiro de desenvolvimento. |
| **1.1** | 2026-11-01 | Incorporação de critérios objetivos e evidências de conclusão para as fases. | Tornar as entregas de cada fase verificáveis. |
| **1.2** | 2026-11-01 | Ajuste nos testes de persistência da Fase 4 e homologação da Fase 6. | Alinhamento com os fluxos operacionais aprovados. |
| **1.3** | 2026-11-01 | Inclusão de testes específicos de touch na Fase 5 e contraste reposicionado na Fase 3. | Rigor em acessibilidade e responsividade. |
| **1.4** | 2026-11-01 | Detalhamento da acessibilidade na Fase 2 e teste de falha de persistência na importação da Fase 6. | Blindagem de integridade de dados e conformidade WCAG. |
| **1.5** | 2026-11-02 | Inclusão da atividade da saudação "Olá!" na Fase 3, testes de campos desconhecidos e formalização das reservas técnicas da Etapa 3. | Fechamento integral do plano de implementação. |
