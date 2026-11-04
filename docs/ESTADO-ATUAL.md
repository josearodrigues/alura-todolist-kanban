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
  - *Branch remota de trabalho:* `fase-7-selecao-exclusao-coletiva`.
  - *Último commit remoto confirmado antes da implementação da Fase 7:* `6a967af2aca53a5af5fcfed98e3ff1ea44b8d0d9` (merge da Fase 6).
  - *Branch principal:* `main`, preservada; esta atualização documental será restrita à branch de trabalho.
  - *Situação local/remota:* o estado remoto foi consultado no GitHub. A cópia local não foi inspecionada nesta atualização; portanto, não há confirmação de sincronização local.
  - *Histórico remoto:* a Fase 1 culminou no commit `0ef5cf4`. A Fase 2 foi registrada em `main` por meio dos commits de implementação HTML e atualizações documentais; a pipeline Nu HTML Checker foi adicionada no commit `11f6cdf`; a correção HTML foi registrada em `a6c7495` e o diagnóstico detalhado da pipeline em `58558ad`. A implementação CSS da Fase 3 e a auditoria de contraste foram adicionadas diretamente à `main` em atualização anterior.
  - *Ações realizadas na Fase 5:* módulos de interface, drag and drop e calendário adicionados/atualizados diretamente na branch remota `fase-5-interacoes`; ponte Python/JavaScript ampliada para métricas; workflow ajustado para validar os módulos ES e HTML nessa branch. Nenhuma alteração foi feita na `main`. Nenhuma tag, release ou publicação da aplicação foi criada. Último commit de código da camada de interação: `11e7615` (tratamento de falha de persistência sem notificação duplicada).
- **Mockup Oficial de Referência:**
  - Arquivo `Painel Kanban de Tarefas Pastel.png`, localizado na Biblioteca do projeto Desafios Alura e consultado durante a revisão visual de 2026-11-02/03.
  - O PNG histórico versionado em `docs/design/referencias/todolist-kanban-1.0-mockup.png` permanece preservado intacto.

---

## 2.1 Revisão de fidelidade ao mockup e telas secundárias — 2026-11-03

- Reestabelecida a hierarquia da barra superior: busca à esquerda; indicador verde “Aplicação Online” e alternância de tema à direita; sem avatar/identificação de usuário no cabeçalho; mascote ilustrativo mantido na barra lateral.
- Saudação preservada como “Olá!” conforme requisito aprovado, com ilustração de mão acenando.
- Reintroduzidas as descrições das três colunas; refinados ícones, cores e tipografia.
- Calendário lateral com cabeçalho azul-marinho, mês, setas visuais e grade alinhada a novembro de 2025; criado painel de calendário em tela própria. Os controles de mês estavam desabilitados na versão demonstrativa; a navegação funcional foi implementada na Fase 5.
- Resumo corrigido: 7 tarefas; 2 concluídas (29%) e 5 pendentes (71%), sendo pendentes a soma de A Fazer + Em Andamento. Restauradas duas barras de progresso independentes (concluídas e pendentes).
- Rodapé recuperou o crédito completo “Desenvolvido com Python • Pyodide • ♥ Alura + Google for Startups”, com versão e última atualização à direita.
- Criadas telas demonstrativas estáticas para Relatórios, Importar/Exportar e Configurações, além do Calendário. Na Fase 6, Relatórios foi convertido em modal funcional e a tela Importar/Exportar recebeu ações de backup; Configurações permanece demonstrativa. O calendário foi integrado funcionalmente na Fase 5.
- Workflow `41560866108` aprovado no commit `db37ac91`: Nu HTML Checker sem erros/avisos e auditoria de contraste aprovada. Inspeção visual manual e aceite do usuário ainda pendentes.

## 2.2 Implementação da Fase 6 — 2026-11-03

- `js/reports_ui.js`: modal de relatórios com indicadores dinâmicos e filtro opcional de conclusão por data inicial/final.
- `js/backup_ui.js`: download JSON, seleção de arquivo, validação, confirmação com contadores e importação.
- `src/todolist/schema.py`: leitura estrita de JSON, rejeição de chaves duplicadas/constantes não padronizadas, validação do envelope e preparação do estado importado. O timestamp global é gerado pelo Python somente após confirmação.
- `js/pyodide_bridge.js` e `js/app.js`: integração dos relatórios e backups com o núcleo Python e a persistência preventiva existente.
- `index.html` e `css/components.css`: Relatórios abre em modal; Importar/Exportar permanece como tela própria, com diálogos de operação e confirmação.
- `tests/test_schema.py`: novos testes de preparação e validação estrita da importação.
- `.github/workflows/validar-html.yml`: inclui a branch da Fase 6 e a sintaxe dos novos módulos JavaScript. `.github/workflows/testes-python.yml`: executa `pytest && python scripts/verify_coverage.py` em Python 3.14.
- **Testes automatizados:** execução local informada pelo usuário: 60 testes aprovados; cobertura de linhas de 96,10% (meta mínima de 90%) e cobertura de branches de 92,72% (meta mínima de 85%). O script de verificação de cobertura concluiu com sucesso.
- **Homologação manual:** CA6.1–CA6.7 aprovados, incluindo a preservação das 30 tarefas nos cenários de rejeição e o cancelamento sem alteração dos dados. Na validação posterior do ajuste de usabilidade, o usuário aprovou a importação válida e a mensagem amigável para schema diferente de 1.0, chave inválida e valor inválido. Detalhes na Seção 12.
- **Homologação manual:** CA6.8 aprovado em 2026-11-03. Durante a importação de um backup válido diferente do estado atual, foi simulada falha de `Storage.prototype.setItem` com `QuotaExceededError`. A aplicação informou que a substituição não foi concluída. As comparações `JSON.stringify(window.kanbanApp.getState()) === window.estadoAntesCA68` e `localStorage.getItem("kanban_app_state") === window.storageAntesCA68` retornaram `true`; o usuário confirmou que o quadro visual permaneceu inalterado. O método original de `Storage.prototype.setItem` e as variáveis temporárias foram restaurados/removidos ao final.
- **Situação da Fase 6:** CA6.1–CA6.8 aprovados. CA6.9 (regressão integrada) e CA6.10 (workflows) foram transferidos para o encerramento do projeto, após os testes específicos da Fase 7; não bloqueiam o início da Fase 7.

## 3. Estado da Governança Documental

A documentação de governança está estabelecida. A revisão desta data atualizou os arquivos operacionais e corrigiu inconsistências de formatação e histórico:
- **`docs/REQUISITOS.md`:** Atualizado (Versão 1.9 — RF16 detalha seleção global e contrato de integridade da exclusão coletiva).
- **`docs/PLANO-IMPLEMENTACAO.md`:** Atualizado (Versão 3.7 — rastreabilidade das fases, workflows e avaliação delimitada da CA7.12).
- **`docs/ESTADO-ATUAL.md`:** Atualizado com o estado operacional corrente (este documento).
- **`README.md`:** Atualizado com tecnologias, estrutura do projeto, instruções de execução, testes, roteiro manual da Fase 2 e roteiro de inspeção visual da Fase 3.
- **`CHANGELOG.md`:** Registra as alterações implementadas por fase.
- **`LICENSE`:** Licença MIT.

---

## 4. Situação de Cada Etapa e Fase do Projeto

