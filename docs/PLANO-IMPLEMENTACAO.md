# Plano de Implementação — To-Do List Kanban

## 1. Visão Geral e Estrutura de Etapas

O desenvolvimento da aplicação é estruturado em etapas controladas, respeitando o princípio pedagógico e de engenharia de software: **Compreender, implementar, validar e explicar.**

- **Etapa 1 — Descoberta e levantamento de requisitos:** [Concluída]
- **Etapa 2 — Planejamento funcional e documentação:** [Concluída]
- **Etapa 3 — Arquitetura e planejamento técnico:** [Concluída e Aprovada]
- **Etapa 4 — Plano de implementação detalhado:** [Pendente]
- **Etapa 5 — Implementação controlada (Fases 1 a 6):** [Pendente de autorização]
- **Etapa 6 — Validação final e homologação:** [Pendente]

---

## 2. Consolidação da Etapa 3 — Arquitetura e Planejamento Técnico

Esta seção registra as sete decisões técnicas formalmente aprovadas que definem a arquitetura da aplicação.

### Decisão Técnica 3.1: Motor WebAssembly
- **Escolha Aprovada:** **Pyodide Direto**, consumido via biblioteca oficial JavaScript `loadPyodide()`.
- **Estratégia de Carregamento de Módulos Próprios:**
  - Carregamento individual assíncrono dos módulos do pacote `todolist` (`__init__.py`, `models.py`, `services.py`, `metrics.py`, `schema.py`) via requisições `fetch()`.
  - Gravação direta dos módulos no virtual filesystem do Pyodide (`pyodide.FS.mkdirTree('/home/pyodide/todolist')` e `pyodide.FS.writeFile(...)`).
  - Configuração do caminho de importação via `sys.path.insert(0, '/home/pyodide')` e importação do pacote via `import todolist`.
- **Justificativa e Impactos:**
  - Controle completo e explícito do ciclo de vida assíncrono de inicialização pelo JavaScript.
  - O código Python permanece 100% puro e desacoplado do DOM, executando exatamente os mesmos arquivos tanto no navegador quanto na suíte local de testes via `pytest`.
  - Elimina etapas manuais de empacotamento zip em tempo de desenvolvimento.

### Decisão Técnica 3.2: Arquitetura de Persistência e Consistência Local
- **Escolha Aprovada:** **Estado Consolidado em Documento JSON Único no `localStorage`**.
- **Mecanismo de Persistência Preventiva:**
  1. O JavaScript mantém em memória o estado confirmado atual.
  2. O domínio Python prepara e valida o novo estado a partir da operação solicitada.
  3. O estado é serializado em um único documento JSON contendo tarefas e o timestamp global da última alteração.
  4. Executa-se a persistência preventiva via `localStorage.setItem("kanban_app_state", payloadJSON)`.
  5. **Confirmação:** Somente após a gravação síncrona bem-sucedida, o novo estado é confirmado na memória da aplicação e os componentes da interface são atualizados.
  6. **Tratamento de Falha (Rollback):** Em caso de exceção de escrita (ex.: `QuotaExceededError`), a operação é abortada, o estado anterior é preservado intacto na memória e na interface, e uma notificação clara de erro é apresentada ao usuário.
- **Limitações Reconhecidas:** Não implementa transações concorrentes entre múltiplas abas abertas simultaneamente nem protege contra descarte físico de dados pelo navegador, mantendo o backup JSON externo (RF13) como mecanismo deliberado de portabilidade e retenção.

### Decisão Técnica 3.3: Estrutura do Domínio Python
- **Escolha Aprovada:** **Abordagem Híbrida (Domínio Rico com `@dataclass` + Fachada Funcional de Serviços)**.
- **Diretrizes de Implementação:**
  - A entidade `Tarefa` utiliza `@dataclass` da biblioteca padrão para representação dos 10 atributos obrigatórios e rotinas de conversão bidirecional (`to_dict` e `from_dict`).
  - Validações explícitas e defensivas são aplicadas no domínio (tamanho de texto, enums de estado e prioridade, formato de datas), sem presumir validação automática por parte do `@dataclass`.
  - Serviços funcionais em `services.py` recebem o estado atual como parâmetro e retornam uma nova estrutura de estado modificada, sem efeitos colaterais sobre o estado confirmado e sem reter estado mutável interno.
  - Suporte à injeção explícita de `id` e `timestamp_utc` para garantir determinismo absoluto nos testes unitários.

