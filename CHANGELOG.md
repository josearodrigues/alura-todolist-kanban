# Changelog

## [Não lançado] — 2026-11-03

### Encerramento acadêmico
- Concluídas as sete fases de implementação do To-Do List Kanban, com os critérios funcionais aprovados nos cenários executados e regressão RF01–RF16 registrada.
- Workflows HTML/contraste e Python/cobertura aprovados na branch de trabalho; suíte Python registrada com 65 testes aprovados, 95,83% de cobertura de linhas e 92,54% de branches.
- RNF02, RNF03 e RNF04 validados no escopo documentado; RNF07 validado para carregamento e sucesso.
- Limitações remanescentes documentadas: auditoria completa de rede (RNF01), reteste visual integrado (RNF05), leitor de tela (RNF06), estado de erro do indicador (RNF07), teste físico de toque (CA5.1) e avaliação de segurança delimitada (CA7.12).
- O encerramento acadêmico não representa homologação integral de todos os requisitos não funcionais. Não foram adicionadas funcionalidades nem alterado código da aplicação nesta consolidação.
Este arquivo registra decisões aprovadas, alterações implementadas e resultados validados em ordem cronológica inversa. Cada entrada distingue planejamento, implementação e validação efetivamente realizados.

## [Não lançado] — 2026-11-03

- RNF02: centralizada em Python a preparação da ordenação do quadro por coluna/campo `ordem` e a identificação de tarefas vencidas; a interface consome os resultados via Pyodide. Os 68 testes Python foram aprovados (95,59% de cobertura de linhas e 92,17% de branches; workflow `41753321406`) e o workflow de sintaxe JavaScript foi aprovado (`41753384763`). Na validação integrada posterior no navegador, os 30 cartões corresponderam à sequência de estado/ordem dos dados e a indicação de vencimento foi consistente em 30/30 tarefas (14 vencidas). RNF02 validado funcionalmente nos cenários examinados; permanecem as pendências gerais da Etapa 6.
- RNF05/CA5.1: inspeção CSS identificou breakpoints (1280, 960 e 767 px), navegação lateral recolhível, colunas empilhadas, banner de vencidas fluido e regras para ponteiro coarse. A evidência estática não substitui reteste visual nem homologação física por toque; ambos permanecem pendentes.


### Revisão técnica de RNF02 e RNF07

- RNF02: inspeção confirmou o núcleo de operações, validações, métricas, relatórios e schema no Python via Pyodide. Identificada duplicação da regra de tarefa vencida em JavaScript e Python; ordenações na interface precisam ser distinguidas entre regra de domínio e apresentação. Requisito permanece parcial, sem alteração de código.
- RNF07: usuário confirmou no navegador `Inicializando...` durante o carregamento e `✓ Carregado` após a inicialização do Pyodide. Validado funcionalmente para carregamento e sucesso; o estado de erro não foi testado.


### Atualização do encerramento da Fase 7

- Fase 7 registrada como implementada e funcionalmente aprovada: CA7.1–CA7.9; regressão funcional RF01–RF16 aprovada nos cenários executados.
- Workflow `Testes Python e cobertura` executado posteriormente na branch `fase-7-selecao-exclusao-coletiva`, conforme confirmação do usuário: 65 testes aprovados, 95,83% de cobertura de linhas e 92,54% de branches; commit informado `c6feb6b`. O identificador da execução não consta no registro disponível.
- CA7.11 registrado como aprovado: workflow Python/cobertura e workflow HTML/contraste na branch de trabalho.
- RNF01 permanece parcial: GitHub Pages e requisição do lockfile Pyodide confirmados (HTTPS, HTTP 200), mas a lista completa de requisições não foi auditada.
- CA7.12 atualizado: payload de XSS importado foi exibido como texto comum; avaliação permanece delimitada e parcial, com pontos de hardening documentados.
- A Etapa 6 permanece em andamento por pendências de RNF01, RNF02, RNF05, RNF06 e homologação por toque CA5.1. RNF07 foi validado funcionalmente para carregamento e sucesso. Nenhuma homologação integral foi declarada.


### Atualização da validação da Fase 7