| Etapa / Fase | Situação | Descrição / Entregáveis |
| :--- | :--- | :--- |
| **Etapa 1 — Descoberta e Requisitos** | **Concluída e Aprovada** | Levantamento via método Grill Me; requisitos aprovados. |
| **Etapa 2 — Planejamento Funcional** | **Concluída e Aprovada** | Especificação consolidada de RF01–RF16, RNF01–RNF07 e regras de negócio. |
| **Etapa 3 — Arquitetura Técnica** | **Concluída e Aprovada** | Sete decisões técnicas aprovadas, arquitetura modular e critérios de testes definidos. |
| **Etapa 4 — Plano de Implementação** | **Concluída e Aprovada** | Plano de Implementação (versão 2.1) formalmente aprovado pelo usuário. |
| **Etapa 5 — Implementação Controlada** | **Implementação das Fases 1 a 7 concluída; homologação de fases anteriores parcialmente pendente** | Fase 7 implementada e funcionalmente aprovada nos critérios CA7.1–CA7.9. Permanecem pendências de homologação herdadas, especialmente CA5.1 (toque), além das verificações não funcionais consolidadas na Etapa 6. |
| ↳ *Fase 1: Domínio Python e Testes* | **Concluída e Validada** | Pacote `src/todolist/`, `pyproject.toml`, testes automatizados (`tests/`) e `scripts/verify_coverage.py` implementados. Após a revisão corretiva, o procedimento oficial aprovou 48/48 testes, com 96,16% de cobertura de linhas e 92,78% de branches. |
| ↳ *Fase 2: HTML e Acessibilidade* | **Implementada; validação manual parcial** | `index.html` contém estrutura semântica, três colunas, widgets, formulários, seis diálogos nativos, template de cartão, nomes acessíveis, atalhos e gerenciamento de foco. Foram aprovadas 20 verificações automatizadas gerais em Chromium; os seis diálogos também foram exercitados individualmente. Nu HTML Checker: execução `41520632228`, zero erros e zero avisos. Na verificação manual desta sessão: `Tab`, `Shift + Tab`, `Enter`, `Espaço`, `Ctrl + K`, foco inicial/contenção/restauração no diálogo Nova Tarefa e fechamento desse diálogo por `Esc` aprovados pelo usuário. Menu contextual não testado: controle `⋮` está desativado; usuário também identificou divergência visual do ícone em relação ao mockup. Inspeção visual dos rótulos/nome dos controles sem problemas aparentes, mas leitor de tela não testado. Validação formal da fase permanece parcial; itens não verificados não são considerados aprovados. |
| ↳ *Fase 3: CSS e Validação Visual* | **Implementada; inspeção visual manual concluída** | Refinamentos visuais e mocks estáticos mantidos. Navegação lateral recolhível em telas de até 960 px, com fechamento por `Esc`, clique no fundo e seleção de seção, restauração e contenção de foco; ícone `⋮` ajustado visualmente, sem ativar o menu contextual. Usuário aprovou Desktop, Tablet (1024 × 768) e Mobile (390 × 844), nos temas Claro e Escuro. Teste manual de `prefers-reduced-motion` também aprovado. Workflow `41553398236`: 25 combinações de contraste aprovadas, zero reprovações e Nu HTML Checker sem erros/avisos. CA3.1–CA3.5 considerados atendidos conforme as evidências registradas; não implica validação funcional das telas demonstrativas. |
| ↳ *Fase 4: WebAssembly e Persistência* | **Implementada; validação funcional concluída, CA4.1 parcialmente verificado** | Pyodide 314.0.7 e importação dos cinco módulos confirmados. Criação, edição, movimentação e exclusão executadas pela API JS/Python; persistência, timestamp e recuperação após recarga confirmados nas quatro operações. Falhas simuladas nas quatro operações preservaram memória e armazenamento; notificação visual observada na criação. CA4.2–CA4.6 atendidos conforme as evidências registradas. No GitHub Pages, o usuário confirmou o carregamento e observou, no filtro Fetch/XHR durante a carga, uma requisição ao CDN jsDelivr para `pyodide-lock.json` (HTTP 200), sem chamadas a APIs de backend nessa amostra. Como a auditoria ficou restrita ao filtro e ao período observado, CA4.1 permanece parcialmente verificado, não homologado integralmente. |
| ↳ *Fase 5: Interações (Pointer Events)* | **Implementada; validação manual parcial** | CA5.2 a CA5.7 aprovados nos cenários exercitados, exceto CA5.1, que permanece parcial por falta de teste de toque. Mouse e alternativa acessível pelo menu foram aprovados. CA5.5 aprovado no cenário exercitado. Após observação de usabilidade com 10 tarefas no mesmo dia, foi implementada rolagem vertical interna no popover; validação visual com listas extensas e em viewport móvel ainda pendente. Correção do menu contextual, datas relativas, destaque de vencidas e remoção da mensagem transitória de carregamento foram implementados e validados pelo usuário. A implementação da Fase 5 está concluída; aceite integral aguarda teste de toque em CA5.1. |
| ↳ *Fase 6: Relatórios e Backup JSON* | **Implementada; CA6.1–CA6.8 aprovados** | Mensagem amigável para rejeição de JSON inválido implementada e validada pelo usuário. CA6.9 e CA6.10 transferidos para o encerramento do projeto como CA7.10 e CA7.11; não bloqueiam a Fase 7. Testes automatizados locais informados: 60 aprovados, cobertura de linhas 96,10% e branches 92,72%. Consulte a Seção 12. |
| ↳ *Fase 7: Seleção e Exclusão Coletiva* | **Implementada; CA7.1–CA7.9 aprovados** | 65 testes aprovados; cobertura de linhas 95,83% e branches 92,54%. Validação manual CA7.1–CA7.9 aprovada nos cenários testados, incluindo rollback, preservação da seleção e integridade dos metadados. Regressão funcional RF01–RF16 aprovada nos cenários executados. Workflows HTML/contraste e Python/cobertura aprovados na branch de trabalho, conforme Seção 19. A homologação não funcional do projeto permanece em andamento. |
| **Etapa 6 — Validação Final** | **Encerrada para a entrega acadêmica, com ressalvas documentadas** | Regressão funcional RF01–RF16 aprovada nos cenários executados. RNF02 validado funcionalmente; RNF03 validado nos workflows executados; RNF04 validado por evidências de rollback; RNF07 validado nos estados de carregamento e sucesso. RNF01 permanece com auditoria de rede parcial; RNF05 com reteste visual integrado não concluído; RNF06 sem teste com leitor de tela; CA5.1 sem homologação física por toque; CA7.12 corresponde a avaliação de segurança delimitada, não a pentest. As limitações foram aceitas para o encerramento acadêmico e não são declaradas como conformidade integral. |

---

## 5. Matriz de Rastreabilidade

- **Planejado:** Aplicação To-Do Kanban estática com Python via WebAssembly (Pyodide), 3 colunas, drag and drop via Pointer Events, calendário integrado, métricas em tempo real e backup JSON.
- **Aprovado:** Versão 1.9 de Requisitos (RF16 detalhado), Etapa 3 (Arquitetura Técnica), Etapa 4 (Plano de Implementação) e decisões funcionais/técnicas da Fase 7. CA7.1–CA7.9 e regressão RF01–RF16 aprovados nos cenários testados.
- **Implementado:** Em 2026-11-03, a interface da Fase 3 recebeu refinamento visual e dados demonstrativos estáticos para tarefas, calendário, resumo e status. Na branch `revisao-visual-d83bbee`, a correção posterior adicionou navegação lateral recolhível em telas de até 960 px e ajustou o símbolo `⋮`; o controle contextual estava desabilitado nessa revisão visual; foi ativado na implementação da Fase 5. Fase 1 implementada: pacote Python `src/todolist/`, configuração, testes e script de cobertura. Fase 2 implementada em `index.html`; workflow Nu HTML Checker criado. Fase 4 implementada na branch `fase-4-pyodide-persistencia`, com ponte JS/Python, Pyodide e persistência local; testes funcionais da API concluídos. Fase 5 implementada na branch `fase-5-interacoes`, com validação manual parcial; Fase 6 implementada e integrada ao histórico remoto até o commit `6a967af`; CA6.1–CA6.8 aprovados e CA6.9/CA6.10 transferidos para o encerramento. A branch atual é `fase-7-selecao-exclusao-coletiva`. A Fase 7 está implementada: serviço coletivo Python, testes, ponte Pyodide, API, seleção individual/global, barra contextual e confirmação. CA7.1–CA7.9 foram aprovados nos cenários testados; suíte automatizada: 65 aprovados, 95,83% de cobertura de linhas e 92,54% de branches. A regressão RF01–RF16 também foi aprovada nos cenários executados. O workflow Python/cobertura foi posteriormente executado com sucesso na branch de trabalho, conforme Seção 19; CA7.12 permanece parcial, conforme Seções 18 e 19.
- **Testado:** Fase 1: procedimento oficial `pytest && python scripts/verify_coverage.py`, com 48/48 testes aprovados, 96,16% de cobertura de linhas e 92,78% de branches. Fase 2: 20 verificações automatizadas em Chromium foram aprovadas; o usuário confirmou manualmente parte dos comportamentos de teclado e foco. Fase 3: usuário aprovou Desktop, Tablet (1024 × 768) e Mobile (390 × 844), nos temas Claro e Escuro, e confirmou o funcionamento com `prefers-reduced-motion` ativo. Não houve teste com leitor de tela. O ícone `⋮` foi implementado, mas não há confirmação isolada de sua aparência.
- **Validado:** critérios CA1.1 a CA1.7 aceitos conforme evidências informadas pelo usuário. Na Fase 2, CA2.1 foi verificado por inspeção estrutural e automatização no navegador; CA2.2 foi validado pelo Nu HTML Checker na execução `41520632228`, sem erros ou avisos. A verificação manual confirmou parte de CA2.3 e CA2.4; CA2.5 e CA2.6 permanecem parcialmente pendentes, sem aceite formal da Fase 2. Na Fase 3, inspeção visual manual aprovada pelo usuário nos três breakpoints (Desktop, Tablet 1024 × 768 e Mobile 390 × 844), nos temas Claro e Escuro; `prefers-reduced-motion` também testado e aprovado. O menu mobile teve funcionamento confirmado pelo usuário. O teste isolado da aparência do ícone `⋮` não foi confirmado.
- **Commitado / Enviado ao GitHub:** Revisão visual registrada diretamente na branch remota `main`: `d02c4fe` (estrutura visual), `b5c3200` (tema e foco), `6861fc8` (ajustes de cabeçalho), `9c2bd97` (mocks e refinamento visual), `740aa60` (semântica e rodapé) e `98078d1` (correção de acessibilidade). O workflow `41553398236`, acionado pelo commit `98078d1`, concluiu com sucesso: 25 combinações de contraste aprovadas, zero reprovações, Nu HTML Checker com zero erros e zero avisos. A execução anterior `41553256719` falhou por atributos ARIA inválidos nos mocks; a correção foi registrada em `98078d1`. Fase 2 registrada diretamente na branch remota `main`. O workflow Nu HTML Checker foi adicionado no commit `11f6cdf`, seus diagnósticos foram aprimorados em `58558ad` e as correções HTML foram registradas em `a6c7495`. Na Fase 3, os arquivos `css/variables.css`, `css/base.css`, `css/layout.css`, `css/kanban.css`, `css/components.css` e `scripts/check_contrast.py` foram criados; `index.html` passou a carregar os estilos e a alternar temas. O workflow `.github/workflows/validar-html.yml` foi ampliado para auditar contraste e considerar alterações em CSS. A cópia local ainda precisa ser sincronizada pelo usuário. Nenhuma tag, release ou publicação da aplicação foi criada.

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

