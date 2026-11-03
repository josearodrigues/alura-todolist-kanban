# Plano de Implementação — To-Do List Kanban

## 1. Visão Geral e Estrutura de Etapas

O desenvolvimento da aplicação é estruturado em etapas controladas, respeitando o princípio pedagógico e de engenharia de software: **Compreender, implementar, validar e explicar.**

- **Etapa 1 — Descoberta e levantamento de requisitos:** [Concluída]
- **Etapa 2 — Planejamento funcional e documentação:** [Concluída]
- **Etapa 3 — Arquitetura e planejamento técnico:** [Concluída e Aprovada]
- **Etapa 4 — Plano de implementação detalhado:** [Concluída e Aprovada — versão 2.1]
- **Etapa 5 — Implementação controlada (Fases 1 a 7):** [Fases 1 a 6 implementadas; Fase 5 mantém pendência de homologação por toque em CA5.1; Fase 6 aguarda validação da mensagem amigável de rejeição de JSON inválido, CA6.8–CA6.10; Fase 7 planejada e aprovada, implementação não iniciada]
- **Etapa 6 — Validação final e homologação:** [Pendente — regressão integrada RF01–RF16 e RNF01–RNF07 após a implementação e homologação das fases previstas]

---

## 2. Revisão corretiva e validação visual — Fase 3 (2026-11-03)

A interface foi refinada conforme o mockup oficial, incluindo cabeçalho, navegação, cartões, calendário, resumo, status demonstrativo e rodapé. As telas secundárias permanecem mocks estáticos; suas funcionalidades serão implementadas nas fases previstas. Na branch `revisao-visual-d83bbee`, foi adicionada navegação lateral recolhível para telas de até 960 px, com fechamento por `Esc`, clique no fundo e seleção de seção, além de gerenciamento de foco. O ícone `⋮` foi ajustado visualmente, mas o menu contextual continua desativado.

A inspeção manual foi aprovada pelo usuário nos três breakpoints — Desktop, Tablet (1024 × 768) e Mobile (390 × 844) — nos temas Claro e Escuro. O usuário também confirmou o comportamento com `prefers-reduced-motion` ativo. O workflow `41553398236` aprovou 25 combinações de contraste, sem reprovações, e o Nu HTML Checker sem erros ou avisos. Portanto, os critérios visuais CA3.1–CA3.3 e de movimento reduzido CA3.5 estão aprovados conforme as evidências disponíveis; CA3.4 possui evidência automatizada. Isso não representa validação funcional das telas demonstrativas.

## 3. Consolidação da Etapa 3 — Arquitetura e Planejamento Técnico

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
  - Texto normal: $\ge 4{,}5:1$ (WCAG 2.2, critério 1.4.3 — Contrast Minimum).
  - Texto grande ($\ge 18\text{pt}$ ou $\ge 14\text{pt}$ negrito): $\ge 3{,}0:1$ (WCAG 2.2, critério 1.4.3 — Contrast Minimum).
  - Componentes gráficos e indicadores não textuais relevantes: $\ge 3{,}0:1$ (WCAG 2.2, critério 1.4.11 — Non-text Contrast).
- **Checklist Manual Estruturado de Acessibilidade:**
  - Navegação integral via teclado (Tab, Shift+Tab, Enter, Espaço, Esc).
  - Foco visível inequívoco e gerenciamento adequado de foco, com focus trap quando aplicável.
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

A execução da Etapa 5 será dividida em sete fases pequenas, sequenciais e verificáveis:

### Fase 1 — Fundação do Domínio Python e Testes Automatizados
- **Objetivo:** Construir o pacote `todolist` com regras de negócio, manipulação de estado, cálculos estatísticos e validação estrita de schema JSON em Python puro.
- **Arquivos Previstos:** `pyproject.toml`, `src/todolist/`, `tests/` e `scripts/verify_coverage.py`.
- **Atividades:**
  - Configurar dependências de desenvolvimento e regras de cobertura no `pyproject.toml`.
  - Implementar a entidade `Tarefa` com `@dataclass` e validações explícitas de atributos em `models.py`.
  - Implementar operações em `services.py` com injeção de identificadores/timestamps e reordenação contígua.
  - Implementar a operação de **edição de tarefas** no domínio Python, com o seguinte fluxo arquitetural:
    1. **Preparação e validação do estado candidato (Python):** o serviço recebe o estado atual e os novos valores; valida os campos; se houver alteração efetiva de conteúdo, gera o estado candidato com `data_atualizacao = timestamp_utc` injetado; em caso de operação sem alteração real (no-op), devolve o estado inalterado sem gerar novo timestamp.
    2. **Tentativa de persistência preventiva (JavaScript):** a camada de storage JavaScript recebe o estado candidato preparado pelo domínio e tenta a gravação síncrona no `localStorage`; em caso de falha de gravação (ex.: cota excedida), a camada JS preserva o estado anterior intacto e notifica o usuário, sem confirmar a alteração.
    3. **Confirmação pós-gravação (JavaScript / UI):** somente após a gravação bem-sucedida pelo JavaScript, o novo estado é confirmado na memória da aplicação e os componentes da interface são atualizados.
    - Metadados não editáveis preservados pelo domínio Python em todas as circunstâncias: `id`, `data_criacao`, `estado`, `ordem`, `data_conclusao`.
  - Implementar testes unitários correspondentes à operação de edição em `test_services.py`, cobrindo: edição com alteração real, edição sem alteração (no-op), e tentativa de alteração de campos não editáveis.
  - Implementar cálculos estatísticos em `metrics.py` com referências temporais estritas.
  - Implementar validação preventiva de schema JSON em `schema.py` com rejeição de campos desconhecidos.
  - Implementar a suíte completa de testes no diretório `tests/`.
  - Implementar o script `scripts/verify_coverage.py`.