- CA7.1–CA7.9 aprovados pelo usuário nos cenários manuais executados; a regressão funcional RF01–RF16 também foi aprovada nos cenários executados.
- Suíte local informada: 65 testes aprovados; cobertura de linhas de 95,83% e branches de 92,54%.
- Workflow `Validar HTML e contraste`: execução `41742982859` aprovada na branch `fase-7-selecao-exclusao-coletiva`, commit `faa12e9`.
- Workflow `Testes Python e cobertura`: execução `41742344451` aprovada na `main`, commit `6a967af`, com 60 testes, 96,10% de linhas e 92,72% de branches. Como antecede a Fase 7, não comprova RNF03 na branch atual; a execução correspondente permanece pendente.
- A validação final de RNF01–RNF07 mantém as lacunas registradas em `docs/ESTADO-ATUAL.md`.

### CA7.12 — validação de segurança (em andamento)

- Inspeção estática da branch `fase-7-selecao-exclusao-coletiva`, no commit-base `c4e8eae`, abrangendo HTML, CSS, módulos JavaScript, domínio Python, dependências e workflows.
- Não foram encontrados os principais sinks HTML pesquisados (`innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `eval` e `new Function`); os conteúdos de tarefas examinados são renderizados por APIs de texto e criação explícita de elementos.
- Testes dinâmicos: payload XSS no título e na descrição foram exibidos como texto, sem execução de alerta nos cenários observados.
- Um backup com payload no título foi importado com sucesso e substituiu as três tarefas existentes por uma, conforme RF14. A confirmação de que o conteúdo importado também é exibido literalmente, sem execução, ainda não foi registrada; este cenário permanece inconclusivo para XSS.
- Inspeção do `localStorage` pelo usuário: somente propriedades funcionais das tarefas; nenhuma credencial ou dado sensível foi identificado. Os dados permanecem em texto claro, sem criptografia.
- Dependências externas identificadas nos arquivos examinados: Google Fonts (fonte Inter) e jsDelivr (Pyodide). O link do repositório GitHub é apenas navegação, não dependência de execução.
- Pontos de hardening preliminares: ausência de CSP explícita; carregamento do Pyodide sem SRI; importação JSON sem limite explícito de tamanho/quantidade; GitHub Actions referenciadas por tags, não por SHA imutável. Não são vulnerabilidades exploradas/confirmadas nesta revisão.
- Nenhuma vulnerabilidade crítica ou alta foi confirmada na inspeção estática realizada. A avaliação permanece delimitada e não constitui pentest nem auditoria abrangente.

### Fase 7 — implementação inicial

- Aprovado o cabeçalho contextual de seleção, com ações para selecionar todas, desselecionar todas, exibir a quantidade selecionada e excluir as tarefas selecionadas.
- A seleção individual será feita nos cartões e abrangerá todas as colunas e estados, inclusive tarefas concluídas; o checkbox de seleção será independente do indicador de conclusão e o menu individual permanecerá independente.
- A exclusão coletiva exigirá confirmação explícita com a quantidade. Cancelamento preserva dados e seleção. A seleção será temporária no frontend, fora do `localStorage` e do backup, e só será limpa após persistência bem-sucedida.
- Formalizado o contrato de `excluir_tarefas()`: rejeitar lista vazia, IDs duplicados e IDs inexistentes; validar todos antes de excluir; não permitir exclusão parcial; não mutar a entrada; reindexar somente colunas afetadas com `reindexar_coluna()`; preservar metadados restantes exceto `ordem`; gerar timestamp global único; retornar novo estado e tarefas excluídas.
- Em falha de persistência, dados, ordenação, interface e seleção deverão permanecer preservados. Exclusão parcial, idempotência adicional e demais operações coletivas permanecem fora do escopo.
- Implementada a operação Python `excluir_tarefas()` e exportada pela API pública do pacote. A operação valida a lista e todos os IDs antes de alterar o estado, rejeita vazio/duplicidade/inexistência, não muta a entrada, reindexa apenas colunas afetadas e retorna as tarefas excluídas com um timestamp global.
- Integrada a operação ao dispatcher Pyodide e à API `deleteTasks`, utilizando a persistência preventiva existente.
- Implementada seleção independente da conclusão nos cartões, barra contextual com selecionar todas/desselecionar todas/contagem/exclusão e confirmação com quantidade. A seleção é reconciliada após alterações persistidas e o foco é direcionado de volta ao quadro ao limpar a seleção.
- Adicionados testes unitários para cenários válidos e inválidos e ampliados os workflows para a branch da Fase 7.
- **Validação no registro inicial:** gravações no GitHub confirmadas; naquele momento, a execução da suíte, cobertura, workflows e testes manuais ainda estava pendente. Os resultados posteriores estão registrados na atualização de validação da Fase 7 acima.

### Replanejamento da homologação final

- Mantida a aprovação de CA6.1–CA6.8; a Fase 6 não depende da regressão integrada nem da validação dos workflows para avançar.
- Transferidos CA6.9 e CA6.10 para o encerramento do projeto, após os testes específicos da Fase 7, como CA7.10 (regressão integrada RF01–RF16 e RNF01–RNF07) e CA7.11 (workflows GitHub).
- Incluído CA7.12 para validação de segurança com escopo, método, evidências, achados, severidade, correções e retestes documentados.
- Definido que a regressão final deverá reaproveitar evidências anteriores válidas e concentrar novos testes nos impactos, integrações e lacunas, evitando repetição indiscriminada de testes de aceite.
- O plano passa a refletir sua natureza evolutiva, preservando rastreabilidade e distinguindo critérios aprovados, transferidos e pendentes.

### Fase 6 — homologação parcial

- Registrada a aprovação de CA6.1–CA6.7, incluindo a preservação dos dados nos cenários de rejeição e o cancelamento da importação sem alterações.
- Implementado ajuste de usabilidade em `js/backup_ui.js`: rejeições de JSON inválido agora exibem mensagem objetiva e amigável, enquanto os detalhes técnicos são enviados ao console para diagnóstico. Validação manual aprovada pelo usuário: importação válida e rejeição de schema diferente de 1.0, chave inválida e valor inválido com mensagem amigável.
- CA6.8 aprovado em teste manual: falha `QuotaExceededError` simulada durante a importação; mensagem de não conclusão exibida; estado em memória e `localStorage` comparados com os valores anteriores (`true`); quadro visual confirmado inalterado. O método original de `Storage.prototype.setItem` foi restaurado e as variáveis temporárias removidas.
- Permanecem pendentes CA6.9 (regressão integrada RF01–RF15 e RNF01–RNF07) e CA6.10 (conferência dos workflows GitHub).
- A execução local informada de 60 testes, com 96,10% de cobertura de linhas e 92,72% de branches, foi preservada como evidência automatizada já obtida.

### Fase 6 — relatórios e backup JSON (implementação)

- Criado `js/reports_ui.js` para apresentar no modal Relatórios os indicadores calculados pelo núcleo Python, com filtro opcional por data de conclusão e opção de limpar o período.
- Criado `js/backup_ui.js` para exportar o envelope JSON versionado e conduzir a seleção, validação, confirmação e importação de arquivos.
- Integrados à ponte Pyodide os cálculos do RF12, a geração de backup e a preparação de importação no domínio Python.
- Reforçada a importação estrita: rejeita JSON malformado, chaves duplicadas, constantes não padronizadas, campos ausentes/desconhecidos e tarefas inválidas; o timestamp global é gerado pelo Python somente após a confirmação.
- A substituição usa o fluxo transacional existente, que persiste antes de confirmar memória e interface e tenta restaurar o documento anterior em falha de renderização.
- Atualizados `index.html` e `css/components.css`: Relatórios abre como modal; Importar/Exportar permanece como tela com ações próprias e modal de confirmação com contadores.
- Ampliados os testes unitários de schema e criados workflows para sintaxe/HTML/contraste e para `pytest` com metas RNF03.
- **Validação:** CA6.1–CA6.8 aprovados. A mensagem amigável para rejeição de JSON inválido foi validada pelo usuário nos cenários de schema incompatível, chave inválida e valor inválido; a importação válida também foi aprovada. CA6.9 (regressão integrada) e CA6.10 (conferência dos workflows) foram transferidos para o encerramento do projeto como CA7.10 e CA7.11, respectivamente.

### Fase 5 — implementação inicial

- Criados `js/kanban_ui.js`, `js/drag_drop.js` e `js/calendar_ui.js` para renderização dinâmica, menus de cartão, movimentação por Pointer Events e calendário mensal com marcadores e popover.
- Integrados os formulários de criação, edição e exclusão e o menu acessível “Mover para...” às operações de `window.kanbanApp`, preservando a persistência preventiva da Fase 4.
- Implementada busca em tempo real por título e descrição, com normalização de acentos; os atalhos `Ctrl + K` e `Esc` existentes foram mantidos.
- Indicadores de resumo e Foco de Hoje passaram a consultar as funções Python pela ponte JS/Python, usando a data local do navegador.
- Atualizado o workflow para verificar sintaxe dos módulos ES, HTML e contraste na branch `fase-5-interacoes`.
- **Validação pendente:** não foram confirmados testes locais/manuais de navegador nem resultado de execução do workflow nesta sessão. CA5.1–CA5.7 não devem ser considerados concluídos até a obtenção das evidências previstas.

### Fase 4 — validação local parcial

- Registrados os testes do usuário para criação, edição, movimentação e exclusão via API JS/Python, com conferência de persistência no `localStorage`.
- Falhas simuladas de gravação nas quatro operações preservaram o estado anterior em memória e no armazenamento; notificação visual observada no cenário de criação.
- Recuperação após recarga confirmada após criação. Permanecem pendentes a confirmação visual do indicador de runtime, evidência de recarga após as demais operações e homologação no GitHub Pages com auditoria de rede.
- Nenhuma publicação ou integração à `main` realizada nesta atualização.

### Simplificação da composição da interface

- Removida a barra inferior; crédito tecnológico e versão transferidos para a parte inferior da sidebar.
- Mantido o timestamp funcional somente no cartão Status da Aplicação. Removidos o timestamp estático e o ícone decorativo do rodapé.
- Removidos os estilos e a reserva de espaço associados à barra inferior.
- Validação visual/responsiva desta alteração pendente.

### Revisão de fidelidade ao mockup e telas do menu

- Reposicionado visualmente o indicador “Aplicação Online” na barra superior, mantendo a alternância de tema à direita e removendo a identificação ilustrativa do cabeçalho.
- Restauradas as descrições das colunas e os ícones de estado; refinado o mascote da barra lateral.
- Calendário com cabeçalho azul-marinho, mês e setas visuais; grade corrigida para novembro de 2025; criado painel de calendário em tela própria.
- Resumo corrigido para 2 concluídas (29%) e 5 pendentes (71%), com pendentes agregando A Fazer e Em Andamento e duas barras de progresso.
- Rodapé restaurado com o crédito completo de Python, Pyodide, Alura e Google for Startups; versão e última atualização à direita.
- Criadas telas demonstrativas estáticas de Relatórios, Importar/Exportar e Configurações. Não foram implementadas operações funcionais dessas áreas.
- Workflow `41560866108` aprovado no commit `db37ac91`: Nu HTML Checker e auditoria de contraste sem falhas.

### Fase 3 — Correções visuais solicitadas

- Cabeçalho atualizado com indicador “Aplicação online” e ícone de confirmação; removido o avatar do cabeçalho e reposicionado o avatar na barra lateral.
- Ampliados os ícones de navegação, estados, seleção circular das tarefas, títulos, descrições, prioridades e prazos; o menu de cada cartão passou a usar três pontos verticais.
- Cartões concluídos passaram a exibir confirmação e data de conclusão.
- Calendário recebeu cabeçalho claro, identificação do mês e setas visuais de navegação.
- Resumo passou a exibir quantidade e percentual por estado, com barra segmentada.
- Status Pyodide apresentado como indicador demonstrativo; rodapé ampliado e última atualização alinhada à direita.
- Ajustados rótulos de prazo para Hoje/Amanhã. Nenhuma integração funcional da Fase 4 foi iniciada.
- Commits: `5267b09`, `b587491`, `dd27bbc`, `82aa222` e `fcf7994`.

### Validado
- Workflows `41558220193` e `41558291161` aprovados: HTML e contraste sem falhas.

### Fase 3 — Mocks visuais e refinamento

- Substituídos caracteres Unicode por ícones SVG consistentes na navegação, busca, tema, calendário e resumo.
- Criado avatar ilustrativo sem iniciais ou identidade de usuário; removido `JD`.
- Rodapé ajustado para atravessar a largura total da aplicação.
- Reforçadas as cores de destaque, tipografia, cartões e hierarquia visual nos temas claro e escuro.
- Incluídos sete cartões demonstrativos, calendário estático de novembro/2026, resumo coerente (7 tarefas, 28,6% concluídas e 71,4% pendentes) e status/última atualização de exemplo.
- Dados demonstrativos não são persistidos nem ativam operações; servem como referência visual para a futura integração.
- Corrigidos atributos ARIA inválidos identificados na primeira execução do Nu HTML Checker.
- Commits da revisão: `9c2bd97`, `740aa60` e `98078d1`.

### Validado
- Workflow `41553398236`: 25 combinações de contraste aprovadas, zero reprovações; Nu HTML Checker com zero erros e zero avisos.

### Pendente
- Inspeção visual nos três breakpoints e nos dois temas, incluindo `prefers-reduced-motion`; CA3.1–CA3.3 e CA3.5 aguardam inspeção visual.

### Fase 3 — Revisão visual

- Reorganizada a estrutura de `index.html` para aproximar a interface do mockup oficial: sidebar e navegação, banner `Olá!`, três colunas, cartões, painel de informações e rodapé.
- Atualizadas as folhas CSS para compor a nova estrutura, mantendo temas claro/escuro, breakpoints e suporte a movimento reduzido.
- Ajustados o ícone da alternância de tema e a cor de foco no tema escuro.
- Preservados os seis diálogos e seus controles ainda desabilitados enquanto as integrações funcionais não forem implementadas.
- Commits registrados na branch `main`: `d02c4fe`, `b5c3200` e `6861fc8`.

### Validado
- Workflow `41550901785` concluído com sucesso: 25 combinações de contraste aprovadas, zero reprovações, Nu HTML Checker com zero erros e zero avisos.

### Pendente
- Inspecionar Desktop, Tablet e Mobile nos temas claro e escuro, incluindo `prefers-reduced-motion`; CA3.1–CA3.3 e CA3.5 ainda pendentes (CA3.4 aprovado pela auditoria automatizada).
- A Fase 2 continua com checklist manual pendente; Fases 4 a 6 não iniciadas.

## [Não lançado] — 2026-11-02

### Fase 3 — CSS e validação visual (implementação)

- Criadas as folhas modulares `css/variables.css`, `css/base.css`, `css/layout.css`, `css/kanban.css` e `css/components.css`.
- Integrados os estilos ao `index.html`, com layout para Desktop (>= 1200 px), Tablet (768–1199 px) e Mobile (< 768 px).
- Implementados os temas Claro e Escuro com tokens CSS nativos, alternância acessível e persistência da preferência visual no navegador.
- Adicionado suporte a `prefers-reduced-motion`.
- Criado `scripts/check_contrast.py`, com verificações de contraste de texto, indicadores, bordas e foco para os dois temas.
- Ampliado o workflow `validar-html.yml` para executar a auditoria de contraste e considerar alterações em CSS.
- Verificação matemática independente das 23 combinações previstas no script: todas atingiram os limites definidos; a execução confirmatória do script pelo workflow ainda precisa ser conferida.
- Permanecem pendentes a inspeção visual humana nos seis cenários responsivos/temas e a evidência visual de referência atualizada. O PNG original permanece preservado.

### Fase 2 — HTML e acessibilidade — 2026-11-02

- Atualizado o README com roteiro de inspeção visual da Fase 3 e instruções para executar a auditoria de contraste.

### Adicionado
- Estrutura HTML semântica da aplicação, com as três colunas do Kanban, áreas de apoio, formulários e diálogos nativos.
- Recursos estruturais de acessibilidade: navegação por teclado, atalho `Ctrl + K`, comportamento contextual de `Esc`, nomes acessíveis, foco visível e gerenciamento de foco nos diálogos.
- Workflow do GitHub Actions para validação do `index.html` pelo Nu HTML Checker.
- README com instruções para execução local por servidor HTTP e roteiro de verificação manual da Fase 2.

### Corrigido
- Erros e avisos apontados pelo Nu HTML Checker: campos `select` obrigatórios sem opção inicial adequada, hierarquia de títulos e atributos ARIA redundantes.

### Validado
- Fase 1: 48 testes aprovados; cobertura de 96,16% das linhas e 92,78% dos branches.
- Fase 2: 20 verificações automatizadas gerais em Chromium aprovadas; os seis diálogos também foram exercitados individualmente.
- Nu HTML Checker: execução do workflow concluída com zero erros e zero avisos.

### Pendente
- Checklist manual de acessibilidade da Fase 2 pelo usuário.
- Validação visual da Fase 3 nos seis cenários (três breakpoints × dois temas), confirmação da execução da auditoria no workflow e produção/inspeção da referência visual corrigida.
- Fases 4 a 6, conforme o plano de implementação.

## Histórico anterior

### Fase 1 — Domínio Python e testes — 2026-11-01

#### Adicionado
- Entidade e regras de domínio para tarefas, incluindo validações e ciclo de vida dos estados.
- Serviços para operações e reordenação de tarefas.
- Validação do contrato JSON e métricas do projeto.
- Suíte automatizada com procedimento de verificação de cobertura.

#### Validado
- Procedimento oficial: `pytest && python scripts/verify_coverage.py`.
- Resultado registrado: 48/48 testes aprovados, 96,16% de cobertura de linhas e 92,78% de branches.