- **Ambiente Git:** repositório remoto `josearodrigues/alura-todolist-kanban`, branch remota de trabalho `fase-7-selecao-exclusao-coletiva`. Último commit remoto confirmado antes da implementação da Fase 7: `6a967af`. A branch recebeu commits de implementação e documentação posteriores. A situação da cópia local não foi verificada. O registro histórico de validação da Fase 4 foi executado pelo usuário no navegador local, com a aplicação servida por HTTP. Naquela ocasião, o usuário confirmou a cópia local alinhada à branch remota e sem alterações pendentes. Isso não confirma o estado local atual.
- **Fase 4 — implementação:** Pyodide 314.0.7 inicializado; cinco módulos Python carregados no filesystem virtual; pacote `todolist` importado; API disponível em `window.kanbanApp`.
- **Fase 4 — operações e persistência:** criação, edição, movimentação e exclusão executadas pela API JS/Python. O conteúdo de `kanban_app_state` e o timestamp foram conferidos após as operações. Recuperação após recarga confirmada para criação, edição, movimentação e exclusão. As três últimas recuperações foram verificadas nesta sessão, com resultados apresentados pelo usuário no console.
- **Fase 4 — falha de persistência:** `Storage.prototype.setItem` foi interceptado temporariamente para simular falha nas quatro operações. Em todos os casos, a alteração foi impedida e o estado anterior permaneceu em memória e no `localStorage`. A notificação de erro foi observada na interface durante o teste de criação; não há confirmação visual independente para as outras três operações.
- **Fase 4 — critérios de aceite:** CA4.2 confirmado pelo usuário (indicador `✓ Carregado`); CA4.3 demonstrado no console; CA4.4 e CA4.5 validados com execução das quatro operações e recuperação após recarga; CA4.6 validado quanto ao rollback nas quatro operações, com notificação visual observada na criação. Para CA4.1, o usuário confirmou a execução no GitHub Pages. Na auditoria realizada, o filtro Fetch/XHR apresentou apenas uma requisição ao CDN jsDelivr (`pyodide-lock.json`, HTTP 200) e nenhuma chamada a API de backend. A observação foi limitada a esse filtro e à carga da página; portanto, CA4.1 permanece parcialmente verificado.
- **Interface:** notificações de erro reposicionadas no topo; barra inferior removida e créditos/versão transferidos para a sidebar. Tipografia dos créditos compactada e conteúdo organizado em três linhas. Ajustes implementados na branch anterior; validação visual final dos últimos créditos ainda não registrada.
- **Registro inicial da validação da Fase 5 (2026-11-03):** as verificações iniciais de criação, edição, exclusão, movimentação, busca, calendário, indicadores, tema e reordenação foram ampliadas pelos resultados mais recentes consolidados na Seção 10. As observações de menu contextual aberto após cancelamento, ciclo de conclusão/reabertura pendente e Foco de Hoje pendente foram resolvidas/validadas posteriormente; consultar a tabela atualizada da Seção 10. Permanecem sem teste o toque em CA5.1 e o cenário adicional de grande volume no popover. A mensagem transitória de carregamento foi removida e validada após recarga; o indicador de status do Pyodide continua funcionando. A limitação observada em navegador móvel antigo está registrada genericamente, sem aparelho ou versão. Workflow `db37ac91`: Nu HTML Checker sem erros/avisos e auditoria de contraste aprovada. A implementação da Fase 5 está concluída; o aceite integral aguarda o teste de toque exigido por CA5.1.
- **Situação local:** antes da rodada de testes funcionais, o usuário confirmou a branch local alinhada à origem e sem alterações pendentes.

---

## 8. Próxima Ação Recomendada

1. Completar a verificação direcionada de RNF01–RNF07, reutilizando evidências válidas e registrando lacunas: auditoria de rede do GitHub Pages (RNF01), inspeção da lógica Python (RNF02), evidência do workflow para RNF03, responsividade integrada (RNF05), acessibilidade WCAG 2.2 AA (RNF06) e feedback de inicialização (RNF07). RNF04 possui evidência de rollback em falha de persistência.
2. Executar e validar o workflow Python/cobertura na branch da Fase 7 (CA7.11); o workflow HTML/contraste já foi aprovado nessa branch.
3. Prosseguir com CA7.12, começando pela confirmação da renderização literal do payload importado e depois cobrindo os pontos dinâmicos ainda não testados.
4. Retestar visualmente sidebar e banner de tarefas vencidas nos temas Claro/Escuro e breakpoints pertinentes. A integração à `main` e publicação permanecem fora desta etapa.
---

## 9. Registro de Validação Local — Fase 4 (2026-11-03)

| Verificação | Evidência observada | Resultado |
|---|---|---|
| Inicialização do Pyodide e importação de `todolist` | Console informou Pyodide 314.0.7 e pacote carregado; API disponível em `window.kanbanApp`. | Aprovada |
| Estado inicial | `getState()` retornou lista vazia e timestamp nulo. | Aprovada |
| Criação | `createTask` retornou `success: true` e `changed: true`. | Aprovada |
| Persistência da criação | Documento `kanban_app_state` continha a tarefa e o timestamp global. | Aprovada |
| Recuperação após recarga — criação | A tarefa foi recuperada após `Ctrl+R` e reinicialização do runtime. | Aprovada |
| Recuperação após recarga — edição | Após edição para o título `Teste de recuperação após edição`, a tarefa e o timestamp atualizado foram recuperados após recarga; confirmação apresentada pelo usuário no console. | Aprovada |
| Recuperação após recarga — movimentação | Após movimentação para `em_andamento`, o estado e o timestamp atualizado foram recuperados após recarga; confirmação apresentada pelo usuário no console. | Aprovada |
| Recuperação após recarga — exclusão | Após exclusão, a consulta por ID retornou `undefined` depois da recarga; confirmação apresentada pelo usuário no console. | Aprovada |
| Falha de persistência na criação | Falha simulada impediu a criação; memória e armazenamento mantiveram uma tarefa; mensagem de erro exibida. | Aprovada para este cenário |
| Edição | `editTask` retornou sucesso com os parâmetros exigidos; metadados não editáveis foram preservados. | Aprovada |
| Persistência da edição | `localStorage` refletiu o título e timestamp atualizados. | Aprovada |
| Movimentação | `moveTask` retornou sucesso e estado `em_andamento`. | Aprovada |
| Persistência da movimentação | `localStorage` refletiu o novo estado e timestamp. | Aprovada |
| Exclusão | `deleteTask` retornou sucesso. | Aprovada |
| Persistência da exclusão | Contagem final igual a zero tanto em memória quanto no `localStorage`. | Aprovada |
| Falha de persistência na edição | Estado anterior preservado em memória e no `localStorage` após falha simulada. | Aprovada |
| Falha de persistência na movimentação | Estado anterior preservado em memória e no `localStorage` após falha simulada. | Aprovada |
| Falha de persistência na exclusão | Tarefa permaneceu em memória e no `localStorage` após falha simulada. | Aprovada |