- **Dependências:** Ambiente Python local com `pytest` e `pytest-cov`.
- **Revisão corretiva:** Foram incluídas validações defensivas de enums, unicidade de ID na criação, proteção dos campos imutáveis da edição, verificação explícita do timestamp global nas seis transições e validação dos limites do período de conclusão. A aprovação final permanece condicionada à execução local do procedimento oficial após estas alterações.
- **Critérios e Evidências de Conclusão:** Execução bem-sucedida do comando oficial:
  ```bash
  pytest && python scripts/verify_coverage.py
  ```
  Evidenciando 100% dos testes aprovados, cobertura de linhas $\ge 90{,}0\%$ e cobertura de ramos $\ge 85{,}0\%$.

#### Critérios de Aceite — Fase 1

| # | Critério | Evidência |
|---|----------|-----------|
| CA1.1 | Entidade `Tarefa` implementada com os 10 atributos obrigatórios, validações defensivas e conversões `to_dict`/`from_dict` (RF02–RF06, RF13, RF14). | Testes automatizados em `test_models.py` aprovados. |
| CA1.2 | Todas as 6 transições de estado implementadas corretamente, atualizando `data_conclusao`, `data_atualizacao` e o timestamp global conforme especificado na Seção 6.1 do REQUISITOS.md. | Testes de transição em `test_services.py` aprovados. |
| CA1.3 | Operação de edição preserva `id`, `data_criacao`, `estado`, `ordem` e `data_conclusao`; gera `data_atualizacao` no candidato somente em alteração real; no-op não produz novo timestamp. | Testes de edição em `test_services.py` aprovados (3 casos: alteração real, no-op, campos não editáveis). |
| CA1.4 | Reordenação intra-coluna: apenas a tarefa diretamente movida tem `data_atualizacao` atualizada; tarefas reindexadas preservam datas originais; no-op não atualiza metadados (RF05, Seção 6.2). | Testes de reordenação em `test_services.py` aprovados. |
| CA1.5 | Validação preventiva de schema JSON rejeita campos desconhecidos no envelope e nas tarefas sem normalização silenciosa (RF14). | Testes em `test_schema.py` aprovados. |
| CA1.6 | Cálculos estatísticos em `metrics.py` determinísticos via injeção de referência temporal: tarefas atrasadas, vencem hoje, vencem nos próximos 7 dias e concluídas no período por `data_conclusao` (RF09, RF10, RF12). | Testes em `test_metrics.py` aprovados. |
| CA1.7 | 100% dos testes aprovados, `percent_covered` $\ge 90{,}0\%$ e `percent_branches_covered` $\ge 85{,}0\%$ (RNF03). | Saída de `pytest && python scripts/verify_coverage.py` sem erros. |

---

### Fase 2 — Estrutura HTML Semântica e Acessibilidade Estrutural
- **Objetivo:** Desenvolver a marcação semântica em `index.html`, contemplando os 3 painéis, modais, formulários acessíveis e saudação neutra aprovada.
- **Arquivos Previstos:** `index.html`.
- **Atividades:**
  - Estruturar a barra lateral (Sidebar), cabeçalho (`Ctrl + K`, alternador de tema), área central com saudação **"Olá!"** e as 3 colunas do Kanban.
  - Estruturar a barra de widgets (Calendário, Resumo do Projeto, Status do Runtime).
  - Estruturar modais para Nova Tarefa/Editar Tarefa, Confirmação de Exclusão, Relatórios e Importar/Exportar.
  - Inserir semântica acessível: atributos ARIA, labels descritivos, gerenciamento adequado de foco (focus trap quando aplicável) e navegação lógica por teclado.
- **Dependências:** Conclusão da Fase 1.
- **Critérios e Evidências de Conclusão:**
  1. Relatório do Nu HTML Checker local sem erros de estrutura ou semântica.
  2. Roteiro de testes de acessibilidade via teclado documentado, contemplando:
     - Tabulação (`Tab` e `Shift+Tab`) e ativação (`Enter`, `Espaço`) em todos os controles interativos.
     - Fechamento via `Esc` em modais, menus e formulários.
     - Entrada, permanência e saída de modais com gerenciamento adequado de foco; focus trap quando aplicável.
     - Navegação por teclado em menus contextuais e formulários de criação e edição.
     - Indicador de foco visível e inequívoco em todos os elementos focáveis.
     - Nomes acessíveis em botões e campos; estados não comunicados exclusivamente por cor.

#### Registro da verificação manual — 2026-11-03

Checklist executado pelo usuário na aplicação local, com resultados informados nesta sessão:

| Verificação | Resultado | Observação |
|---|---|---|
| `Tab` e `Shift + Tab` | Aprovado | Navegação nos controles testados. |
| `Enter` e `Espaço` | Aprovado | Ativação dos controles apropriados testados. |
| `Ctrl + K` | Aprovado | Foco direcionado ao campo de busca. |
| Diálogo Nova Tarefa: foco inicial, contenção e restauração | Aprovado | Comportamentos confirmados pelo usuário nesse diálogo. |
| `Esc` no diálogo Nova Tarefa | Aprovado | O diálogo foi fechado. |
| `Esc` no menu contextual | Pendente | Menu contextual indisponível/desativado. |
| Navegação por teclado no menu contextual | Pendente | Controle `⋮` desativado; não foi possível abrir o menu. |
| Rótulos e identificação visual dos controles | Sem problema visual observado | Não equivale a teste com leitor de tela. |
| Nomes acessíveis com leitor de tela | Não testado | Exige validação específica com tecnologia assistiva. |

**Resultado da Fase 2:** validação manual parcial. Os resultados aprovados acima não cobrem todos os critérios CA2.3–CA2.6. O menu contextual também apresenta divergência visual em relação ao mockup (desenho do ícone `⋮`), registrada para correção na etapa apropriada, sem alteração nesta validação.

#### Critérios de Aceite — Fase 2

