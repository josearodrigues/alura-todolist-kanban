# Requisitos do Projeto — To-Do List Kanban

**Especificação funcional:** versão 1.9 (RF01–RF16; RNF01–RNF07).

Este documento preserva os requisitos e decisões aprovados. O estado de implementação e a extensão das evidências de validação da versão 1.0.0 são registrados nas seções finais de `docs/ESTADO-ATUAL.md` e `docs/PLANO-IMPLEMENTACAO.md`. Requisito especificado não significa, por si só, conformidade integral homologada.

## 1. Identidade e Propósito da Aplicação

O projeto consiste no desenvolvimento de uma aplicação web de gerenciamento de tarefas (To-Do List) no formato visual **Kanban**, como parte do Desafio 3 da Imersão Engenharia de Software: Dev na Era da IA (Alura + Google for Startups).

A aplicação tem propósito pedagógico e funcional:
- **Linguagem central:** Python, executado diretamente no navegador do usuário por meio de WebAssembly.
- **Hospedagem:** 100% estática, compatível com **GitHub Pages**.
- **Interface:** Organizada em três colunas de estados (*A Fazer*, *Em Andamento*, *Concluídas*), com movimentação visual por arrastar e soltar (drag and drop) e alternativa acessível via menu contextual.
- **Persistência primária:** Armazenamento local no navegador (`localStorage`), com mecanismo externo de salvaguarda via exportação e importação de arquivos JSON estruturados.

---

## 2. Identidade Visual e Referência Gráfica

A interface adota como base de concepção visual o arquivo:
`docs/design/referencias/todolist-kanban-1.0-mockup.png`

### 2.1 Registro da Exceção de Saudação
> **Decisão Aprovada:** A identidade visual seguirá o mockup oficial, exceto pelo texto da saudação no banner principal, que será substituído por **"Olá!"** (em vez de "Olá, João!"). O arquivo de imagem original permanece preservado intacto como referência histórica de concepção. A versão visual corrigida será produzida durante a Fase 3 de desenvolvimento. A aplicação não implementará rotinas de autenticação, login ou personalização nominal de perfil nesta versão 1.0.

### 2.2 Paleta de Cores e Temas

#### Modo Claro
- Fundo: `#EEF2FF`
- Barra lateral (Sidebar): `#172B4D`
- Superfícies/Cartões: `#FFFFFF`
- Azul principal: `#2563EB`
- Coluna A Fazer: `#3B82F6`
- Coluna Em Andamento: `#F59E0B`
- Coluna Concluídas: `#22C55E`
- Texto principal: `#172554`

#### Modo Escuro
- Fundo: `#0F172A`
- Barra lateral (Sidebar): `#0B1220`
- Superfícies/Cartões: `#1E293B`
- Texto principal: `#E5EDF8`
- Texto secundário: `#94A3B8`
- Bordas: `#334155`

### 2.3 Tipografia e Elementos de Design
- **Fonte principal:** `Inter`, com fontes alternativas da família `sans-serif`.
- **Componentes:** Cartões com cantos arredondados, elevações suaves (sombras discretas), hierarquia tipográfica clara, contraste mínimo de 4.5:1 para texto e respeito à diretiva `prefers-reduced-motion`.

---

## 3. Requisitos Funcionais (RF)