**Limites desta validação:** os testes funcionais das operações foram executados diretamente pela API no console do navegador, pois os controles da interface permanecem demonstrativos e sua integração está prevista para a Fase 5. A falha de persistência foi simulada nas quatro operações; a notificação visual foi observada na criação. A recuperação após recarga foi confirmada para as quatro operações. No GitHub Pages, a auditoria limitada ao filtro Fetch/XHR durante o carregamento mostrou uma requisição ao CDN jsDelivr para `pyodide-lock.json` (HTTP 200), sem chamadas a APIs de backend nessa amostra. Isso não comprova ausência de toda e qualquer requisição de rede. A substituição de estado/importação não foi testada e permanece reservada à Fase 6.


## Revisão da composição da interface — 2026-11-03

- Removida a barra inferior da aplicação. O crédito tecnológico e a versão foram transferidos para a área inferior do painel esquerdo (sidebar).
- O timestamp funcional da última alteração permanece exclusivamente no cartão Status da Aplicação, conforme RF11. O texto estático “Sem alterações” e o ícone decorativo de atualização do antigo rodapé foram eliminados.
- A reserva de espaço e os estilos específicos da barra inferior foram removidos. A sidebar mantém os créditos também quando aberta como navegação móvel.
- Implementação registrada na branch `fase-4-pyodide-persistencia`; inspeção visual e validação responsiva desta alteração ainda pendentes.


## Correções de interface — 2026-11-03

- **Modal de edição:** estrutura HTML harmonizada com o modal de criação, reutilizando as mesmas classes e regras visuais. Campos, nomes (titulo, descricao, prioridade, data_limite) e fluxo de submissão foram preservados; opções de prioridade agora exibem os mesmos ícones.
- **Inicialização do Kanban:** removidos os cartões demonstrativos estáticos das três listas e os contadores/foco fixos. O quadro mantém sua estrutura e apresenta um estado de carregamento enquanto o Pyodide inicializa; os cartões reais são renderizados a partir do estado recuperado. Em caso de falha do runtime, a mensagem de carregamento informa que não foi possível carregar as tarefas.
- **Acessibilidade:** o contêiner das colunas sinaliza o carregamento com aria-busy e encerra esse estado após a renderização ou falha de inicialização.
- **Registro:** alterações implementadas diretamente na branch fase-5-interacoes. Testes de sintaxe, execução e inspeção visual dos modais e da inicialização ainda pendentes; não considerar as correções homologadas até a validação local e no navegador.


## 10. Registro de Validação Manual — Fase 5 (2026-11-03)

Os resultados abaixo foram informados e confirmados pelo usuário durante a validação no navegador. São evidências de testes manuais, não de testes automatizados.

| Critério / área | Verificação realizada | Resultado / limite |
|---|---|---|
| CA5.1 — movimentação | Drag and drop com mouse e alternativa pelo menu `Mover para...`. | Mouse e alternativa acessível aprovados. Toque e caneta não testados por indisponibilidade de dispositivos. |
| CA5.2 — operações e interface | Criação; edição de título, descrição, prioridade e vencimento; movimentação pelo menu e com mouse; exclusão; atualização dos contadores. | Funcionamento confirmado nos cenários exercitados. Correção posterior fecha menus e submenus contextuais ao fechar/cancelar os diálogos; usuário confirmou. Persistência da edição após recarga não foi explicitamente confirmada nesta rodada. |
| CA5.3 — metadados e transições | Reordenação intra-coluna, no-op, movimentação entre estados, conclusão e reabertura, com inspeção do `localStorage`. | Aprovado: tarefa diretamente movida atualiza `data_atualizacao`; tarefas reindexadas preservam suas datas; no-op não altera metadados nem timestamp global; conclusão define `data_conclusao` igual ao timestamp da operação; reabertura limpa `data_conclusao`. |
| CA5.4 — busca e atalhos | Busca em tempo real e limpeza; correspondência com/sem acentos e sem distinção de maiúsculas/minúsculas; `Ctrl + K` e `Esc`. | Aprovados conforme confirmação do usuário. Os atalhos já haviam sido testados na Fase 2; não foram repetidos nesta rodada. |
| CA5.5 — calendário | Navegação mensal; popover com tarefas no mesmo dia; seleção de tarefa levando ao cartão correspondente, com destaque temporário. | Cenários funcionais aprovados. Após teste com 10 tarefas e observação de ocupação da tela, implementada rolagem vertical interna na lista do popover. Validação visual com mais de 10 itens e em viewport móvel ainda pendente. |
| CA5.6 — resumo e Foco de Hoje | Total, contagens, percentuais, proteção contra divisão por zero e Foco de Hoje calculado pela data local do navegador. | Aprovado: duas tarefas pendentes com vencimento no dia local foram contabilizadas; tarefa concluída foi excluída; cenário sem tarefas exibiu zero sem divisão por zero. |
| CA5.7 — tema | Preferência de tema preservada após recarga. | Aprovado. |
| Datas e vencimentos nos cartões | Datas de vencimento nas tarefas pendentes; data de conclusão nas concluídas; rótulos relativos para ontem/hoje/amanhã; destaque de tarefas pendentes vencidas. | Usuário confirmou testes de datas anteriores, ontem, hoje e amanhã, data de conclusão e destaque de vencidas. Ajuste visual da etiqueta “Vencida” para 14 px e prevenção de quebra de linha implementados; commit `a4e466d` confirmado visualmente pelo usuário. |
| Limitação de compatibilidade | Inicialização em navegador móvel antigo. | Falha de inicialização observada; causa específica não comprovada. Registrar genericamente, sem aparelho/versão; investigação e adaptação fora do escopo imediato. |
| Carregamento inicial | Mensagem transitória “Carregando tarefas...” e indicador de status do Pyodide. | Usuário decidiu remover a mensagem transitória por provocar deslocamento vertical do Kanban. A mensagem e suas referências foram removidas de `index.html`, `js/kanban_ui.js` e `js/app.js`; usuário confirmou após recarga que o Kanban funciona sem o deslocamento e que o indicador de status do Pyodide continua funcionando (RNF07). |

**Estado de validação:** implementação da Fase 5 concluída. CA5.2 a CA5.7 aprovados nos cenários exercitados. CA5.1 permanece parcialmente validado: mouse e alternativa pelo menu aprovados; teste por toque pendente, conforme critério explícito. Caneta não testada. A rolagem vertical interna foi implementada para limitar a altura da lista no popover; a validação com mais de 10 tarefas e em viewport móvel permanece pendente. A remoção da mensagem transitória de carregamento foi validada após recarga; o indicador de status do Pyodide permanece funcional. O aceite integral da Fase 5 depende do teste de toque.

---

## 11. Decisão aprovada — Fase 7: Seleção e Exclusão Coletiva (2026-11-03)

- **Decisão:** incluir a Fase 7 no plano, restrita à seleção múltipla e exclusão coletiva de tarefas.
- **Interface aprovada:** o quadro exibirá um cabeçalho contextual ao ativar o modo de seleção, com ações para selecionar todas, desselecionar todas, informar a quantidade selecionada e excluir as selecionadas. A seleção individual ocorrerá nos cartões. A seleção global abrangerá todas as colunas e estados, inclusive tarefas concluídas. O checkbox de seleção será independente do indicador de conclusão; o menu individual de cada cartão continuará independente.
- **Confirmação:** a exclusão coletiva solicitará confirmação explícita e informará a quantidade de tarefas. Cancelar preserva dados e seleção.
- **Contrato do domínio:** a operação coletiva receberá o estado atual e os IDs selecionados; rejeitará lista vazia, IDs duplicados ou qualquer ID inexistente. Todos os IDs serão validados antes da exclusão, sem exclusão parcial. A operação não modificará a estrutura original recebida, excluirá o conjunto em uma única operação, reindexará somente as colunas afetadas por meio de `reindexar_coluna()`, preservará os metadados das tarefas restantes exceto `ordem`, gerará um único timestamp global e retornará o novo estado e a relação das tarefas excluídas.
- **Reuso técnico:** antes de implementar a nova operação, inspecionar `excluir_tarefa()` e `reindexar_coluna()`. Não executar exclusões individuais em sequência sem avaliar os efeitos intermediários.
- **Persistência e estado da interface:** a seleção será temporária no frontend, sem gravação no `localStorage` ou no backup. A exclusão só será confirmada após persistência bem-sucedida. Em falha, preservar dados, ordenação, interface e seleção; limpar a seleção somente após sucesso.
- **Limites:** não implementar movimentação coletiva, edição coletiva, alteração coletiva de prioridade ou vencimento, mecanismos adicionais de idempotência ou outras operações em lote.
- **Situação:** decisões aprovadas e documentadas; implementação, testes e validação ainda não iniciados.