### Decisão Técnica 3.4: Identificadores, Ordenação e Invariantes Temporais
- **Identificador (`id`):** Padrão **UUID v4**, gerado pelo módulo nativo `uuid` do Python, em representação canônica textual (36 caracteres minúsculos com hífens). Validação rigorosa de formato, versão e unicidade.
- **Validação Estrita de `ordem`:**
  - Sequência inteira não negativa, única e contígua por coluna, iniciando obrigatoriamente em zero ($0, 1, 2, \dots, n-1$).
  - O validador de importação JSON rejeita arquivos com sequências de ordem inválidas, duplicadas ou com lacunas, sem aplicar correções silenciosas.
- **Invariantes Temporais (Timestamps ISO 8601 UTC com Milissegundos `YYYY-MM-DDTHH:MM:SS.sssZ`):**
  1. `data_atualizacao >= data_criacao`.
  2. Quando `estado == "concluida"`, `data_conclusao` é obrigatória.
  3. `data_conclusao >= data_criacao`.
  4. `data_conclusao <= data_atualizacao`.
  5. Quando `estado != "concluida"`, `data_conclusao == null`.
  6. Ao reabrir uma tarefa (sair de `concluida`), limpar `data_conclusao = null` e atualizar `data_atualizacao`.
  7. Ao concluir uma tarefa (entrar em `concluida`), registrar `data_conclusao = timestamp_utc` e atualizar `data_atualizacao`.
  8. Alterações de conteúdo em tarefas já concluídas atualizam `data_atualizacao`, preservando a `data_conclusao` original intacta.

### Decisão Técnica 3.5: Estratégia de Testes Automatizados e Metas do RNF03
- **Critérios Formais de Aprovação:**
  - **100% de Aprovação:** Zero falhas e zero erros na suíte `pytest`.
  - **Cobertura de Linhas:** $\ge 90,0\%$ de declarações (`percent_covered` no `coverage.json`).
  - **Cobertura de Ramos:** $\ge 85,0\%$ de branches (`percent_branches_covered` no `coverage.json`).
- **Configuração no `pyproject.toml`:** Centralização das opções do pytest e coverage sem limites arbitrários sobre métricas combinadas:
  ```toml
  [tool.pytest.ini_options]
  testpaths = ["tests"]
  pythonpath = ["src"]
  addopts = "--cov=src/todolist --cov-branch --cov-report=term-missing --cov-report=json:coverage.json"
  ```
- **Procedimento Oficial de Validação da Fase 1:**
  ```bash
  pytest && python scripts/verify_coverage.py
  ```
  O script `scripts/verify_coverage.py` analisa o `coverage.json` gerado, exige que o arquivo exista e esteja íntegro, valida individualmente as duas metas percentuais e encerra com código de erro caso qualquer limite não seja atingido.

### Decisão Técnica 3.6: Validação de Frontend e Acessibilidade (WCAG 2.2 AA)
- **Validação de HTML:** Uso do Nu HTML Checker (v.Nu) em execução local, exigindo zero erros de validação estrutural e semântica.
- **Validação Matemática de Contraste:** Implementação do script `scripts/check_contrast.py` para calcular e auditar a razão de contraste (fórmula de luminância relativa da WCAG 2.2) para todas as combinações de cores dos temas Claro e Escuro:
  - Texto normal: $\ge 4.5:1$.
  - Texto grande / componentes visuais e indicadores essenciais: $\ge 3.0:1$ (WCAG 1.4.11).
- **Checklist Manual Estruturado de Acessibilidade:**
  - Navegação integral via teclado (Tab, Shift+Tab, Enter, Espaço, Esc).
  - Foco visível inequívoco e focus trap ativo em todos os modais.
  - Fechamento contextual de menus e popovers.
  - Não dependência exclusiva de cores para transmissão de estado ou prioridade.
  - Respeito à preferência do usuário por `prefers-reduced-motion`.