| # | Critério | Evidência |
|---|----------|-----------|
| CA2.1 | Estrutura semântica dos 3 painéis (Sidebar, Kanban com 3 colunas e Área de Widgets), cabeçalhos, contadores e botão de criação de tarefa em cada coluna implementados em HTML (RF01). | Inspeção da árvore DOM e verificação visual dos painéis, cabeçalhos, contadores iniciais e dos três botões de criação. |
| CA2.2 | HTML validado pelo Nu HTML Checker sem erros de estrutura ou semântica (RNF06). | Relatório do Nu HTML Checker sem erros. |
| CA2.3 | Controles operáveis via `Tab`, `Shift+Tab`, `Enter` e `Espaço`; `Ctrl + K` foca a busca; `Esc` limpa a busca quando ela está em foco e nenhum modal/popover está aberto, e nos demais casos fecha o componente ativo superior (RF07, RNF06). | Checklist manual documentando navegação por teclado, foco da busca e comportamento contextual de `Esc`. |
| CA2.4 | Modais com gerenciamento adequado de foco e focus trap quando aplicável; entrada, permanência e saída documentadas (RNF06). | Checklist manual documentado. |
| CA2.5 | Menus contextuais e formulários de criação/edição navegáveis por teclado (RF02, RF03, RF04, RF06, RNF06). | Checklist manual documentado. |
| CA2.6 | Foco visível e inequívoco em todos os elementos focáveis; nomes acessíveis em botões e campos; estados não comunicados exclusivamente por cor (RNF06). | Inspeção visual e checklist manual documentados. |

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
     - Texto normal: razão de contraste $\ge 4{,}5:1$ (WCAG 2.2, critério 1.4.3 — Contrast Minimum).
     - Texto grande ($\ge 18\text{pt}$ ou $\ge 14\text{pt}$ negrito): razão $\ge 3{,}0:1$ (WCAG 2.2, critério 1.4.3 — Contrast Minimum).
     - Componentes gráficos e indicadores não textuais relevantes: razão $\ge 3{,}0:1$ (WCAG 2.2, critério 1.4.11 — Non-text Contrast).
  2. Evidência documental de inspeção visual confirmando integridade do layout em Desktop, Tablet e Mobile nos dois temas.

#### Critérios de Aceite — Fase 3

| # | Critério | Evidência |
|---|----------|-----------|
| CA3.1 | Interface implementada conforme o mockup de referência e as decisões aprovadas; saudação exibida como \"Olá!\"; arquivo PNG original preservado intacto (Seção 2.1 REQUISITOS.md). | Inspeção visual da aplicação e verificação do arquivo PNG. |
| CA3.2 | Temas Claro e Escuro funcionais com paleta aprovada e variáveis CSS nativas (RF15, Seção 2.2 REQUISITOS.md). | Inspeção visual nos dois temas. |
| CA3.3 | Responsividade verificada nos três breakpoints: Desktop $\ge 1200\text{px}$, Tablet $768\text{px}$–$1199\text{px}$, Mobile $< 768\text{px}$ (RNF05). | Evidência documental de inspeção visual. |
| CA3.4 | Texto normal com razão $\ge 4{,}5:1$ (WCAG 2.2, 1.4.3), texto grande com razão $\ge 3{,}0:1$ (WCAG 2.2, 1.4.3) e componentes não textuais relevantes com razão $\ge 3{,}0:1$ (WCAG 2.2, 1.4.11) nos dois temas (RNF06). | Relatório gerado por `check_contrast.py`. |
| CA3.5 | Suporte a `prefers-reduced-motion` aplicado nos elementos com animação (RNF06). | Inspeção visual com preferência ativa. |

> **Registro de execução — 2026-11-02:** folhas CSS modulares, alternância de tema, layout responsivo, badge de prioridade, barra de progresso e suporte a movimento reduzido implementados. `scripts/check_contrast.py` foi criado. A auditoria confirmatória pelo workflow deve ser consultada após cada alteração visual relevante.

> **Registro de execução — 2026-11-03:** interface e telas demonstrativas estáticas refinadas; navegação lateral mobile recolhível implementada e testada pelo usuário nos temas Claro e Escuro. O usuário aprovou a inspeção visual em Desktop, Tablet (1024 × 768) e Mobile (390 × 844), nos dois temas, e confirmou o teste com `prefers-reduced-motion` ativo. Workflow `41553398236`: 25 combinações de contraste aprovadas, zero reprovações e Nu HTML Checker sem erros/avisos. O ícone `⋮` foi corrigido visualmente, mas não há confirmação isolada de sua aparência; o menu contextual permanece desativado. A Fase 2 ainda possui checklist manual parcial pendente.

---

### Fase 4 — Integração WebAssembly e Persistência Segura com Garantia de Rollback
- **Estado:** Implementação registrada na branch `fase-4-pyodide-persistencia`; validação funcional da API concluída em 2026-11-03. O usuário executou criação, edição, movimentação e exclusão, conferiu persistência e timestamp, confirmou o indicador `✓ Carregado` e verificou recuperação após recarga para as quatro operações. Falhas simuladas nas quatro operações comprovaram rollback. No GitHub Pages, o usuário confirmou o carregamento. Na auditoria limitada ao filtro Fetch/XHR durante a carga, foi observada uma requisição ao CDN jsDelivr (`pyodide-lock.json`, HTTP 200), sem chamadas a APIs de backend nessa amostra. CA4.1 permanece parcialmente verificado, pois essa observação não representa auditoria completa de todo o tráfego de rede. A interface continua demonstrativa; sua integração funcional é atividade da Fase 5.
- **Runtime selecionado:** Pyodide 314.0.7 (Python 3.14.2), versão oficial disponível pelo CDN.
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
  1. Console confirmou Pyodide 314.0.7, carregamento dos cinco módulos e importação de `todolist`; o usuário confirmou visualmente o indicador `✓ Carregado` (CA4.2).
  2. Criação, edição, movimentação e exclusão foram executadas pela API JS/Python, com persistência e timestamp conferidos no `localStorage`. Recuperação após recarga confirmada para as quatro operações; as verificações após edição, movimentação e exclusão foram apresentadas pelo usuário no console nesta sessão.
  3. Falha de gravação simulada nas quatro operações: em todas, memória e armazenamento preservaram o estado anterior. A notificação de erro foi observada no teste de criação.
  4. Execução no GitHub Pages confirmada pelo usuário. No filtro Fetch/XHR, durante o carregamento, foi observada uma requisição ao CDN jsDelivr para `pyodide-lock.json` (HTTP 200), sem chamadas a APIs de backend nessa amostra. A auditoria é limitada ao filtro e ao período observado; CA4.1 permanece parcialmente verificado.