## 12. Registro de Homologação Manual — Fase 6 (2026-11-03)

Os resultados abaixo foram informados pelo usuário durante a execução dos testes no navegador. A aprovação se limita aos cenários efetivamente exercitados.

| Critério | Verificação e evidência | Resultado |
|---|---|---|
| CA6.1 — Relatórios | Com massa de 30 tarefas: total 30; A Fazer 10 (33,3%); Em Andamento 8 (26,7%); Concluídas 12 (40,0%). | **Aprovado pelo usuário** |
| CA6.2 — Exportação JSON | Arquivo exportado inspecionado: schema 1.0, identificação da aplicação, timestamp ISO, total 30, 30 tarefas, IDs únicos e ordenação contígua por coluna. | **Aprovado após inspeção** |
| CA6.3 — Importação válida | Aplicação informou sucesso na substituição do estado. A inspeção do fluxo de código confirmou encaminhamento para substituição integral do estado e persistência na chave `kanban_app_state`; não é uma operação de acréscimo. | **Aprovado pelo usuário** |
| CA6.4 — Schema incompatível | Arquivo com `versao_schema: "9.9"` foi rejeitado; a validação informou que a versão esperada é `"1.0"`. O usuário confirmou que as 30 tarefas permaneceram intactas. | **Aprovado pelo usuário** |
| CA6.5 — Chave JSON malformada | Chave com aspas incorretas foi rejeitada pelo parser (`JSONDecodeError: Expecting ':' delimiter`, linha 21, coluna 17). O usuário confirmou que as 30 tarefas permaneceram intactas. | **Aprovado pelo usuário** |
| CA6.6 — Valor JSON malformado | Valor contendo caractere de controle inválido foi rejeitado pelo parser (`JSONDecodeError: Invalid control character`, linha 22, coluna 85); o usuário confirmou que as 30 tarefas permaneceram intactas após a rejeição. | **Aprovado pelo usuário** |
| CA6.7 — Cancelamento da importação | Cenário de cancelamento executado; os dados existentes permaneceram inalterados. Critério funcional aprovado. | **Aprovado pelo usuário** |
| CA6.8 — Falha de persistência/rollback | Falha `QuotaExceededError` simulada durante a importação; a aplicação informou que a substituição não foi concluída. As comparações do estado em memória e do `localStorage` retornaram `true`, e o usuário confirmou que o quadro visual permaneceu inalterado. O método original de `Storage.prototype.setItem` foi restaurado. | **Aprovado pelo usuário** |

### Observação de usabilidade

- **Rejeição de JSON inválido (usabilidade):** nos cenários de rejeição, a interface exibia traceback completo do Pyodide/Python. A mensagem apresentada ao usuário deve ser objetiva e amigável; detalhes técnicos permanecem disponíveis no console para diagnóstico. Após a implementação em `js/backup_ui.js`, o usuário validou a mensagem amigável nos cenários de schema diferente de 1.0, chave inválida e valor inválido. A importação válida também foi aprovada.
- **Cancelamento (CA6.7):** comportamento funcional aprovado; não há ajuste pendente neste critério.

### Limites e pendências

- **CA6.8 — Falha de persistência/rollback:** aprovado no cenário de falha simulada durante a importação, conforme evidências registradas na tabela.
- **CA6.9 e CA6.10:** transferidos para o encerramento do projeto como CA7.10 (regressão integrada) e CA7.11 (workflows), após a implementação e os testes específicos da Fase 7.
- A execução local informada de 60 testes, com 96,10% de cobertura de linhas e 92,72% de branches, permanece registrada separadamente; não substitui os critérios manuais pendentes nem a conferência dos workflows.


## 13. Replanejamento do encerramento do projeto — 2026-11-03

- CA6.1–CA6.8 permanecem aprovados; a Fase 6 não fica bloqueada pela regressão integrada ou pela validação dos workflows.
- CA6.9 e CA6.10 foram transferidos para o encerramento, após os testes específicos da Fase 7, como CA7.10 e CA7.11.
- **CA7.10:** regressão integrada RF01–RF16 e RNF01–RNF07, reutilizando evidências anteriores válidas e concentrando novos testes nos impactos, integrações e lacunas. Não repetir indiscriminadamente todos os testes de aceite.
- **CA7.11:** executar e validar os workflows GitHub no estado final, registrando workflow, branch, commit e resultado. Não declarar aprovação sem evidência no GitHub Actions.
- **CA7.12:** validação de segurança com escopo, método, evidências, achados, severidade, correções e retestes documentados. A conclusão deve refletir apenas o escopo efetivamente avaliado; não denominar pentest ou auditoria abrangente sem cobertura correspondente.
- Pendências de acessibilidade e compatibilidade já registradas (toque em CA5.1, leitor de tela, zoom de 200% inconclusivo, rolagem do popover com mais de 10 tarefas e viewport móvel, e auditoria de rede RNF01 parcial) não foram convertidas em aprovações e devem ser reavaliadas conforme impacto e escopo da regressão final.


## 14. Atualização documental da Fase 7 — 2026-11-03

- Atualizados `docs/ESTADO-ATUAL.md`, `docs/PLANO-IMPLEMENTACAO.md`, `docs/REQUISITOS.md` e `CHANGELOG.md` na branch `fase-7-selecao-exclusao-coletiva`.
- Formalizados o cabeçalho contextual, a seleção global e individual, a abrangência das tarefas concluídas e a independência do menu individual.
- Formalizado o contrato de `excluir_tarefas()`: validação integral dos IDs, ausência de exclusão parcial, não mutação da entrada, reindexação apenas das colunas afetadas, preservação de metadados, timestamp global único e retorno das tarefas excluídas.
- Registradas as regras de persistência preventiva, rollback e preservação da seleção em caso de falha.
- Corrigida a inconsistência documental sobre CA6.8: critério aprovado; CA6.9 e CA6.10 permanecem transferidos para CA7.10 e CA7.11.
- **Estado real:** atualização exclusivamente documental. Nenhuma implementação ou teste da Fase 7 foi realizado. A cópia local não foi inspecionada.


## 15. Implementação da Fase 7 — 2026-11-03

- Criada a operação de domínio `excluir_tarefas()`, com validação de lista vazia, tipos inválidos, IDs duplicados e IDs inexistentes antes da exclusão; execução integral sem mutar a entrada; reindexação somente das colunas afetadas; preservação dos metadados restantes, exceto `ordem`; timestamp global único e retorno das tarefas excluídas.
- Exportada a operação pela API pública do pacote e integrada ao dispatcher Pyodide como `excluir_varias`; adicionada a ação `deleteTasks` na API da aplicação, reutilizando o fluxo de persistência preventiva/rollback existente.
- Adicionada seleção independente do indicador de conclusão nos cartões, barra contextual com contagem, selecionar todas/desselecionar todas e diálogo de confirmação com quantidade. A seleção é reconciliada após alterações persistidas e o foco é restaurado ao quadro após limpar a seleção.
- Adicionados testes unitários para exclusão em múltiplas colunas, preservação da entrada/metadados, lista vazia, IDs duplicados, inexistentes e tipos inválidos.
- Atualizados os workflows de interface e Python para considerar a branch da Fase 7.
- **Validação:** alterações gravadas no GitHub; execução da suíte, cobertura, workflows e testes manuais em navegador ainda não confirmados. CA7.1–CA7.9 não recebem aceite apenas pela implementação.


## 16. Atualização da validação da Fase 7 e regressão funcional — 2026-11-03

### Evidências registradas
- **CA7.1–CA7.9:** aprovados pelo usuário nos cenários manuais executados. Incluem seleção individual/global, seleção entre colunas e estados, contagem, confirmação/cancelamento, exclusão coletiva, rollback em falha de persistência, preservação de ordenação/metadados, teclado, foco e viewport móvel de 375 px.
- **CA7.6 — falha de persistência:** simulação de `QuotaExceededError`; memória, armazenamento e seleção permaneceram preservados, com mensagem de erro. O método original de armazenamento foi restaurado ao final.
- **CA7.7 — integridade após exclusão:** após exclusão de duas tarefas, permaneceu uma tarefa persistida com ordem 0 e metadados preservados.
- **CA7.8 — testes automatizados:** `pytest && python scripts/verify_coverage.py`: 65 testes aprovados; cobertura de linhas 95,83% (meta ≥90%) e branches 92,54% (meta ≥85%).
- **CA7.9 — acessibilidade/responsividade:** navegação por Tab, Espaço, Enter e Esc aprovada no fluxo testado; foco retornou ao acionador do diálogo. Em viewport de 375 px, o fluxo testado não apresentou cortes ou sobreposição.
- **CA7.10 — regressão funcional:** RF01–RF16 aprovados pelo usuário nos cenários executados. A aprovação não significa que RNF01–RNF07 estejam integralmente homologados.