- **Interação Unificada via Pointer Events:** O módulo `js/drag_drop.js` adota a API de **Pointer Events** (`pointerdown`, `pointermove`, `pointerup`, `pointercancel`) para unificar o tratamento de mouse, toque em telas sensíveis e caneta, complementado pela via acessível de movimentação no menu `⋮` ("Mover para...").

### Decisão Técnica 3.7: Arquitetura Modular e Estrutura de Diretórios
- **Estrutura Completa da Raiz do Projeto (`./`):**

```text
./                               # Raiz do projeto
│
├── pyproject.toml               # Configuração do pytest, coverage e dependências de desenvolvimento
├── index.html                   # Estrutura semântica e montagem da aplicação
│
├── css/                         # Folhas de estilo modulares
│   ├── variables.css            # Tokens de design e variáveis dos temas Claro e Escuro
│   ├── base.css                 # Reset, tipografia Inter e acessibilidade estrutural
│   ├── layout.css               # Estrutura dos 3 painéis (Sidebar, Kanban, Widgets) e responsividade
│   ├── kanban.css               # Colunas, cartões de tarefas e estados visuais de interação
│   └── components.css           # Modais, formulários, popovers, badges e botões
│
├── js/                          # Camada de orquestração do frontend (JavaScript ES6+)
│   ├── app.js                   # Inicialização geral e listeners globais
│   ├── pyodide_bridge.js        # Carregamento do Pyodide via CDN, fetch dos módulos para o FS e ponte FFI
│   ├── storage.js               # Persistência preventiva no localStorage com confirmação pós-gravação
│   ├── kanban_ui.js             # Renderização e atualização dos cartões e colunas no DOM
│   ├── drag_drop.js             # Gestão de arraste unificada via Pointer Events (mouse, touch, caneta)
│   ├── calendar_ui.js           # Renderização do calendário, marcadores e popover de foco
│   ├── reports_ui.js            # Renderização do modal de relatórios com métricas dinâmicas
│   └── backup_ui.js             # Interface para exportação e importação de arquivo JSON
│
├── src/                         # Núcleo de Domínio e Regras de Negócio em Python Puro
│   └── todolist/                # Pacote principal da aplicação
│       ├── __init__.py          # Exportações do pacote
│       ├── models.py            # Entidade Tarefa (@dataclass), validações e conversões (to_dict/from_dict)
│       ├── services.py          # Operações de negócio (criar, editar, mover, reordenar, excluir)
│       ├── metrics.py           # Cálculos estatísticos, prazos e atrasos dinâmicos
│       └── schema.py            # Validação estrita do envelope e tarefas para import/export
│
├── tests/                       # Suíte de testes automatizados (pytest)
│   ├── __init__.py
│   ├── test_models.py           # Testes de limites de atributos, enums e invariantes da Tarefa
│   ├── test_services.py         # Testes das 6 transições de estado, reordenação e metadados
│   ├── test_metrics.py          # Testes determinísticos de prazos, atrasos e relatórios
│   └── test_schema.py           # Testes de validação de schema JSON (rejeição de campos desconhecidos)
│
├── scripts/                     # Scripts de suporte e validação local
│   ├── check_contrast.py        # Validação matemática de contraste de cores (WCAG 2.2 AA)
│   └── verify_coverage.py       # Validação estrita de percent_covered (>=90%) e percent_branches_covered (>=85%)
│
└── docs/                        # Tríade documental de governança
    ├── REQUISITOS.md            # Catálogo de requisitos e regras de negócio
    ├── PLANO-IMPLEMENTACAO.md   # Roteiro de fases e decisões técnicas consolidadas
    ├── ESTADO-ATUAL.md          # Registro operacional de continuidade e mapeamento do repositório
    └── design/
        └── referencias/
            └── todolist-kanban-1.0-mockup.png  # Referência histórica de concepção
```

---

## 3. Fases de Implementação Controlada

A execução da Etapa 5 será dividida em seis fases pequenas, sequenciais e verificáveis:

### Fase 1 — Fundação do Domínio Python e Testes Automatizados
- **Objetivo:** Construir o pacote `todolist` com regras de negócio, manipulação de estado, cálculos estatísticos e validação estrita de schema JSON em Python puro.
- **Arquivos Previstos:** `pyproject.toml`, `src/todolist/`, `tests/` e `scripts/verify_coverage.py`.
- **Atividades:**
  - Configurar dependências de desenvolvimento e regras de cobertura no `pyproject.toml`.
  - Implementar a entidade `Tarefa` com `@dataclass` e validações explícitas de atributos em `models.py`.
  - Implementar operações em `services.py` com injeção de identificadores/timestamps e reordenação contígua.
  - Implementar a operação de **edição de tarefas**, preservando os metadados não editáveis (`id`, `data_criacao`, `estado`, `ordem`, `data_conclusao`) e atualizando `data_atualizacao` apenas quando houver alteração real confirmada e persistência bem-sucedida.
  - Implementar testes unitários correspondentes à operação de edição em `test_services.py`, cobrindo: edição com alteração real, edição sem alteração (no-op), e tentativa de alteração de campos não editáveis.
  - Implementar cálculos estatísticos em `metrics.py` com referências temporais estritas.
  - Implementar validação preventiva de schema JSON em `schema.py` com rejeição de campos desconhecidos.
  - Implementar a suíte completa de testes no diretório `tests/`.
  - Implementar o script `scripts/verify_coverage.py`.
- **Dependências:** Ambiente Python local com `pytest` e `pytest-cov`.
- **Critérios e Evidências de Conclusão:** Execução bem-sucedida do comando oficial:
  ```bash
  pytest && python scripts/verify_coverage.py
  ```
  Evidenciando 100% dos testes aprovados, cobertura de linhas $\ge 90,0\%$ e cobertura de ramos $\ge 85,0\%$.

---

### Fase 2 — Estrutura HTML Semântica e Acessibilidade Estrutural
- **Objetivo:** Desenvolver a marcação semântica em `index.html`, contemplando os 3 painéis, modais, formulários acessíveis e saudação neutra aprovada.
- **Arquivos Previstos:** `index.html`.
- **Atividades:**
  - Estruturar a barra lateral (Sidebar), cabeçalho (`Ctrl + K`, alternador de tema), área central com saudação **"Olá!"** e as 3 colunas do Kanban.
  - Estruturar a barra de widgets (Calendário, Resumo do Projeto, Status do Runtime).
  - Estruturar modais para Nova Tarefa/Editar Tarefa, Confirmação de Exclusão, Relatórios e Importar/Exportar.
  - Inserir semântica acessível: atributos ARIA, labels descritivos, focus trap e navegação lógica por teclado.
- **Dependências:** Conclusão da Fase 1.
- **Critérios e Evidências de Conclusão:**
  1. Relatório do Nu HTML Checker local sem erros de estrutura ou semântica.
  2. Roteiro de testes de acessibilidade via teclado documentado, contemplando:
     - Tabulação (`Tab` e `Shift+Tab`) e ativação (`Enter`, `Espaço`) em todos os controles interativos.
     - Fechamento via `Esc` em modais, menus e formulários.
     - Entrada, permanência e saída de modais com gerenciamento de foco; focus trap ativo enquanto o modal estiver aberto.
     - Navegação por teclado em menus contextuais e formulários de criação e edição.
     - Indicador de foco visível e inequívoco em todos os elementos focáveis.
     - Nomes acessíveis em botões e campos; estados não comunicados exclusivamente por cor.

---