- **RF01 — Visualização do Quadro Kanban:** Exibir 3 colunas (*A Fazer*, *Em Andamento*, *Concluídas*) com contadores dinâmicos de tarefas, cabeçalhos estilizados e botão de criação de tarefa em cada coluna. O banner de boas-vindas exibirá a saudação neutra "Olá!" acompanhada do contador de foco diário.
- **RF02 — Criação de Tarefas:** Permitir criação de tarefas via modal com os campos: `titulo` (obrigatório), `descricao` (opcional), `prioridade` (Baixa, Média, Alta) e `data_limite` (opcional). **Toda tarefa é criada obrigatoriamente no estado `a_fazer`**, sem opção de escolha de estado inicial no formulário. A transição ocorre exclusivamente pela movimentação no Kanban.
- **RF03 — Edição de Tarefas:** Exclusiva pelo menu de opções `⋮` de cada cartão. Permite editar `titulo`, `descricao`, `prioridade` e `data_limite`. Preserva `id`, `data_criacao`, `estado`, `ordem` e `data_conclusao`. Atualiza `data_atualizacao` e o timestamp persistente global apenas após confirmação e salvamento efetivo com alteração real de conteúdo e persistência confirmada com sucesso.
- **RF04 — Movimentação Livre entre Estados:** Movimentação livre entre quaisquer colunas via drag and drop ou pela opção "Mover para..." no menu `⋮`, executando as regras de ciclo de vida de `data_conclusao` e atualizando o timestamp global após persistência confirmada com sucesso.
- **RF05 — Reordenação Manual Intra-Coluna:** Reordenação por drag and drop dentro da coluna. A posição é refletida no campo técnico `ordem`, **sendo estritamente independente da prioridade**. Atualiza metadados conforme as regras da Seção 5 após persistência confirmada com sucesso.
- **RF06 — Exclusão com Confirmação e Consistência:** Acionada pelo menu `⋮`. Modal exibe o título da tarefa e opções de confirmação e cancelamento. A exclusão definitiva é aplicada ao estado em memória e à persistência conforme a estratégia técnica consolidada, garantindo consistência com o timestamp global após persistência confirmada com sucesso.
- **RF07 — Busca em Tempo Real e Gestão de Teclas:** Filtragem instantânea nos campos `titulo` e `descricao` (insensível a maiúsculas e acentos). `Ctrl + K` foca o campo de busca. `Esc` limpa a busca quando em foco e sem modais/popovers abertos; nos demais casos, fecha o componente ativo superior.
- **RF08 — Calendário Integrado:** Visão mensal com navegação e destaque no dia atual. Marcadores visuais nos dias com tarefas: tarefas concluídas identificadas distintamente; tarefas atrasadas mantidas na data de vencimento original. Clique na data abre popover; selecionar a tarefa aciona scroll suave e destaque temporário no Kanban sem filtrar o quadro.
- **RF09 — Resumo do Projeto:** Exibe Total, Concluídas (% com uma casa decimal) e Pendentes (% calculado por diferença em relação a 100,0%). Proteção contra divisão por zero ($0$ tarefas = $0,0\%$).
- **RF10 — Banner Foco de Hoje:** Total de tarefas não concluídas com $\text{data\_limite} \le \text{data\_atual\_local}$.
- **RF11 — Status da Aplicação e Timestamp Persistente:** Exibe o estado do runtime Python (*Inicializando...*, *✓ Carregado*, *⚠ Erro*) e o timestamp da última alteração efetiva de dados, **o qual persiste entre sessões e recargas**.
- **RF12 — Módulo de Relatórios:** Modal com indicadores dinâmicos calculados em Python: total, por estado, por prioridade, atrasadas, vencem hoje, vencem nos próximos 7 dias e tarefas concluídas no período selecionado (utilizando estritamente `data_conclusao` como referência temporal).
- **RF13 — Exportação de Dados:** Download de arquivo JSON estruturado com envelope versionado (`versao_schema: "1.0"`), contendo estritamente os 5 campos do envelope e a lista de tarefas contendo estritamente os 10 atributos aprovados.
- **RF14 — Importação com Substituição Integral e Validação Estrita:** Upload de JSON com validação preventiva integral em memória. Rejeição de campos desconhecidos no envelope e nas tarefas. Apresenta modal de confirmação indicando total de tarefas atuais vs. importadas. Falhas na validação, cancelamento pelo usuário ou falhas durante a gravação na persistência mantêm o estado anterior rigorosamente intacto na memória e na interface.
- **RF15 — Alternância de Tema:** Modos Claro e Escuro com alternador visual e persistência da preferência no navegador.
- **RF16 — Seleção e Exclusão Coletiva de Tarefas:** Permitir selecionar e desselecionar tarefas individualmente nos cartões e globalmente por meio de cabeçalho contextual, abrangendo todas as colunas e estados, inclusive tarefas concluídas. O cabeçalho oferecerá selecionar todas, desselecionar todas, exibir a quantidade selecionada e excluir as selecionadas. O controle de seleção será independente do indicador visual de conclusão e do menu individual de cada cartão. A exclusão exigirá confirmação explícita com a quantidade de tarefas. Cancelar não altera dados nem seleção. A seleção será temporária no frontend e não integrará o `localStorage` nem o backup; só será limpa após persistência bem-sucedida. Em falha de persistência, dados, ordenação, interface e seleção serão preservados.

  **Contrato da operação coletiva:** receber o estado atual e os IDs selecionados; rejeitar lista vazia, IDs duplicados ou qualquer ID inexistente; validar todos os IDs antes de excluir; não permitir exclusão parcial; excluir o conjunto em uma única operação; não modificar a estrutura original recebida; reindexar somente as colunas afetadas, reaproveitando `reindexar_coluna()`; preservar os metadados das tarefas restantes, exceto `ordem`; gerar um único timestamp global; retornar o novo estado e a relação das tarefas excluídas. A implementação deverá analisar `excluir_tarefa()` existente, sem executar exclusões individuais em sequência. Movimentação coletiva, edição coletiva, alteração coletiva de prioridade/vencimento, idempotência adicional e outras operações em lote não fazem parte deste requisito.