### Pendências de validação final
- **RNF01:** auditoria de rede abrangente no GitHub Pages; a evidência anterior é parcial.
- **RNF02:** revisão direcionada da centralização da lógica de negócio em Python e das integrações.
- **RNF03:** além da execução histórica na `main` (`41742344451`), o usuário confirmou execução posterior do workflow Python/cobertura na branch `fase-7-selecao-exclusao-coletiva`, com 65 testes aprovados, 95,83% de cobertura de linhas e 92,54% de branches. O commit testado informado foi `c6feb6b`; não há número de execução registrado nesta documentação.
- **RNF04:** cenário de rollback por falha de gravação validado na Fase 7; preservar também as evidências anteriores da Fase 4 e Fase 6.
- **RNF05:** reteste visual integrado, incluindo sidebar e banner de vencidas, nos breakpoints oficiais.
- **RNF06:** completar verificações WCAG 2.2 AA pertinentes; os testes de teclado realizados não equivalem a auditoria completa nem a teste com leitor de tela.
- **RNF07:** confirmar o indicador de inicialização no estado atual da aplicação.
- **CA7.11:** workflows aprovados na branch `fase-7-selecao-exclusao-coletiva`. `Validar HTML e contraste`: execução `41742982859`, commit `faa12e9514137f24ce8952652b6ae6d6c3e1a72d`. `Testes Python e cobertura`: execução posterior confirmada pelo usuário na branch de trabalho, com 65 testes, 95,83% de linhas e 92,54% de branches; commit informado `c6feb6b`. O identificador da execução Python não foi preservado no registro disponível.
- **CA7.12:** avaliação delimitada em andamento. A inspeção estática e os primeiros testes dinâmicos foram realizados; resultados e lacunas estão na Seção 18.
- A situação da cópia local não foi inspecionada nesta atualização documental.


## 17. Atualização dos workflows GitHub — 2026-11-03

- **Workflow `Validar HTML e contraste`:** execução `41742982859`, branch `fase-7-selecao-exclusao-coletiva`, commit `faa12e9514137f24ce8952652b6ae6d6c3e1a72d`; conclusão `success`. Sintaxe dos módulos JavaScript, auditoria de contraste WCAG 2.2 AA e Nu HTML Checker aprovados.
- **Workflow `Testes Python e cobertura`:** execução `41742344451`, branch `main`, commit `6a967af2aca53a5af5fcfed98e3ff1ea44b8d0d9`; conclusão `success`. 60 testes aprovados; cobertura de linhas 96,10% (meta ≥90%) e branches 92,72% (meta ≥85%). Essa execução é anterior à integração da Fase 7 e não valida a versão atual da branch de trabalho.
- **Conclusão:** CA7.11 parcialmente validado. RNF03 permanece pendente de execução do workflow Python/cobertura na branch `fase-7-selecao-exclusao-coletiva`. A branch `main` não foi alterada nesta atualização documental.

## 18. Revisão documental e avaliação inicial de segurança — 2026-11-03

### 18.1 Estado da revisão documental

A revisão foi realizada na branch `fase-7-selecao-exclusao-coletiva`, a partir do commit-base `c4e8eae81d29d766c5ce02466dcac22c599d688c`. Foram examinados os cinco documentos Markdown versionados: `README.md`, `CHANGELOG.md`, `docs/ESTADO-ATUAL.md`, `docs/PLANO-IMPLEMENTACAO.md` e `docs/REQUISITOS.md`.

- `README.md`: reestruturado para remover um bloco inteiro armazenado como texto com sequências literais `\n`, corrigir informações desatualizadas sobre as fases, workflows e validação, e alinhar a estrutura do repositório aos arquivos existentes.
- `CHANGELOG.md`: convertidas as sequências literais `\n` em quebras reais, consolidados os cabeçalhos repetidos da mesma data e corrigida a ordem cronológica das versões 1.8 e 1.9. Adicionado o registro inicial da CA7.12.
- `docs/REQUISITOS.md`: corrigida a ordem das entradas 1.8 e 1.9. Não foram alterados os requisitos aprovados.
- `docs/PLANO-IMPLEMENTACAO.md`: corrigida a sequência dos títulos das seções de rastreabilidade e histórico, removido um bloco de atualização de validação duplicado com o estado operacional, ordenado o histórico de versões e atualizada a versão para 3.7.
- `docs/ESTADO-ATUAL.md`: esta seção consolida as novas evidências e mantém as pendências explícitas.
- Commits documentais nesta revisão: README `30ece5d6d010e1e2c8e91299cfe895b276aead96`; CHANGELOG `f0361812874b1c6c50b9c9e1ebf638c1957b98b7`; REQUISITOS `34d010e4749070f8da26bc35133590d0d48cfaa3`; PLANO-IMPLEMENTACAO (versão final revisada) `c0989554aad45e83db4e3f5ff97d19ea2df8f168`.
- A branch `main` foi consultada e permanece em `6a967af2aca53a5af5fcfed98e3ff1ea44b8d0d9`; nenhuma gravação foi feita nela. O HEAD final da branch de trabalho é informado no relatório desta revisão.

Não foram encontrados outros blocos de documentação com quebras de linha literais equivalentes ao problema do README/CHANGELOG. Os registros históricos de fases anteriores foram preservados quando ainda explicam decisões ou evidências da época; não foram apagados apenas por estarem desatualizados como fotografia histórica.

### 18.2 Escopo da inspeção estática de segurança

Inspecionados `index.html`, os cinco arquivos CSS, os oito módulos JavaScript, os módulos Python do domínio, `pyproject.toml` e os dois workflows GitHub Actions.