### Fase 3 — Design System, Estilos Responsivos e Validação Visual (CSS)
- **Objetivo:** Implementar o design system moderno em CSS modular, temas Claro e Escuro, adaptação fluida para Desktop, Tablet e Mobile, e produção do mockup visual com a saudação atualizada.
- **Arquivos Previstos:** `css/variables.css`, `css/base.css`, `css/layout.css`, `css/kanban.css`, `css/components.css` e `scripts/check_contrast.py`.
- **Atividades:**
  - Definir variáveis CSS nativas para temas Claro e Escuro conforme paleta aprovada.
  - Estilizar painéis, cartões com cantos arredondados, elevações suaves, badges de prioridade e barras de progresso.
  - Implementar regras de mídia responsivas (Desktop $\ge 1200\text{px}$, Tablet $768\text{px}-1199\text{px}$, Mobile $< 768\text{px}$).
  - Implementar e executar o script `scripts/check_contrast.py` para auditoria matemática de contraste.
  - Produzir a versão visual de referência com a saudação corrigida para "Olá!", mantendo o arquivo PNG original intacto como referência histórica.
  - Aplicar suporte a `prefers-reduced-motion`.
- **Dependências:** Conclusão da Fase 2.
- **Critérios e Evidências de Conclusão:**
  1. Relatório gerado por `check_contrast.py` demonstrando, para ambos os temas Claro e Escuro:
     - Texto normal: razão de contraste $\ge 4{,}5:1$ (WCAG 1.4.3 — nível AA).
     - Texto grande ($\ge 18\text{pt}$ ou $\ge 14\text{pt}$ negrito): razão $\ge 3{,}0:1$ (WCAG 1.4.3 — nível AA).
     - Componentes gráficos e indicadores de estado essenciais: razão $\ge 3{,}0:1$ (WCAG 1.4.11 — nível AA).
  2. Evidência documental de inspeção visual confirmando integridade do layout em Desktop, Tablet e Mobile nos dois temas.

---

### Fase 4 — Integração WebAssembly e Persistência Segura com Garantia de Rollback
- **Objetivo:** Inicializar o runtime WebAssembly via Pyodide, carregar os módulos Python no virtual filesystem, estabelecer a ponte bidirecional JS $\leftrightarrow$ Python e implementar o motor de persistência consistente no `localStorage`.
- **Arquivos Previstos:** `js/pyodide_bridge.js`, `js/storage.js`, `js/app.js`.
- **Atividades:**
  - Inicializar o Pyodide via CDN e carregar os módulos Python no virtual filesystem pela seguinte sequência obrigatória:
    1. Requisição `fetch()` individual de cada arquivo do pacote `src/todolist/` (`__init__.py`, `models.py`, `services.py`, `metrics.py`, `schema.py`).
    2. Gravação de cada arquivo no virtual filesystem via `pyodide.FS.mkdirTree('/home/pyodide/todolist')` e `pyodide.FS.writeFile(...)`.
    3. Configuração do caminho de importação via `sys.path.insert(0, '/home/pyodide')` executado no contexto Python do Pyodide.
    4. Importação do pacote via `import todolist` e verificação de que as funções públicas estão disponíveis e operacionais.
  - Implementar a sincronização bidirecional entre interface e núcleo Python.
  - Implementar a persistência preventiva em documento JSON único no `localStorage` com controle de confirmação pós-gravação.
  - Implementar o tratamento de falhas de gravação (reversão do estado em memória e na tela).
- **Dependências:** Conclusão das Fases 1, 2 e 3.
- **Critérios e Evidências de Conclusão:**
  1. Evidência de que a sequência de carregamento Pyodide foi concluída com sucesso: o indicador de status transiciona visualmente para `✓ Carregado` e as funções do pacote `todolist` respondem conforme esperado a partir do JavaScript.
  2. Testes de ciclo de vida e persistência executados separadamente para criação, edição, movimentação e exclusão, com recarga da página (`F5`) comprovando retenção íntegra e atualização sincronizada do timestamp.
  3. Teste de falha de gravação simulada comprovando preservação do estado anterior e notificação de erro ao usuário.

---

### Fase 5 — Interações: Drag and Drop, Menus, Modais e Calendário
- **Objetivo:** Implementar as interações dinâmicas da interface: movimentação unificada por arrastar e soltar (Pointer Events), ação acessível "Mover para...", busca em tempo real com atalhos de teclado e calendário integrado com popover.
- **Arquivos Previstos:** `js/drag_drop.js`, `js/kanban_ui.js`, `js/calendar_ui.js`.
- **Atividades:**
  - Implementar eventos de drag and drop via Pointer Events unificados para mouse, toque e caneta.
  - Implementar o submenu "Mover para..." no menu `⋮` de cada cartão como via alternativa de movimentação.
  - Implementar busca em tempo real nos campos `titulo` e `descricao` com normalização de acentos e atalhos (`Ctrl + K`, `Esc`).
  - Implementar navegação do calendário entre meses, marcadores de tarefas e popover de foco com scroll suave no Kanban.
  - Integrar menus contextuais e formulários de cartão com as operações de criação, edição, movimentação e exclusão do domínio Python.