---

## 4. Requisitos Não Funcionais (RNF)

- **RNF01 — Execução no GitHub Pages:** Compatibilidade integral com hospedagem estática no GitHub Pages, executando a lógica de negócio em Python diretamente no navegador do usuário por meio de WebAssembly.
- **RNF02 — Lógica Central em Python:** Regras de negócio, cálculos estatísticos, ordenação e validações concentradas em código Python.
- **RNF03 — Qualidade e Cobertura de Testes:** Suíte `pytest` com 100% de aprovação (zero falhas e zero erros), cobertura integral da matriz de regras críticas e as seguintes metas formalizadas na Etapa 3:
  - Cobertura de linhas: `percent_covered` $\ge 90{,}0\%$ (campo do `coverage.json` gerado pelo `coverage.py`).
  - Cobertura de ramos: `percent_branches_covered` $\ge 85{,}0\%$ (campo do `coverage.json`).
  - Procedimento oficial de validação: `pytest && python scripts/verify_coverage.py`.
- **RNF04 — Persistência Segura no Navegador:** Persistência no `localStorage` com garantia de consistência entre dados das tarefas e metadados globais, garantia de reversão do estado em memória e na tela diante de falhas de gravação e tratamento de exceções.
- **RNF05 — Responsividade Adaptativa:** Breakpoints de referência (Desktop $\ge 1200\text{px}$, Tablet $768\text{px}-1199\text{px}$, Mobile $< 768\text{px}$), ajustáveis na validação visual.
- **RNF06 — Acessibilidade Referenciada em WCAG 2.2 Nível AA:** Foco visível evidente, navegação lógica por teclado, estrutura semântica com atributos ARIA, alternativa acessível de movimentação, suporte a `prefers-reduced-motion` e conformidade com os critérios de contraste da WCAG 2.2 (nível AA):
  - Texto normal: razão de contraste mínima de 4,5:1 (critério 1.4.3 — Contrast Minimum).
  - Texto grande ($\ge 18\text{pt}$ ou $\ge 14\text{pt}$ negrito): razão de contraste mínima de 3:1 (critério 1.4.3 — Contrast Minimum).
  - Componentes gráficos relevantes e elementos não textuais: razão de contraste mínima de 3:1 (critério 1.4.11 — Non-text Contrast).
  - Aplicação obrigatória em ambos os temas Claro e Escuro.
- **RNF07 — Feedback de Inicialização:** Indicador de carregamento amigável durante a preparação do ambiente WebAssembly.