#### Critérios de Aceite — Fase 4

| # | Critério | Evidência |
|---|----------|-----------|
| CA4.1 | Aplicação publicada e executada com sucesso no GitHub Pages, integralmente estática via Pyodide e sem dependência de backend convencional (RNF01). | Acesso à URL publicada no GitHub Pages, verificação do carregamento e uso da aplicação e auditoria de rede comprovando ausência de requisições a APIs de backend. |
| CA4.2 | Pyodide inicializado com sucesso via CDN; indicador de status transiciona para `✓ Carregado` (RF11, RNF07). | Inspeção visual do indicador de status. |
| CA4.3 | Todos os arquivos do pacote `todolist` gravados no virtual filesystem; `sys.path` configurado; `import todolist` bem-sucedido; funções públicas respondendo a partir do JavaScript (Decisão 3.1). | Evidência em console/log de inicialização. |
| CA4.4 | Comunicação bidirecional JS $\leftrightarrow$ Python funcional para as operações de criação, edição, movimentação e exclusão (RNF02). | Testes de ciclo de vida por operação com recarga de página (`F5`). |
| CA4.5 | Persistência preventiva: gravação síncrona no `localStorage` antes da confirmação em memória e atualização da interface; timestamp global persistente entre sessões (RF11, RNF04, Decisão 3.2). | Teste com recarga de página comprovando retenção íntegra. |
| CA4.6 | Falha de gravação (ex.: `QuotaExceededError`) preserva estado anterior em memória e na interface; usuário recebe notificação clara (RNF04, Seção 6.3 REQUISITOS.md). | Teste de falha de gravação simulada. |

---

### Fase 5 — Interações: Drag and Drop, Menus, Modais e Calendário
- **Estado da implementação e validação (2026-11-03):** implementação registrada na branch `fase-5-interacoes`. Módulos `js/kanban_ui.js`, `js/drag_drop.js` e `js/calendar_ui.js` criados; `js/app.js`, `js/pyodide_bridge.js`, `index.html` e `css/kanban.css` integrados/atualizados. Formulários e menus conectados à API `window.kanbanApp`; busca com normalização de acentos; calendário mensal com marcadores e popover; métricas de resumo e Foco de Hoje consultam o domínio Python. Workflow `db37ac91`: Nu HTML Checker sem erros/avisos e auditoria de contraste aprovada. Validação manual: CA5.2, CA5.3 (incluindo conclusão/reabertura e metadados), CA5.4, CA5.6 (incluindo Foco de Hoje e quadro vazio) e CA5.7 aprovados nos cenários exercitados; CA5.5 aprovado nos cenários funcionais exercitados. Após teste com 10 tarefas no mesmo dia e observação de ocupação da tela, foi implementada rolagem vertical interna no popover; validação visual com listas extensas e em viewport móvel permanece pendente. CA5.1 permanece parcial: mouse e alternativa pelo menu aprovados; teste por toque não realizado e caneta também não testada. Também foram validados o fechamento do menu contextual ao cancelar/fechar diálogos, as datas relativas/destaque de tarefas vencidas e a remoção da mensagem transitória de carregamento após recarga; o indicador do Pyodide permaneceu funcional. A limitação genérica de navegador móvel antigo está documentada, sem causa comprovada. A implementação da Fase 5 está concluída; o aceite integral aguarda o teste de toque exigido por CA5.1.
- **Objetivo:** Implementar as interações dinâmicas da interface: movimentação unificada por arrastar e soltar (Pointer Events), ação acessível "Mover para...", busca em tempo real com atalhos de teclado e calendário integrado com popover.
- **Arquivos Previstos:** `js/drag_drop.js`, `js/kanban_ui.js`, `js/calendar_ui.js`.
- **Atividades:**
  - Implementar eventos de drag and drop via Pointer Events unificados para mouse, toque e caneta.
  - Implementar o submenu "Mover para..." no menu `⋮` de cada cartão como via alternativa de movimentação.
  - Implementar busca em tempo real nos campos `titulo` e `descricao` com normalização de acentos e atalhos (`Ctrl + K`, `Esc`).
  - Implementar navegação do calendário entre meses, marcadores de tarefas e popover de foco com scroll suave no Kanban.
  - Integrar menus contextuais e formulários de cartão com as operações de criação, edição, movimentação e exclusão do domínio Python.
- **Dependências:** Conclusão da Fase 4.

- **Registro de validação manual parcial (2026-11-03):**
  - **CA5.1:** drag and drop com mouse e alternativa `Mover para...` aprovados. Toque e caneta não testados por indisponibilidade de dispositivos.
  - **CA5.2:** criação, edição de título/descrição/prioridade/vencimento, exclusão, movimentação por menu e mouse e atualização dos contadores confirmadas. Correção posterior fecha menus e submenus contextuais ao fechar/cancelar diálogos; usuário confirmou.
  - **CA5.3:** reordenação intra-coluna, preservação dos metadados de tarefas reindexadas e no-op aprovados. Movimentação entre estados, conclusão e reabertura também aprovadas: conclusão define `data_conclusao` com o timestamp da operação e reabertura a limpa.
  - **CA5.4:** busca em tempo real, limpeza, normalização de acentos e caixa, `Ctrl + K` e `Esc` confirmados. Os atalhos já haviam sido aprovados na Fase 2; não foram repetidos nesta rodada.
  - **CA5.5:** navegação mensal, popover exibindo três tarefas no mesmo dia e foco/destaque temporário no cartão correspondente aprovados. Após observação com 10 tarefas no mesmo dia, implementada rolagem vertical interna na lista do popover; validação visual com mais de 10 itens e em viewport móvel pendente.
  - **CA5.6:** total, contagens, percentuais, Foco de Hoje pela data local e cenário sem tarefas (sem divisão por zero) aprovados.
  - **CA5.7:** persistência da preferência de tema após recarga aprovada.
  - **Datas e vencimentos:** rótulos relativos para datas anteriores, ontem, hoje e amanhã; data de conclusão e destaque de tarefas pendentes vencidas confirmados. Ajuste da etiqueta “Vencida” para 14 px e `white-space: nowrap` confirmado visualmente após commit `a4e466d`.
  - **Compatibilidade:** falha de inicialização observada em navegador móvel antigo; causa não comprovada. Registrar genericamente no README e no estado atual, sem identificar aparelho/versão.
  - **Carregamento:** mensagem transitória “Carregando tarefas...” e referências associadas removidas de `index.html`, `js/kanban_ui.js` e `js/app.js`. Verificação estática e teste manual após recarga confirmaram ausência da mensagem, funcionamento do quadro sem deslocamento vertical e preservação do indicador de status do Pyodide e de `aria-busy`.
