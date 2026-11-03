# Changelog

Este arquivo registra alterações relevantes do projeto em ordem cronológica inversa. Os registros descrevem o que foi implementado e validado, sem antecipar funcionalidades planejadas.

## [Não lançado] — 2026-11-03

### Fase 6 — homologação parcial

- Registrada a aprovação de CA6.1–CA6.6, incluindo a confirmação de preservação das 30 tarefas após rejeição de JSON com valor malformado.
- Registrado CA6.7 (cancelamento da importação) como executado e funcionalmente aprovado; permanece pendente apenas a substituição da mensagem técnica por uma mensagem clara e amigável ao usuário.
- Permanecem pendentes CA6.8 (falha de persistência/rollback), CA6.9 (regressão integrada RF01–RF15 e RNF01–RNF07) e CA6.10 (conferência dos workflows GitHub).
- A execução local informada de 60 testes, com 96,10% de cobertura de linhas e 92,72% de branches, foi preservada como evidência automatizada já obtida.

### Fase 6 — relatórios e backup JSON (implementação)

- Criado `js/reports_ui.js` para apresentar no modal Relatórios os indicadores calculados pelo núcleo Python, com filtro opcional por data de conclusão e opção de limpar o período.
- Criado `js/backup_ui.js` para exportar o envelope JSON versionado e conduzir a seleção, validação, confirmação e importação de arquivos.
- Integrados à ponte Pyodide os cálculos do RF12, a geração de backup e a preparação de importação no domínio Python.
- Reforçada a importação estrita: rejeita JSON malformado, chaves duplicadas, constantes não padronizadas, campos ausentes/desconhecidos e tarefas inválidas; o timestamp global é gerado pelo Python somente após a confirmação.
- A substituição usa o fluxo transacional existente, que persiste antes de confirmar memória e interface e tenta restaurar o documento anterior em falha de renderização.
- Atualizados `index.html` e `css/components.css`: Relatórios abre como modal; Importar/Exportar permanece como tela com ações próprias e modal de confirmação com contadores.
- Ampliados os testes unitários de schema e criados workflows para sintaxe/HTML/contraste e para `pytest` com metas RNF03.
- **Validação:** CA6.1–CA6.7 executados, com CA6.1–CA6.6 aprovados e CA6.7 funcionalmente aprovado; permanece pendente apenas o ajuste da mensagem exibida no cancelamento. CA6.8 (falha de persistência/rollback), CA6.9 (regressão integrada) e CA6.10 (conferência dos workflows) continuam pendentes.

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

## [Não lançado] — 2026-11-03\n\n### Revisão de fidelidade ao mockup e telas do menu\n\n- Reposicionado visualmente o indicador “Aplicação Online” na barra superior, mantendo a alternância de tema à direita e removendo a identificação ilustrativa do cabeçalho.\n- Restauradas as descrições das colunas e os ícones de estado; refinado o mascote da barra lateral.\n- Calendário com cabeçalho azul-marinho, mês e setas visuais; grade corrigida para novembro de 2025; criado painel de calendário em tela própria.\n- Resumo corrigido para 2 concluídas (29%) e 5 pendentes (71%), com pendentes agregando A Fazer e Em Andamento e duas barras de progresso.\n- Rodapé restaurado com o crédito completo de Python, Pyodide, Alura e Google for Startups; versão e última atualização à direita.\n- Criadas telas demonstrativas estáticas de Relatórios, Importar/Exportar e Configurações. Não foram implementadas operações funcionais dessas áreas.\n- Workflow `41560866108` aprovado no commit `db37ac91`: Nu HTML Checker e auditoria de contraste sem falhas.\n\n\n### Fase 3 — Correções visuais solicitadas\n\n- Cabeçalho atualizado com indicador “Aplicação online” e ícone de confirmação; removido o avatar do cabeçalho e reposicionado o avatar na barra lateral.\n- Ampliados os ícones de navegação, estados, seleção circular das tarefas, títulos, descrições, prioridades e prazos; o menu de cada cartão passou a usar três pontos verticais.\n- Cartões concluídos passaram a exibir confirmação e data de conclusão.\n- Calendário recebeu cabeçalho claro, identificação do mês e setas visuais de navegação.\n- Resumo passou a exibir quantidade e percentual por estado, com barra segmentada.\n- Status Pyodide apresentado como indicador demonstrativo; rodapé ampliado e última atualização alinhada à direita.\n- Ajustados rótulos de prazo para Hoje/Amanhã. Nenhuma integração funcional da Fase 4 foi iniciada.\n- Commits: `5267b09`, `b587491`, `dd27bbc`, `82aa222` e `fcf7994`.\n\n### Validado\n- Workflows `41558220193` e `41558291161` aprovados: HTML e contraste sem falhas.

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
- Validação visual da Fase 3 nos seis cenários (três breakpoints × dois temas), confirmação da execução da auditoria no workflow e produção/inspeção da referência visual corrigida.\n- Fases 4 a 6, conforme o plano de implementação.

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