**Resultados favoráveis:**
- Não foram encontrados nos módulos JavaScript os sinks pesquisados: `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `eval` e `new Function`.
- Os conteúdos de tarefas examinados são apresentados com APIs de texto e criação explícita de elementos.
- A importação JSON passa por validação estrita no domínio Python, incluindo estrutura do envelope, campos conhecidos, versão e integridade das tarefas.
- Os workflows declaram permissão `contents: read`.
- Não foi identificada dependência Python de execução declarada em `pyproject.toml`.

**Dependências externas encontradas nos arquivos da aplicação:**
- Google Fonts (`fonts.googleapis.com` e `fonts.gstatic.com`): fonte Inter.
- jsDelivr (`cdn.jsdelivr.net`): distribuição do Pyodide, com versão fixada e HTTPS.
- O link para o repositório GitHub em `index.html` é navegação e não dependência de execução.

**Pontos de atenção preliminares, sem exploração confirmada:**
1. Não foi identificada Content-Security-Policy (CSP) explícita.
2. O script do Pyodide é carregado dinamicamente sem Subresource Integrity (SRI).
3. A importação lê o arquivo JSON integralmente, sem limite explícito de tamanho ou de quantidade de tarefas.
4. As GitHub Actions usam tags (`actions/checkout@v4` e `actions/setup-python@v5`), não SHAs imutáveis.
5. O `localStorage` não é criptografado. Isso é uma limitação de privacidade da arquitetura local; os usuários não devem armazenar segredos ou dados sensíveis na aplicação.

Nenhuma vulnerabilidade crítica ou alta foi confirmada na inspeção estática. Os itens acima são oportunidades de hardening ou limitações, não vulnerabilidades exploradas.

### 18.3 Testes dinâmicos e evidências do usuário

| Cenário | Resultado observado | Estado |
|---|---|---|
| Payload XSS no título de tarefa (`<img src=x onerror=alert(document.domain)>`) | Conteúdo exibido como texto; nenhum alerta foi aberto. | Aprovado neste cenário |
| Payload XSS na descrição (`<svg onload=alert(document.domain)>`) | Conteúdo exibido como texto; nenhum alerta foi aberto. | Aprovado neste cenário |
| Importação de backup contendo payload no título | Arquivo importado normalmente; as três tarefas existentes foram substituídas pela tarefa importada, conforme RF14. O usuário confirmou que o conteúdo foi exibido como texto comum, sem execução. | Aprovado neste cenário |
| Inspeção do `localStorage` | Usuário observou somente propriedades comuns das tarefas, sem credenciais ou dados sensíveis. | Aprovado no escopo observado |

A importação por substituição corresponde ao requisito RF14 vigente. A proposta de oferecer escolha entre substituir e mesclar tarefas não faz parte do escopo aprovado e não foi incorporada.

### 18.4 Limites e próximas verificações da CA7.12

- A lista completa de requisições da página publicada não foi fornecida; a auditoria de rede permanece limitada à requisição Pyodide descrita na Seção 19.
- Concluir os testes dinâmicos controlados restantes de integridade e exposição, sem repetir os testes de importação inválida e rollback já aprovados nas Fases 4 e 6.
- Avaliar a necessidade de limites para tamanho do arquivo e quantidade de tarefas.
- Avaliar medidas de hardening para CSP, SRI e fixação das Actions por SHA, sem alterar o escopo funcional.
- Registrar correções e retestes somente se forem aprovados e implementados.

A CA7.12 permanece **parcialmente concluída**. Esta avaliação é delimitada aos arquivos, cenários e evidências descritos; não constitui pentest nem auditoria abrangente. Nenhuma alteração no código da aplicação foi realizada nesta revisão documental.


## 19. Atualização de validação e situação de encerramento — 2026-11-03

### 19.1 Fase 7 e critérios de encerramento

- **Implementação da Fase 7:** concluída. O escopo funcional aprovado não foi ampliado.
- **CA7.1–CA7.9:** aprovados pelo usuário nos cenários manuais e automatizados registrados na Seção 16.
- **CA7.10:** regressão funcional RF01–RF16 aprovada nos cenários executados. Isso não equivale à homologação integral de todos os requisitos não funcionais.
- **CA7.11 — workflows:** aprovado na branch `fase-7-selecao-exclusao-coletiva`:
  - `Validar HTML e contraste`: execução `41742982859`, commit `faa12e9514137f24ce8952652b6ae6d6c3e1a72d`, conclusão `success`.
  - `Testes Python e cobertura`: execução posterior confirmada pelo usuário na branch de trabalho; 65 testes aprovados, cobertura de linhas de 95,83% e branches de 92,54%; commit informado `c6feb6b`. O identificador da execução não foi preservado no registro disponível.
- **RNF03:** validado para a execução Python/cobertura informada, com as metas mínimas de linhas (90%) e branches (85%) superadas.
- **RNF04:** rollback por falha de persistência validado na Fase 7; evidências anteriores das Fases 4 e 6 permanecem aplicáveis.
- **RNF01:** execução no GitHub Pages confirmada. Na auditoria de rede, foi apresentada a requisição GET ao `https://cdn.jsdelivr.net/pyodide/v314.0.7/full/pyodide-lock.json`, com origem e referenciador `https://josearodrigues.github.io/`, HTTPS e HTTP 200. A lista completa de requisições não foi apresentada; portanto, não se conclui ausência de outras chamadas externas ou de APIs.
- **RNF02:** a regra de ordenação do quadro por coluna/campo `ordem` e a identificação de tarefas vencidas foram centralizadas em Python, com consumo dos resultados via Pyodide. A ordenação alfabética do popover do calendário permanece em JavaScript por ser exclusivamente de apresentação. Na validação manual integrada no navegador, os 30 cartões foram comparados com os registros de `getState()`: a sequência visual correspondeu à sequência dos dados, agrupada em 10 tarefas `a_fazer`, 8 `em_andamento` e 12 `concluida`, com `ordem` crescente em cada coluna. A indicação visual de vencimento coincidiu com a condição esperada em todos os 30 cartões: 14 vencidas e 16 não vencidas/concluídas. Em conjunto com os 68 testes Python aprovados (95,59% de cobertura de linhas e 92,17% de branches) e o workflow de sintaxe JavaScript aprovado, RNF02 está **validado funcionalmente nos cenários examinados**. A evidência não substitui os retestes visuais integrados de RNF05.
- **RNF05:** reteste visual integrado da sidebar e do banner de tarefas vencidas nos breakpoints oficiais permanece pendente.
- **RNF06:** workflow de contraste aprovado e verificações de teclado/foco registradas. Não houve teste com leitor de tela nem evidência suficiente para declarar conformidade WCAG 2.2 AA integral.
- **RNF07:** além da inspeção estática do elemento inicial `Inicializando...` em `index.html` e das transições no `js/app.js`, o usuário confirmou no navegador a exibição de `Inicializando...` durante a carga e `✓ Carregado` após a inicialização do Pyodide. **Validado funcionalmente para os estados de carregamento e sucesso.** O estado de erro não foi provocado nem testado.
- **CA5.1 (Fase 5):** homologação por toque continua pendente; não foi considerada concluída por inferência.

### 19.2 Atualização da CA7.12 — avaliação delimitada de segurança

- O usuário confirmou que o payload XSS inserido no título durante a importação do backup foi exibido como texto comum, sem execução. O teste complementa os cenários já aprovados para título e descrição.
- A inspeção do `localStorage` não identificou credenciais ou dados sensíveis nos dados observados; o armazenamento permanece em texto claro, sem criptografia.
- A requisição de rede apresentada na versão publicada foi o carregamento do lockfile do Pyodide via jsDelivr (HTTPS, HTTP 200). Como não foi fornecida a lista completa de Network → All, a auditoria de tráfego é parcial.
- Permanecem como pontos de hardening, sem exploração confirmada: ausência de CSP explícita, ausência de SRI no carregamento dinâmico do Pyodide, ausência de limite explícito de tamanho do arquivo de importação e uso de tags de versão nas GitHub Actions em vez de SHAs imutáveis.
- Não foi confirmada vulnerabilidade crítica ou alta no escopo estático e dinâmico examinado. A conclusão limita-se aos arquivos e cenários descritos; não representa pentest nem auditoria abrangente.

### 19.3 Conclusão operacional

A **Fase 7 está implementada e funcionalmente aprovada**. A Etapa 6 — Validação Final permanece em andamento até a resolução ou aceitação formal das pendências listadas nesta seção, incluindo CA5.1 e as verificações RNF01, RNF05 e RNF06. RNF02 foi validado funcionalmente nos cenários de integração registrados na Seção 21; RNF07 foi validado para carregamento e sucesso. Não declarar o projeto integralmente homologado neste estado.

- **Branch de trabalho:** `fase-7-selecao-exclusao-coletiva`.
- **HEAD remoto consultado antes desta atualização documental:** `b53a921afdd1cdb4de60a13fa55eaaa6c9d32e96`.
- **Branch `main`:** não foi alterada nesta atualização.
- **Código da aplicação:** nenhuma alteração realizada nesta atualização; somente documentação.
- **Cópia local:** não inspecionada; sincronização local não confirmada.


## 20. Revisão técnica de RNF02 e RNF07 — 2026-11-03

### RNF02 — centralização da lógica em Python

**Evidências favoráveis**
- `js/pyodide_bridge.js` carrega os módulos `models.py`, `services.py`, `metrics.py` e `schema.py` no runtime Pyodide.
- A ponte encaminha operações de criação, edição, movimentação, exclusão individual/coletiva, validação de estado, importação/exportação, métricas e relatórios para funções do pacote `todolist`.
- As regras de entidade, invariantes, validação de schema, cálculos estatísticos e operações de domínio estão implementadas nos módulos Python examinados.
- `js/app.js` concentra a coordenação da interface, persistência e chamadas ao núcleo Python, sem substituir os serviços de domínio.

**Implementação aplicada em 03/11/2026**
- Criada em `src/todolist/metrics.py` a função `preparar_apresentacao_kanban()`, responsável por ordenar as tarefas pela sequência das colunas e pelo campo `ordem`, além de identificar os IDs de tarefas vencidas usando a data local de referência.
- A função foi exportada em `src/todolist/__init__.py` e integrada ao dispatcher e à API de `js/pyodide_bridge.js`.
- `js/app.js` solicita a preparação ao Python antes de cada renderização do quadro, inclusive após alterações persistidas e em rollback.
- `js/kanban_ui.js` passou a consumir a lista ordenada e os IDs vencidos fornecidos pelo Python. Foram removidos da interface o cálculo da condição de vencimento e a ordenação por `ordem` em JavaScript.
- A ordenação alfabética de tarefas no popover do calendário permanece em `js/calendar_ui.js`, por ser ordenação exclusivamente de apresentação, sem efeito sobre o domínio ou a ordem persistida.
- Acrescentados três testes unitários em `tests/test_metrics.py`, cobrindo ordenação, identificação de vencidas e rejeição de data inválida.

**Validação pendente**
- Workflow `Testes Python e cobertura`: execução `41753321406`, commit `c37ff886`, resultado `success`; 68 testes aprovados, cobertura de linhas 95,59% e branches 92,17%.
- Workflow `Validar HTML e contraste`: execução `41753384763`, commit `5adc302`, resultado `success`; sintaxe dos módulos JavaScript, contraste WCAG 2.2 AA e Nu HTML Checker aprovados.
- A integração funcional navegador/Pyodide ainda precisa ser conferida após a atualização.
- Portanto, RNF02 permanece **em validação**; não se declara o requisito aprovado até a conferência do comportamento do quadro no navegador.