- **Critérios e Evidências de Conclusão:**
  1. Testes de movimentação realizados via mouse e via toque (*touch*), diferenciando-os explicitamente.
  2. Teste da movimentação acessível via menu `⋮`.
  3. Teste de busca com atalhos de teclado e teste do popover do calendário acionando foco e scroll no cartão correspondente.
  4. Validação das regras de metadados de reordenação manual dentro da coluna:
     - `data_atualizacao` é atualizada apenas na tarefa diretamente movida; tarefas apenas reindexadas para contiguidade mantêm suas datas originais inalteradas.
     - O timestamp global da última alteração é atualizado somente quando houver reordenação efetiva.
     - Operações sem mudança real de posição (drop na mesma posição) não disparam nenhuma atualização de metadados.

#### Critérios de Aceite — Fase 5

| # | Critério | Evidência |
|---|----------|-----------|
| CA5.1 | Drag and drop via Pointer Events funcional em mouse e toque, diferenciando explicitamente os dois dispositivos; via acessível \"Mover para...\" disponível no menu `⋮` (RF04, RF05, RNF06). | Testes manuais documentados por dispositivo. |
| CA5.2 | Criação, edição, exclusão e movimentação funcionais, integradas ao domínio Python via ponte JS $\leftrightarrow$ Python; contadores das colunas atualizados corretamente após criação, movimentação e exclusão (RF01–RF06). | Testes de ciclo de vida por operação e verificação dos contadores antes e depois de cada operação. |
| CA5.3 | Reordenação respeita regras aprovadas: `data_atualizacao` atualizada apenas na tarefa diretamente movida; tarefas reindexadas preservam datas originais; timestamp global atualizado somente em reordenação efetiva; no-op não dispara metadados (RF05, Seção 6.2 REQUISITOS.md). | Testes manuais documentados com verificação de metadados. |
| CA5.4 | Busca em tempo real com normalização de acentos e atalhos `Ctrl + K` e `Esc` funcionais (RF07). | Teste manual com casos de acentuação e atalhos documentados. |
| CA5.5 | Calendário com marcadores, navegação mensal e popover que aciona scroll suave e destaque no Kanban sem filtrar o quadro (RF08). | Teste manual documentado. |
| CA5.6 | Resumo do Projeto com totais, percentuais e proteção contra divisão por zero (RF09); Foco de Hoje calculado corretamente pela data local do navegador (RF10). | Verificação manual com conjunto controlado de dados. |
| CA5.7 | Preferência de tema persistente entre sessões (RF15). | Teste com recarga de página. |

---

### Fase 6 — Relatórios, Backup JSON (Import/Export) e Homologação Final
- **Objetivo:** Implementar o modal de relatórios com métricas dinâmicas em Python, o download de backup JSON versionado e a importação com validação atômica preventiva e confirmação explícita.
- **Arquivos previstos e implementados:** `js/reports_ui.js`, `js/backup_ui.js`, ajustes em `js/app.js`, `js/pyodide_bridge.js`, `index.html`, `css/components.css`, `src/todolist/schema.py`, `src/todolist/__init__.py` e `tests/test_schema.py`; workflows de validação ampliados.
- **Atividades:**
  - Integrar o modal de relatórios com os cálculos estatísticos do núcleo Python (incluindo filtro por `data_conclusao`).
  - Implementar geração e download do arquivo JSON de backup estruturado (`versao_schema: "1.0"`).
  - Implementar upload e validação de schema antes da substituição de dados.
  - Implementar modal de confirmação com contadores de tarefas (atual vs. nova).
- **Dependências:** Núcleo Python, ponte Pyodide, persistência preventiva e componentes de interface das fases anteriores.
- **Critérios e Evidências de Conclusão:**
  1. Conferência das métricas do relatório com conjunto de dados controlado.
  2. Validação do schema JSON gerado na exportação.
  3. Teste de importação de arquivo válido com substituição integral e atualização imediata do quadro.
  4. Teste de importação com campos desconhecidos no envelope ou nas tarefas, demonstrando rejeição integral e preservação dos dados existentes.
  5. Teste de cancelamento da importação comprovando ausência de alteração.
  6. Teste de falha de gravação durante a importação comprovando que o estado anterior é preservado e que os novos dados não são apresentados como salvos.
  7. Regressão integrada verificando os requisitos funcionais (RF01–RF15) e não funcionais (RNF01–RNF07) conforme a matriz de rastreabilidade, sem substituir os testes específicos das fases anteriores.
- **Implementação registrada:** modal de relatórios com filtro de conclusão; exportação JSON; importação estrita com rejeição de chaves duplicadas/constantes inválidas; modal de confirmação com contadores; timestamp global gerado no momento da confirmação; substituição pelo fluxo transacional existente.
- **Estado de validação:** CA6.1–CA6.7 aprovados. Foi implementado um ajuste de usabilidade para apresentar mensagem amigável na rejeição de JSON inválido, mantendo o detalhe técnico no console; validação manual no navegador pendente. CA6.8–CA6.10 permanecem pendentes. A execução local de 60 testes e as coberturas de 96,10% (linhas) e 92,72% (branches) foi informada pelo usuário; a conferência dos workflows ainda é necessária. Não declarar a Fase 6 homologada antes da conclusão dos critérios pendentes.