---

## 5. Contrato de Dados e Validação Estrutural

O contrato de dados da versão 1.0 é rígido e composto exatamente por 10 atributos para as tarefas e 5 atributos para o envelope de backup.

### 5.1 Atributos da Tarefa
1. `id`: string identificadora única não vazia.
2. `titulo`: string de 3 a 100 caracteres após remoção de espaços nas extremidades (*strip/trim*). Obrigatório.
3. `descricao`: string de até 500 caracteres após remoção de espaços nas extremidades. Opcional (padrão `""`).
4. `estado`: string pertencente ao enum `["a_fazer", "em_andamento", "concluida"]`. Padrão inicial obrigatório `"a_fazer"`.
5. `prioridade`: string pertencente ao enum `["baixa", "media", "alta"]`. Padrão `"media"`.
6. `data_criacao`: string no formato ISO 8601 UTC (`YYYY-MM-DDTHH:MM:SS.sssZ`), gerada automaticamente na criação (imutável).
7. `data_limite`: string no formato estrito `YYYY-MM-DD` ou `null`. Permite datas passadas, presentes ou futuras.
8. `data_atualizacao`: string no formato ISO 8601 UTC, atualizada em mutações efetivas.
9. `data_conclusao`: string no formato ISO 8601 UTC se `estado == "concluida"`, ou estritamente `null` se `estado != "concluida"`.
10. `ordem`: número inteiro não negativo ($\ge 0$), indicando a posição ordinal dentro da coluna.

> **Importante:** Não existe o atributo `responsavel` nem qualquer outro campo adicional nesta versão 1.0. A presença de campos desconhecidos implica rejeição do registro.

### 5.2 Envelope de Exportação e Importação JSON
O documento JSON de backup deve conter estritamente os cinco campos:
- `versao_schema`: string estrita `"1.0"`.
- `aplicacao`: string `"To-Do List Kanban"`.
- `data_exportacao`: string ISO 8601 UTC da geração do arquivo.
- `total_tarefas`: inteiro estritamente igual a `len(tarefas)`.
- `tarefas`: lista contendo os objetos de tarefas íntegros.

> **Política de Rejeição de Campos Desconhecidos:** A presença de atributos desconhecidos no envelope ou em qualquer tarefa provoca a rejeição imediata do arquivo na importação, sem descarte silencioso de campos.

---

## 6. Regras de Negócio e Semântica de Operações

### 6.1 Transições de Estado (6 Cenários Possíveis)
1. `a_fazer` $\rightarrow$ `em_andamento`: define `data_atualizacao = timestamp_utc`, mantém `data_conclusao = null`, atualiza timestamp global.
2. `a_fazer` $\rightarrow$ `concluida`: define `data_atualizacao = timestamp_utc`, define `data_conclusao = timestamp_utc`, atualiza timestamp global.
3. `em_andamento` $\rightarrow$ `a_fazer`: define `data_atualizacao = timestamp_utc`, mantém `data_conclusao = null`, atualiza timestamp global.
4. `em_andamento` $\rightarrow$ `concluida`: define `data_atualizacao = timestamp_utc`, define `data_conclusao = timestamp_utc`, atualiza timestamp global.
5. `concluida` $\rightarrow$ `a_fazer`: define `data_atualizacao = timestamp_utc`, redefine `data_conclusao = null` (reabertura), atualiza timestamp global.
6. `concluida` $\rightarrow$ `em_andamento`: define `data_atualizacao = timestamp_utc`, redefine `data_conclusao = null` (reabertura), atualiza timestamp global.