- **Dependências:** Conclusão da Fase 4.
- **Critérios e Evidências de Conclusão:**
  1. Testes de movimentação realizados via mouse e via toque (*touch*), diferenciando-os explicitamente.
  2. Teste da movimentação acessível via menu `⋮`.
  3. Teste de busca com atalhos de teclado e teste do popover do calendário acionando foco e scroll no cartão correspondente.
  4. Validação das regras de metadados de reordenação manual dentro da coluna:
     - `data_atualizacao` é atualizada apenas na tarefa diretamente movida; tarefas apenas reindexadas para contiguidade mantêm suas datas originais inalteradas.
     - O timestamp global da última alteração é atualizado somente quando houver reordenação efetiva.
     - Operações sem mudança real de posição (drop na mesma posição) não disparam nenhuma atualização de metadados.

---

### Fase 6 — Relatórios, Backup JSON (Import/Export) e Homologação Final
- **Objetivo:** Implementar o modal de relatórios com métricas dinâmicas em Python, o download de backup JSON versionado e a importação com validação atômica preventiva e confirmação explícita.
- **Arquivos Previstos:** `js/reports_ui.js`, `js/backup_ui.js`.
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
  7. Regressão integrada verificando os requisitos funcionais (RF01–RF15) e não funcionais (RNF01–RNF07) conforme a matriz de rastreabilidade, sem substituir os testes específicos das fases anteriores.

---

## 4. Histórico de Alterações do Plano

| Versão | Data | Alterações Registradas | Justificativa |
| :--- | :--- | :--- | :--- |
| **1.0** | 2026-11-01 | Elaboração inicial das 6 fases de implementação. | Estruturar o roteiro de desenvolvimento. |
| **1.1** | 2026-11-01 | Incorporação de critérios objetivos e evidências de conclusão para as fases. | Tornar as entregas de cada fase verificáveis. |
| **1.2** | 2026-11-01 | Ajuste nos testes de persistência da Fase 4 e homologação da Fase 6. | Alinhamento com os fluxos operacionais aprovados. |
| **1.3** | 2026-11-01 | Inclusão de testes específicos de touch na Fase 5 e contraste reposicionado na Fase 3. | Rigor em acessibilidade e responsividade. |
| **1.4** | 2026-11-01 | Detalhamento da acessibilidade na Fase 2 e teste de falha de persistência na importação da Fase 6. | Blindagem de integridade de dados e conformidade WCAG. |
| **1.5** | 2026-11-02 | Inclusão da atividade da saudação "Olá!" na Fase 3, testes de campos desconhecidos e formalização das reservas técnicas da Etapa 3. | Fechamento integral do plano de implementação funcional. |
| **1.6** | 2026-11-02 | Consolidação integral da Etapa 3: Decisões 3.1 a 3.7 aprovadas, arquitetura modular `src/todolist/`, `pyproject.toml`, Pointer Events e procedimento oficial de validação da Fase 1. | Conclusão e aprovação formal da Etapa 3 (Arquitetura e Planejamento Técnico). |
| **1.7** | 2026-11-02 | Seis ajustes pontuais à Etapa 4: operação de edição e testes em `services.py` (Fase 1); critérios de acessibilidade modal e foco (Fase 2); três limites de contraste explícitos WCAG 2.2 AA (Fase 3); sequência de quatro etapas de carregamento Pyodide com critério de conclusão (Fase 4); regras de metadados de reordenação e integração menus/formulários (Fase 5); regressão integrada RF01–RF15 e RNF01–RNF07 (Fase 6). | Fechamento das lacunas identificadas na revisão técnica da Etapa 4. |