### RNF07 — indicador de inicialização

**Evidência estática**
- `index.html` apresenta inicialmente `Inicializando...` no elemento `#pyodide-status`.
- `js/app.js` atualiza o indicador para carregamento no início de `inicializarAplicacao()`, para sucesso após a inicialização do runtime Pyodide e para erro quando a inicialização falha.
- `css/components.css` contém estilos para os estados carregado e erro.

**Conclusão:** implementação encontrada e coerente no código. O usuário confirmou no navegador os estados `Inicializando...` e `✓ Carregado`; RNF07 está validado funcionalmente para carregamento e sucesso. O estado `⚠ Erro` permanece sem teste dinâmico, portanto não se afirma que os três estados foram homologados.


### RNF05 e CA5.1 — inspeção estática responsiva e de toque

- Os estilos definem breakpoints em 1280 px, 960 px e 767 px. Até 960 px, a navegação lateral passa a ser recolhível e as colunas do Kanban são empilhadas; até 767 px, cabeçalho, formulários e barra de seleção passam a layouts de coluna.
- O banner de tarefa vencida usa largura de 100%, dimensionamento com `box-sizing: border-box` e altura mínima de 32 px. O cartão permite quebra de texto no título e descrição.
- Há regra específica para ponteiro coarse: `touch-action: none` no cartão e alvo mínimo de 40 × 40 px no resumo do menu da tarefa. Isso demonstra preparação para interação por toque, mas não comprova usabilidade real em dispositivo touchscreen.
- **Conclusão:** inspeção estática não substitui o reteste visual integrado da sidebar e do banner nos breakpoints oficiais, nem a homologação por toque CA5.1. Ambos permanecem pendentes de execução manual.

### Escopo desta revisão

- Arquivos examinados: `js/app.js`, `js/pyodide_bridge.js`, `js/kanban_ui.js`, `js/calendar_ui.js`, `js/backup_ui.js`, `js/drag_drop.js`, `js/reports_ui.js`, `js/storage.js`, módulos Python do domínio e requisito RNF02 em `docs/REQUISITOS.md`.
- Não foram executados testes nem alterado código da aplicação nesta revisão.
- RNF02 permanece parcial; RNF07 foi validado funcionalmente nos estados de carregamento e sucesso. O estado de erro permanece sem teste dinâmico.


### Atualização de implementação RNF02 — 2026-11-03

- Centralizada em Python a preparação da ordenação do quadro e a identificação de tarefas vencidas; removidos os cálculos correspondentes do renderizador JavaScript.
- Mantida em JavaScript somente a ordenação alfabética do calendário, classificada como apresentação.
- Incluídos três testes unitários em `tests/test_metrics.py`; execução ainda pendente.
- Commits de implementação: `7010d1b` (função Python), `4bff746` (exportação), `c37ff88` (testes), `ac821f7` (ponte Pyodide), `3b51168` (renderizador) e `fdabfde`/`5adc302` (integração e correção da renderização inicial).
- RNF02 permanece em validação: testes automatizados e sintaxe JavaScript aprovados; integração funcional no navegador ainda pendente.


## 21. Validação funcional integrada de RNF02 — 2026-11-03

### Procedimento e evidências no navegador

- Após sincronizar a branch de trabalho por `git pull --ff-only`, o usuário recarregou a aplicação local. O console confirmou o carregamento do pacote `todolist` no Pyodide 0.314.0.7 e a inicialização da aplicação, com a API disponível em `window.kanbanApp`.
- A API `getState()` retornou 30 tarefas. A inspeção dos registros mostrou 10 tarefas em `a_fazer` (ordens 0–9), 8 em `em_andamento` (ordens 0–7) e 12 em `concluida` (ordens 0–11).
- A inspeção dos 30 elementos `.task-card`, usando `data-task-id`, confirmou que a sequência de cartões na interface corresponde à sequência dos IDs retornados por `getState()`. Assim, a ordem exibida corresponde aos estados e valores de `ordem` observados.
- Para cada tarefa, foi comparada a condição de vencimento esperada (estado diferente de concluída, prazo não nulo e prazo anterior à data local) com a classe visual `is-overdue`. Resultado: **30/30 consistentes**, sendo 14 tarefas vencidas e 16 sem indicação de vencimento.
- O aviso do console sobre a instrução WebAssembly `try` obsoleta foi acompanhado das mensagens de carregamento do pacote e inicialização bem-sucedida. Não foi observada falha de inicialização; o aviso, isoladamente, não invalida o teste.

### Resultado

- **RNF02: validado funcionalmente nos cenários examinados.** A preparação Python integrada ao Pyodide alimentou corretamente a ordenação do quadro e a indicação visual de tarefas vencidas.
- A validação cobre a amostra atual de 30 tarefas e o fluxo de inicialização/renderização observado. Não representa prova de todos os estados possíveis nem substitui a regressão de outros requisitos.
- A Etapa 6 permanece em andamento. Continuam pendentes as verificações de RNF01, RNF05 e RNF06, a homologação por toque CA5.1 e a conclusão formal da avaliação delimitada CA7.12.

## 22. Encerramento do projeto — 2026-11-03

### Decisão de encerramento

O projeto To-Do List Kanban está **encerrado para fins da entrega acadêmica**, com base na implementação das sete fases, na aprovação dos critérios funcionais exercitados, na regressão RF01–RF16 dos cenários executados e nos resultados de automação registrados. O encerramento não significa homologação integral de todos os requisitos não funcionais nem elimina as limitações abaixo.

A decisão prioriza a conclusão do desafio e evita reabrir funcionalidades ou repetir testes já realizados. Não foram aprovadas novas funcionalidades nem alterações de código para esta etapa de encerramento.

### Estado consolidado

- **Etapas 1 a 5:** concluídas quanto à descoberta, especificação, arquitetura, planejamento e implementação. As fases funcionais foram implementadas; as limitações de homologação manual remanescentes estão explicitadas a seguir.
- **Fase 7:** CA7.1–CA7.9 aprovados nos cenários executados; regressão RF01–RF16 aprovada nos cenários exercitados.
- **Automação:** workflows HTML/contraste e Python/cobertura aprovados na branch de trabalho. A execução Python registrada após a Fase 7 informou 65 testes aprovados, 95,83% de cobertura de linhas e 92,54% de branches. A integração RNF02 também possui validação posterior no navegador com 30 tarefas.
- **RNF02, RNF03 e RNF04:** validados no escopo das evidências registradas.
- **RNF07:** estados de carregamento e sucesso confirmados; o estado de erro não foi provocado.

### Limitações aceitas e não conformidades não declaradas como aprovadas

| Item | Situação no encerramento |
|---|---|
| RNF01 / CA4.1 | Aplicação executada no GitHub Pages e requisição do lockfile Pyodide observada com HTTP 200. A captura completa de tráfego não foi realizada; auditoria de rede parcial. |
| RNF05 | Há evidências anteriores de inspeção visual em Desktop, Tablet e Mobile. O reteste visual integrado final não foi concluído; observações pontuais de layout não justificam reabrir a implementação nesta entrega. |
| RNF06 | Nu HTML Checker, contraste e parte dos testes de teclado/foco foram aprovados. Não houve teste com leitor de tela; não se declara conformidade WCAG 2.2 AA integral. |
| RNF07 | Carregamento e sucesso validados; estado de erro sem teste dinâmico. |
| CA5.1 | Interação por toque em dispositivo físico não homologada por indisponibilidade de ambiente de teste. |
| CA7.12 | Inspeção estática e testes dinâmicos delimitados realizados. Nenhuma vulnerabilidade crítica ou alta foi confirmada no escopo examinado; a avaliação não equivale a pentest ou auditoria abrangente. Pontos de hardening permanecem registrados na Seção 19. |
| Usabilidade visual | Pequenas observações de apresentação foram registradas durante a inspeção final. Não foi comprovado impedimento funcional que justifique reabrir o escopo. |

### Situação de versionamento e publicação

- Branch de trabalho: `fase-7-selecao-exclusao-coletiva`.
- Esta consolidação é exclusivamente documental e será registrada na branch de trabalho.
- A branch `main` não foi alterada por esta atualização.
- Push da branch de trabalho, integração/push final, exclusão das branches temporárias e criação da tag `v1.0.0` permanecem sob execução do usuário, com orientação do assistente.
- Não há declaração de release/tag criada ou de publicação final decorrente deste registro.

### Critério de conclusão

O desafio está documentalmente encerrado para a entrega acadêmica. As limitações acima permanecem transparentes e não impedem considerar concluído o trabalho planejado dentro do escopo e dos recursos de validação disponíveis.