### 6.2 Reordenação Intra-Coluna e Atualização de Metadados
- **Tarefa diretamente movimentada pelo usuário:** Seu campo `ordem` é alterado para o novo índice e sua `data_atualizacao` é atualizada para o timestamp UTC da operação.
- **Demais tarefas da coluna reindexadas:** Seus campos `ordem` são atualizados para manter a sequência ordinal contígua ($0, 1, 2, \dots$), preservando suas respectivas `data_atualizacao` originais inalteradas.
- **Timestamp global do quadro:** É atualizado para refletir mutação na organização do quadro.
- **Operação sem alteração real (Drop cancelado):** Nenhuma tarefa tem metadados alterados e o timestamp global não é atualizado.
- **Independência da prioridade:** A ordenação é puramente manual, independente da prioridade da tarefa.

### 6.3 Garantia Funcional de Preservação contra Falhas de Persistência
Uma operação de alteração (criação, edição, movimentação, exclusão ou importação) **somente será considerada efetivada após a persistência ser concluída com sucesso**. Em caso de erro na gravação:
1. O estado anterior dos dados em memória é preservado/revertido.
2. A interface reverte qualquer alteração visual efetuada de forma otimista.
3. O usuário recebe notificação clara de falha.

### 6.4 Tratamento de Datas e Limites Temporais
- **Data Local de Referência:** A data atual para cálculo de prazos e atrasos é extraída dos componentes locais do calendário do navegador (`getFullYear()`, `getMonth() + 1`, `getDate()`) gerando a string `YYYY-MM-DD`.
- **Atrasadas:** $\text{data\_limite} < \text{data\_atual\_local} \land \text{estado} \neq \text{"concluida"}$.
- **Vencem Hoje:** $\text{data\_limite} == \text{data\_atual\_local} \land \text{estado} \neq \text{"concluida"}$.
- **Próximos 7 Dias:** $\text{data\_atual\_local} + 1\text{ dia} \le \text{data\_limite} \le \text{data\_atual\_local} + 7\text{ dias} \land \text{estado} \neq \text{"concluida"}$.
- **Tarefas Concluídas:** Associadas à data de vencimento no calendário com marcador visual específico; excluídas dos cálculos de atraso.

### 6.5 Backup Externo e Durabilidade
A exportação de arquivos JSON oferece um mecanismo de backup externo e portabilidade dos dados. Sua durabilidade depende da conservação do arquivo pelo usuário.

---

## 7. Critérios de Aceitação Gerais

1. A aplicação executa no navegador sem requisições a servidores de aplicação backend.
2. Todas as 10 propriedades de uma tarefa persistem no `localStorage` e em arquivos JSON de backup.
3. Transições de estado atualizam `data_conclusao`, `data_atualizacao` e o timestamp global conforme a especificação.
4. A reordenação manual na coluna é preservada entre recargas e não afeta as datas das tarefas apenas reindexadas.
5. Em caso de falha de persistência, nenhum dado em memória ou na interface diverge do armazenamento.
6. A busca filtra dinamicamente sem distinção de acentos ou caixa alta/baixa.
7. O calendário exibe marcadores, permite navegação e foca cartões no quadro sem filtrar as demais tarefas.
8. Os relatórios apresentam métricas exatas calculadas por rotinas Python.
9. A importação substitui dados apenas após validação estrita e confirmação explícita do usuário, rejeitando arquivos com campos desconhecidos.
10. A seleção e exclusão coletiva permitem remover somente as tarefas selecionadas, com confirmação, persistência bem-sucedida e preservação integral do estado anterior em caso de falha.

---

## 8. Histórico de Alterações e Decisões Aprovadas