#### Critérios de Aceite — Fase 6

| # | Critério | Evidência |
|---|----------|-----------|
| CA6.1 | Métricas do modal de relatórios calculadas corretamente pelo núcleo Python: total, por estado, por prioridade, atrasadas, vencem hoje, vencem nos próximos 7 dias e concluídas no período por `data_conclusao` (RF12). | Conferência com conjunto de dados controlado. |
| CA6.2 | Exportação gera arquivo JSON com envelope de exatamente 5 campos e lista de tarefas com exatamente 10 atributos cada (RF13, Seção 5.1–5.2 REQUISITOS.md). | Validação do schema do arquivo gerado. |
| CA6.3 | Importação com arquivo válido substitui dados integralmente, exibe modal de confirmação com contadores e atualiza o quadro imediatamente após confirmação (RF14). | Teste manual documentado. |
| CA6.4 | Arquivo com versão de schema incompatível é rejeitado integralmente e o estado anterior permanece intacto. | Teste manual com versão não suportada. |
| CA6.5 | JSON com chave malformada é rejeitado integralmente e o estado anterior permanece intacto. | Teste manual com sintaxe inválida na chave. |
| CA6.6 | JSON com valor malformado é rejeitado integralmente e o estado anterior permanece intacto. | Teste manual com valor inválido; confirmação da preservação dos dados. |
| CA6.7 | Cancelamento da importação não altera os dados existentes. | Teste manual documentado; aprovado pelo usuário. |
| CA6.8 | Falha de gravação durante a importação preserva o estado anterior em memória, na interface e no armazenamento (RNF04). | Teste de falha simulada, com verificação de consistência. |
| CA6.9 | Regressão integrada de RF01–RF15 e RNF01–RNF07 executada e aprovada conforme a matriz de rastreabilidade. | Registro dos resultados da regressão por requisito. |
| CA6.10 | Workflows GitHub associados à branch da Fase 6 executados e aprovados. | Evidência das execuções no GitHub Actions. |

**Qualidade automatizada:** o procedimento local `pytest && python scripts/verify_coverage.py` foi informado com 60 testes aprovados, 96,10% de cobertura de linhas e 92,72% de branches. Esses números são registrados como evidência automatizada já obtida, sem substituir CA6.8–CA6.10.

---

### Fase 7 — Seleção e Exclusão Coletiva de Tarefas

- **Objetivo:** permitir que o usuário selecione múltiplas tarefas em diferentes colunas e as exclua em uma única operação, com confirmação explícita e garantia de integridade dos dados.
- **Escopo aprovado:** seleção/deseleção individual; seleção simultânea entre colunas e estados; indicação da quantidade selecionada; ação para limpar a seleção; confirmação com a quantidade de tarefas; exclusão coletiva. O checkbox será um controle real de seleção e permanecerá independente do indicador visual (tick) de conclusão.
- **Fora do escopo:** movimentação coletiva, edição coletiva, alteração coletiva de prioridade ou vencimento e qualquer outra operação em lote.
- **Arquivos previstos:** a definir após inspeção da implementação existente. Áreas potencialmente envolvidas: `js/kanban_ui.js`, `js/app.js`, `js/storage.js`, `src/todolist/services.py`, CSS e testes. A definição final deverá respeitar a arquitetura atual e evitar alterações desnecessárias.
- **Atividades:**
  1. Implementar seleção e desseleção de tarefas na interface, inclusive em cartões de tarefas concluídas.
  2. Manter a seleção temporária no frontend, sem persistir esse estado no backup ou no `localStorage`.
  3. Exibir a quantidade selecionada e disponibilizar ação para limpar a seleção.
  4. Apresentar confirmação explícita com a quantidade de tarefas selecionadas; cancelar não altera dados nem seleção.
  5. Implementar no domínio Python uma operação única de exclusão para o conjunto de IDs selecionados, validando os identificadores e recalculando a ordenação das colunas afetadas.
  6. Integrar a operação à persistência preventiva existente: somente confirmar a exclusão e limpar a seleção após gravação bem-sucedida.
  7. Em falha de persistência, preservar integralmente o estado anterior em memória e na interface, mantendo a seleção para nova tentativa.
  8. Atualizar os cartões e contadores após sucesso, preservando os metadados das tarefas restantes, exceto os índices `ordem` necessários à contiguidade.
  9. Implementar testes automatizados e validar teclado, foco, feedback e responsividade.
- **Dependências:** conclusão da integração de persistência da Fase 4 e componentes de interface das Fases 2 e 5. A homologação da Fase 6 permanece uma pendência independente e não será considerada concluída por causa da Fase 7.
- **Critérios de Aceite:**

| # | Critério | Evidência |
|---|----------|-----------|
| CA7.1 | Selecionar e desselecionar individualmente tarefas por controle próprio, sem confundir seleção com conclusão. | Teste manual dos estados selecionado/não selecionado e concluído/pendente. |
| CA7.2 | Selecionar simultaneamente tarefas de colunas e estados diferentes. | Cenário controlado com tarefas nas três colunas. |
| CA7.3 | Exibir a quantidade correta de tarefas selecionadas e permitir limpar a seleção sem alterar os dados. | Conferência da contagem e teste da ação limpar seleção. |
| CA7.4 | Exibir confirmação com a quantidade correta; cancelar preserva dados e seleção. | Testes manuais de confirmação e cancelamento. |
| CA7.5 | Excluir somente as tarefas selecionadas em uma única operação e atualizar cartões e contadores. | Teste funcional com tarefas selecionadas e não selecionadas em todas as colunas. |
| CA7.6 | Persistir a exclusão antes de confirmar a atualização da interface; em falha, preservar dados e seleção. | Teste de falha simulada de persistência e verificação de memória, armazenamento e interface. |
| CA7.7 | Manter a ordenação contígua nas colunas afetadas e preservar os metadados das tarefas restantes, exceto `ordem`. | Inspeção do estado persistido antes e depois da exclusão coletiva. |
| CA7.8 | Testes automatizados aprovados e metas do RNF03 mantidas. | Saída de `pytest && python scripts/verify_coverage.py`. |
| CA7.9 | Operação acessível por teclado, com foco e feedback adequados, e interface responsiva. | Checklist manual de teclado/acessibilidade e inspeção nos breakpoints Desktop, Tablet e Mobile. |