| Versão | Data | Principais Mudanças / Decisões Aprovadas | Justificativa |
| :--- | :--- | :--- | :--- |
| **1.0** | 2026-11-01 | Levantamento de requisitos inicial com o usuário (método Grill Me). Definição de escopo, colunas e 10 atributos. | Estabelecer o escopo funcional da aplicação. |
| **1.1** | 2026-11-01 | Neutralidade técnica, atalho Esc, calendário com concluídas distintas, validações de modelo. | Refinamento das regras de negócio e de interface. |
| **1.2** | 2026-11-01 | Fixação do estado inicial `a_fazer`, persistência de timestamp global, critérios objetivos de testes. | Fechamento de regras de transição e governança. |
| **1.3** | 2026-11-01 | Precisão conceitual de persistência, matriz explícita de movimentação, teste de touch. | Eliminação de ambiguidades técnicas e de acessibilidade. |
| **1.4** | 2026-11-01 | Neutralidade de WebAssembly no RNF01, regras de importação estrutural e falhas de persistência. | Aprofundamento da integridade de dados e conformidade documental. |
| **1.5** | 2026-11-02 | Semântica estrita de `data_atualizacao`, contrato fechado de 10 atributos (sem `responsavel`), garantia de preservação de estado, saudação neutra "Olá!" e preservação do PNG histórico. | Aprovação final do planejamento funcional consolidado. |
| **1.6** | 2026-11-02 | Atualização do RNF03: metas de cobertura formalizadas na Etapa 3 registradas (`percent_covered` $\ge 90\%$, `percent_branches_covered` $\ge 85\%$, 100% de aprovação, comando oficial `pytest && python scripts/verify_coverage.py`). | Eliminação de referência pendente à Etapa 3 e registro das metas aprovadas. |
| **1.7** | 2026-11-02 | Alinhamento do RNF06 à classificação normativa WCAG 2.2 nível AA: especificação dos limites para texto normal (1.4.3 $\ge 4{,}5:1$), texto grande (1.4.3 $\ge 3:1$) e componentes não textuais relevantes (1.4.11 $\ge 3:1$) em ambos os temas. | Eliminação da definição genérica de contraste de 4.5:1 e alinhamento com as decisões arquiteturais. |
| **1.8** | 2026-11-03 | Inclusão do RF16 para seleção múltipla e exclusão coletiva, com confirmação explícita, seleção temporária e preservação integral dos dados em falhas de persistência. | Formalizar a melhoria de experiência do usuário aprovada para a Fase 7, restrita à exclusão coletiva. |
| **1.9** | 2026-11-03 | Detalhamento do RF16: cabeçalho contextual, seleção global e individual em todas as colunas, separação do indicador de conclusão, contrato atômico de exclusão, validação integral de IDs, preservação de metadados e timestamp único. | Transformar as decisões aprovadas no Grill Me em requisito funcional e contrato verificável antes da implementação. |


---

## 9. Situação dos requisitos na entrega acadêmica v1.0.0

Esta seção não altera os requisitos aprovados nas Seções 3 a 7. Ela registra apenas o alcance da validação realizada para a entrega acadêmica.

| Requisito | Situação documentada no encerramento |
|---|---|
| RF01–RF16 | Regressão funcional aprovada nos cenários exercitados; isso não representa prova exaustiva de todos os estados possíveis. |
| RNF01 | Execução no GitHub Pages confirmada; auditoria integral de tráfego não realizada. |
| RNF02 | Validado funcionalmente nos cenários integrados examinados no navegador, com 30 tarefas. |
| RNF03 | Workflow Python/cobertura aprovado: 68 testes, 95,59% de cobertura de linhas e 92,17% de branches. |
| RNF04 | Rollback validado nos cenários de falha de persistência registrados. |
| RNF05 | Inspeção visual anterior em Desktop, Tablet e Mobile; reteste integrado final não concluído. |
| RNF06 | Validação parcial: HTML, contraste e parte dos testes de teclado/foco; leitor de tela não testado. Não se declara conformidade WCAG 2.2 AA integral. |
| RNF07 | Estados de carregamento e sucesso validados; estado de erro não testado dinamicamente. |

**Critérios específicos ainda não homologados integralmente:** CA5.1 (teste físico por toque) e CA7.12 (avaliação de segurança delimitada, sem equivalência a pentest ou auditoria abrangente).

A decisão de encerramento acadêmico aceita explicitamente essas limitações. Para detalhes, evidências, escopo e histórico, consultar `docs/ESTADO-ATUAL.md`, Seção 22, e `docs/PLANO-IMPLEMENTACAO.md`, Seção 3.1.