## 5. Matriz de Rastreabilidade de Requisitos

Esta seção relaciona cada requisito aprovado à fase responsável pela sua implementação, ao critério de aceite correspondente e à evidência prevista para validação.

### 5.1 Requisitos Funcionais (RF01–RF16)

| Req. | Descrição Resumida | Fase | Critério de Aceite | Evidência |
|------|--------------------|------|--------------------|-----------|
| RF01 | Quadro Kanban com 3 colunas, contadores dinâmicos, cabeçalhos estilizados e saudação \\"Olá!\\" | Fase 2, Fase 3, Fase 5 | CA2.1, CA3.1, CA5.2 | Inspeção DOM/visual dos 3 painéis e cabeçalhos; inspeção do banner; testes funcionais do quadro e dos contadores após criação, movimentação e exclusão. |
| RF02 | Criação de tarefa via modal; estado inicial obrigatório `a_fazer` | Fase 1, Fase 2, Fase 5 | CA1.1, CA2.5, CA5.2 | Testes automatizados em `test_models.py`; checklist de teclado; teste funcional no navegador. |
| RF03 | Edição de tarefa via menu `⋮`; preservação de metadados não editáveis | Fase 1, Fase 2, Fase 5 | CA1.3, CA2.5, CA5.2 | Testes automatizados de edição em `test_services.py`; checklist de teclado; teste funcional. |
| RF04 | Movimentação livre entre colunas via drag and drop ou menu acessível, com ciclo de vida de conclusão/reabertura | Fase 1, Fase 2, Fase 5 | CA1.2, CA2.5, CA5.1, CA5.2 | Testes das seis transições e metadados; checklist de acessibilidade; testes de movimentação por mouse, toque e menu. |
| RF05 | Reordenação manual intra-coluna; metadados conforme regras de Seção 6.2 | Fase 1, Fase 5 | CA1.4, CA5.1, CA5.3 | Testes automatizados em `test_services.py`; testes manuais com verificação de metadados. |
| RF06 | Exclusão com confirmação via modal; consistência após persistência | Fase 2, Fase 5 | CA2.4, CA2.5, CA5.2 | Checklist de modais/teclado; teste de ciclo de vida com persistência e rollback. |
| RF07 | Busca em tempo real, `Ctrl + K`, `Esc` contextual | Fase 2, Fase 5 | CA2.3, CA5.4 | Checklist de teclado; teste manual com acentuação e atalhos. |
| RF08 | Calendário com marcadores, navegação e popover com scroll/destaque | Fase 5 | CA5.5 | Teste manual documentado com navegação e scroll suave. |
| RF09 | Resumo do Projeto com percentuais e proteção contra divisão por zero | Fase 1, Fase 5 | CA1.6, CA5.6 | Testes automatizados em `test_metrics.py`; verificação com dados controlados. |
| RF10 | Banner Foco de Hoje baseado na data local do navegador | Fase 1, Fase 5 | CA1.6, CA5.6 | Testes automatizados em `test_metrics.py`; verificação manual com dados controlados. |
| RF11 | Status do runtime e timestamp global persistente entre sessões | Fase 4 | CA4.2, CA4.5 | Inspeção visual do indicador; teste com recarga de página (`F5`). |
| RF12 | Relatórios com métricas dinâmicas calculadas em Python | Fase 1, Fase 6 | CA1.6, CA6.1 | Testes automatizados em `test_metrics.py`; conferência com dados controlados no modal. |
| RF13 | Exportação JSON com envelope e tarefas conforme contrato de dados | Fase 1, Fase 6 | CA1.1, CA6.2 | Testes automatizados de schema; validação estrutural do arquivo exportado. |
| RF14 | Importação com validação estrita, confirmação e rollback em falhas | Fase 1, Fase 6 | CA1.5, CA6.3, CA6.4, CA6.5, CA6.6 | Testes em `test_schema.py`; testes manuais por cenário de importação. |
| RF15 | Alternância de tema claro/escuro com persistência da preferência | Fase 3, Fase 5 | CA3.2, CA5.7 | Inspeção visual nos dois temas; teste com recarga de página. |
| RF16 | Seleção múltipla e exclusão coletiva com confirmação, persistência segura e rollback | Fase 7 | CA7.1–CA7.9 | Testes automatizados do domínio; testes manuais de seleção, cancelamento, exclusão, ordenação e falha de persistência; checklist de acessibilidade. |

### 5.2 Requisitos Não Funcionais (RNF01–RNF07)

| Req. | Descrição Resumida | Fase | Critério de Aceite | Evidência |
|------|--------------------|------|--------------------|-----------|
| RNF01 | Execução 100% estática, compatível com GitHub Pages | Fase 4 | CA4.1 | Aplicação acessada e executada na URL publicada do GitHub Pages; auditoria de rede sem requisições a APIs de backend. |
| RNF02 | Lógica central em Python (regras, cálculos, validações) | Fase 1, Fase 4 | CA1.1–CA1.6, CA4.4 | Testes automatizados no pytest; teste funcional da ponte JS/Python. |
| RNF03 | 100% de aprovação dos testes; `percent_covered` $\ge 90\%$; `percent_branches_covered` $\ge 85\%$ | Fase 1, Fase 6 | CA1.7, CA6.8 | Saída oficial de `pytest && python scripts/verify_coverage.py`. |
| RNF04 | Persistência segura com reversão em falha de gravação | Fase 4, Fase 6 | CA4.5, CA4.6, CA6.6 | Testes de falha simulada (`QuotaExceededError`); verificação de consistência. |
| RNF05 | Responsividade nos três breakpoints (Desktop, Tablet, Mobile) | Fase 3 | CA3.3 | Evidência documental de inspeção visual nos três breakpoints. |
| RNF06 | Acessibilidade WCAG 2.2 AA: foco, teclado, ARIA, contraste, `prefers-reduced-motion` | Fase 2, Fase 3 | CA2.2–CA2.6, CA3.4, CA3.5 | Relatório Nu HTML Checker; relatório `check_contrast.py`; checklist de teclado. |
| RNF07 | Indicador amigável de carregamento do ambiente WebAssembly | Fase 4 | CA4.2 | Inspeção visual do indicador de status (*Inicializando...* $\rightarrow$ *✓ Carregado*). |

---

## 6. Histórico de Alterações do Plano

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
| **1.8** | 2026-11-02 | Consolidação documental da Etapa 4: matriz de rastreabilidade RF01–RF15 e RNF01–RNF07 (Seção 5); critérios de aceite verificáveis nas seis fases (CA1.x–CA6.x); correção do focus trap para "quando aplicável" (Fase 2); detalhamento do fluxo de edição em três etapas (preparação, persistência, confirmação) na Fase 1; referências WCAG corrigidas (1.4.3 e 1.4.11 com nomes normativos) em toda a Seção 3.6 e Fases 3; atualização do RNF03 em REQUISITOS.md; atualização de estado e rastreabilidade em ESTADO-ATUAL.md. | Consolidação da Etapa 4 para revisão e aprovação. |
| **1.9** | 2026-11-02 | Correção das 4 inconsistências da revisão: alinhamento do focus trap na Decisão 3.6 para "quando aplicável"; atribuição estrita da persistência ao JavaScript na Fase 1; criação dos critérios CA2.1 (painéis e contadores) e CA4.1 (execução estática sem backend); remapeamento completo da Matriz de Rastreabilidade para RF01–RF15 e RNF01–RNF07. | Fechamento rigoroso das pendências apontadas na revisão técnica pós-commit 03eae77. |
| **2.0** | 2026-11-02 | Refinamento dos critérios RF01 e RNF01: validação dos contadores após operações do quadro e comprovação de execução efetiva na hospedagem publicada do GitHub Pages. | Tornar as evidências de aceite diretamente verificáveis e alinhadas aos requisitos aprovados. |
| **2.1** | 2026-11-02 | Ajustes finais de rastreabilidade e critérios: CA2.1 explicita botão de criação em cada coluna; CA2.3 detalha o comportamento contextual de `Esc`; RF04 passa a referenciar as seis transições de estado e seus testes em CA1.2. | Fechar lacunas entre os requisitos aprovados, critérios de aceite e evidências previstas. |
| **2.2** | 2026-11-03 | Registro da conclusão da inspeção visual da Fase 3 nos três breakpoints e nos dois temas, incluindo o teste manual de `prefers-reduced-motion` e a correção da navegação mobile. | Atualizar os critérios de aceite com as evidências efetivamente confirmadas pelo usuário. |
| **2.3** | 2026-11-03 | Atualização do estado de validação da Fase 4 com os testes executados pelo usuário: ciclo de vida das quatro operações, persistência e falhas simuladas com rollback. | Evitar repetição de testes já realizados e manter explícitas as evidências e pendências reais da homologação. |
| **2.4** | 2026-11-03 | Registro da recuperação após recarga para criação, edição, movimentação e exclusão; confirmação do indicador Pyodide carregado e execução no GitHub Pages. Auditoria de rede do CA4.1 permanece pendente. | Atualizar os critérios da Fase 4 com as confirmações apresentadas pelo usuário, sem repetir testes já realizados. |
| **2.5** | 2026-11-03 | Consolidação da validação funcional da API da Fase 4; registro da auditoria Fetch/XHR no GitHub Pages (requisição ao CDN jsDelivr, HTTP 200, sem chamada a backend na amostra); explicitação de que a interface demonstrativa será integrada na Fase 5. | Distinguir validação do motor Python da integração da interface e registrar o alcance real da auditoria de rede. |
| **2.6** | 2026-11-03 | Registro da validação manual parcial da Fase 5: operações e contadores, busca/atalhos, calendário/popover, resumo, tema e metadados de reordenação/no-op; explicitação das verificações ainda pendentes em CA5.1, CA5.3 e CA5.6. | Preservar evidências confirmadas, evitar repetição de testes e manter o estado real dos critérios de aceite. |
| **2.7** | 2026-11-03 | Atualização das evidências da Fase 5: conclusão/reabertura e metadados (CA5.3), Foco de Hoje e divisão por zero (CA5.6), correção do menu contextual, datas relativas e destaque de vencidas; registro das pendências de toque/caneta e compatibilidade móvel; implementação de rolagem interna no popover após avaliação de usabilidade; remoção da mensagem de carregamento implementada e validada. | Manter o plano alinhado aos testes efetivamente confirmados e às pendências reais. |
| **2.8** | 2026-11-03 | Inclusão da Fase 7 — Seleção e Exclusão Coletiva, com escopo restrito à exclusão em lote, requisito RF16, critérios CA7.1–CA7.9, confirmação explícita, persistência preventiva e preservação da seleção em caso de falha. | Incorporar a melhoria de experiência do usuário aprovada, mantendo a homologação da Fase 6 como atividade independente. |
| **3.0** | 2026-11-03 | Correção da rastreabilidade da Fase 6: CA6.7 registrado como aprovado; ajuste de usabilidade separado para mensagens de rejeição de JSON inválido, com detalhes técnicos restritos ao console. | Refletir corretamente a pendência de interface sem reabrir o critério de cancelamento. |
| **2.9** | 2026-11-03 | Reorganização dos critérios de homologação da Fase 6 para refletir os cenários executados: CA6.4–CA6.6 para rejeição de arquivos inválidos, CA6.7 para cancelamento, CA6.8 para falha de persistência, CA6.9 para regressão integrada e CA6.10 para workflows. | Corrigir a rastreabilidade entre os testes efetivamente executados, os critérios de aceite e as pendências restantes.
