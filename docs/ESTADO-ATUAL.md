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
  - *Branch remota de trabalho:* `fase-5-interacoes`
  - *Branch remota:* `fase-5-interacoes` (criada anteriormente pelo usuário; implementação remota em andamento).
  - *Histórico remoto:* a Fase 1 culminou no commit `0ef5cf4`. A Fase 2 foi registrada em `main` por meio dos commits de implementação HTML e atualizações documentais; a pipeline Nu HTML Checker foi adicionada no commit `11f6cdf`; a correção HTML foi registrada em `a6c7495` e o diagnóstico detalhado da pipeline em `58558ad`. A implementação CSS da Fase 3 e a auditoria de contraste foram adicionadas diretamente à `main` nesta sessão.
  - *Situação local/remota:* comparação remota `main...fase-5-interacoes`: branch de trabalho à frente da `main`, sem commits atrás na comparação registrada; a `main` permanece sem alterações nesta implementação. A cópia local não foi inspecionada nesta sessão.
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
- Criadas telas demonstrativas estáticas para Relatórios, Importar/Exportar e Configurações, além do Calendário. As telas de Relatórios e Importar/Exportar permanecem demonstrativas, conforme escopo da Fase 6; o calendário foi integrado funcionalmente na Fase 5.
- Workflow `41560866108` aprovado no commit `db37ac91`: Nu HTML Checker sem erros/avisos e auditoria de contraste aprovada. Inspeção visual manual e aceite do usuário ainda pendentes.

## 3. Estado da Governança Documental

A tríade documental mandatória encontra-se plenamente estabelecida e atualizada:
- **`docs/REQUISITOS.md`:** Atualizado (Versão 1.7 — RNF06 alinhado aos critérios normativos de contraste WCAG 2.2 AA).
- **`docs/PLANO-IMPLEMENTACAO.md`:** Atualizado (Versão 2.1 — plano aprovado; situação da Etapa 4 e autorização da Fase 1 alinhadas ao estado real, com registro da revisão corretiva).
- **`docs/ESTADO-ATUAL.md`:** Atualizado com o estado operacional corrente (este documento).
- **`README.md`:** Atualizado com tecnologias, estrutura do projeto, instruções de execução, testes, roteiro manual da Fase 2 e roteiro de inspeção visual da Fase 3.
- **`CHANGELOG.md`:** Registra as alterações implementadas por fase.
- **`LICENSE`:** Licença MIT.

---

## 4. Situação de Cada Etapa e Fase do Projeto

| Etapa / Fase | Situação | Descrição / Entregáveis |
| :--- | :--- | :--- |
| **Etapa 1 — Descoberta e Requisitos** | **Concluída e Aprovada** | Levantamento via método Grill Me; requisitos aprovados. |
| **Etapa 2 — Planejamento Funcional** | **Concluída e Aprovada** | Especificação consolidada de RF01–RF15, RNF01–RNF07 e regras de negócio. |
| **Etapa 3 — Arquitetura Técnica** | **Concluída e Aprovada** | Sete decisões técnicas aprovadas, arquitetura modular e critérios de testes definidos. |
| **Etapa 4 — Plano de Implementação** | **Concluída e Aprovada** | Plano de Implementação (versão 2.1) formalmente aprovado pelo usuário. |
| **Etapa 5 — Implementação Controlada** | **Em andamento** | Fase 1 concluída e validada; Fase 2 implementada, com validação manual parcial; Fase 3 implementada e inspeção visual aprovada; Fase 4 implementada e validada funcionalmente pela API JS/Python, com auditoria de rede parcial; Fase 5 implementada na branch `fase-5-interacoes`, com validação manual parcial e pendências descritas nesta seção; Fase 6 implementada; testes automatizados e homologação manual pendentes. |
| ↳ *Fase 1: Domínio Python e Testes* | **Concluída e Validada** | Pacote `src/todolist/`, `pyproject.toml`, testes automatizados (`tests/`) e `scripts/verify_coverage.py` implementados. Após a revisão corretiva, o procedimento oficial aprovou 48/48 testes, com 96,16% de cobertura de linhas e 92,78% de branches. |
| ↳ *Fase 2: HTML e Acessibilidade* | **Implementada; validação manual parcial** | `index.html` contém estrutura semântica, três colunas, widgets, formulários, seis diálogos nativos, template de cartão, nomes acessíveis, atalhos e gerenciamento de foco. Foram aprovadas 20 verificações automatizadas gerais em Chromium; os seis diálogos também foram exercitados individualmente. Nu HTML Checker: execução `41520632228`, zero erros e zero avisos. Na verificação manual desta sessão: `Tab`, `Shift + Tab`, `Enter`, `Espaço`, `Ctrl + K`, foco inicial/contenção/restauração no diálogo Nova Tarefa e fechamento desse diálogo por `Esc` aprovados pelo usuário. Menu contextual não testado: controle `⋮` está desativado; usuário também identificou divergência visual do ícone em relação ao mockup. Inspeção visual dos rótulos/nome dos controles sem problemas aparentes, mas leitor de tela não testado. Validação formal da fase permanece parcial; itens não verificados não são considerados aprovados. |
| ↳ *Fase 3: CSS e Validação Visual* | **Implementada; inspeção visual manual concluída** | Refinamentos visuais e mocks estáticos mantidos. Navegação lateral recolhível em telas de até 960 px, com fechamento por `Esc`, clique no fundo e seleção de seção, restauração e contenção de foco; ícone `⋮` ajustado visualmente, sem ativar o menu contextual. Usuário aprovou Desktop, Tablet (1024 × 768) e Mobile (390 × 844), nos temas Claro e Escuro. Teste manual de `prefers-reduced-motion` também aprovado. Workflow `41553398236`: 25 combinações de contraste aprovadas, zero reprovações e Nu HTML Checker sem erros/avisos. CA3.1–CA3.5 considerados atendidos conforme as evidências registradas; não implica validação funcional das telas demonstrativas. |
| ↳ *Fase 4: WebAssembly e Persistência* | **Implementada; validação funcional concluída, CA4.1 parcialmente verificado** | Pyodide 314.0.7 e importação dos cinco módulos confirmados. Criação, edição, movimentação e exclusão executadas pela API JS/Python; persistência, timestamp e recuperação após recarga confirmados nas quatro operações. Falhas simuladas nas quatro operações preservaram memória e armazenamento; notificação visual observada na criação. CA4.2–CA4.6 atendidos conforme as evidências registradas. No GitHub Pages, o usuário confirmou o carregamento e observou, no filtro Fetch/XHR durante a carga, uma requisição ao CDN jsDelivr para `pyodide-lock.json` (HTTP 200), sem chamadas a APIs de backend nessa amostra. Como a auditoria ficou restrita ao filtro e ao período observado, CA4.1 permanece parcialmente verificado, não homologado integralmente. |
| ↳ *Fase 5: Interações (Pointer Events)* | **Implementada; validação manual parcial** | CA5.2 a CA5.7 aprovados nos cenários exercitados, exceto CA5.1, que permanece parcial por falta de teste de toque. Mouse e alternativa acessível pelo menu foram aprovados. CA5.5 aprovado no cenário exercitado. Após observação de usabilidade com 10 tarefas no mesmo dia, foi implementada rolagem vertical interna no popover; validação visual com listas extensas e em viewport móvel ainda pendente. Correção do menu contextual, datas relativas, destaque de vencidas e remoção da mensagem transitória de carregamento foram implementados e validados pelo usuário. A implementação da Fase 5 está concluída; aceite integral aguarda teste de toque em CA5.1. |
| ↳ *Fase 6: Relatórios e Backup JSON* | Implementada; validação pendente | Modal de relatórios com métricas Python e filtro por data de conclusão; exportação JSON versionada; importação estrita, confirmação com contadores e substituição transacional. Testes automatizados ampliados; execução dos workflows e homologação manual ainda pendentes. |
| **Etapa 6 — Validação Final** | **Não iniciada** | Homologação integrada e testes de aceitação. |

---

## 5. Matriz de Rastreabilidade

- **Planejado:** Aplicação To-Do Kanban estática com Python via WebAssembly (Pyodide), 3 colunas, drag and drop via Pointer Events, calendário integrado, métricas em tempo real e backup JSON.
- **Aprovado:** Versão 1.7 de Requisitos (RNF06 alinhado à WCAG 2.2 AA), Etapa 3 (Arquitetura Técnica) e Etapa 4 (Plano de Implementação, versão 2.1) formalmente aprovadas.
- **Implementado:** Em 2026-11-03, a interface da Fase 3 recebeu refinamento visual e dados demonstrativos estáticos para tarefas, calendário, resumo e status. Na branch `revisao-visual-d83bbee`, a correção posterior adicionou navegação lateral recolhível em telas de até 960 px e ajustou o símbolo `⋮`; o controle contextual estava desabilitado nessa revisão visual; foi ativado na implementação da Fase 5. Fase 1 implementada: pacote Python `src/todolist/`, configuração, testes e script de cobertura. Fase 2 implementada em `index.html`; workflow Nu HTML Checker criado. Fase 4 implementada na branch `fase-4-pyodide-persistencia`, com ponte JS/Python, Pyodide e persistência local; testes funcionais da API concluídos. Fase 5 implementada na branch `fase-5-interacoes`, com validação manual parcial; Fase 6 implementada na branch `fase-6-relatorios-backup`, com validação automatizada e manual pendentes.
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

- **Ambiente Git:** repositório remoto `josearodrigues/alura-todolist-kanban`, branch de trabalho `fase-5-interacoes`. A situação da cópia local não foi verificada nesta sessão. O registro histórico de validação da Fase 4 foi executado pelo usuário no navegador local, com a aplicação servida por HTTP. Naquela ocasião, o usuário confirmou a cópia local alinhada à branch remota e sem alterações pendentes. Isso não confirma o estado local atual.
- **Fase 4 — implementação:** Pyodide 314.0.7 inicializado; cinco módulos Python carregados no filesystem virtual; pacote `todolist` importado; API disponível em `window.kanbanApp`.
- **Fase 4 — operações e persistência:** criação, edição, movimentação e exclusão executadas pela API JS/Python. O conteúdo de `kanban_app_state` e o timestamp foram conferidos após as operações. Recuperação após recarga confirmada para criação, edição, movimentação e exclusão. As três últimas recuperações foram verificadas nesta sessão, com resultados apresentados pelo usuário no console.
- **Fase 4 — falha de persistência:** `Storage.prototype.setItem` foi interceptado temporariamente para simular falha nas quatro operações. Em todos os casos, a alteração foi impedida e o estado anterior permaneceu em memória e no `localStorage`. A notificação de erro foi observada na interface durante o teste de criação; não há confirmação visual independente para as outras três operações.
- **Fase 4 — critérios de aceite:** CA4.2 confirmado pelo usuário (indicador `✓ Carregado`); CA4.3 demonstrado no console; CA4.4 e CA4.5 validados com execução das quatro operações e recuperação após recarga; CA4.6 validado quanto ao rollback nas quatro operações, com notificação visual observada na criação. Para CA4.1, o usuário confirmou a execução no GitHub Pages. Na auditoria realizada, o filtro Fetch/XHR apresentou apenas uma requisição ao CDN jsDelivr (`pyodide-lock.json`, HTTP 200) e nenhuma chamada a API de backend. A observação foi limitada a esse filtro e à carga da página; portanto, CA4.1 permanece parcialmente verificado.
- **Interface:** notificações de erro reposicionadas no topo; barra inferior removida e créditos/versão transferidos para a sidebar. Tipografia dos créditos compactada e conteúdo organizado em três linhas. Ajustes implementados na branch anterior; validação visual final dos últimos créditos ainda não registrada.
- **Registro inicial da validação da Fase 5 (2026-11-03):** as verificações iniciais de criação, edição, exclusão, movimentação, busca, calendário, indicadores, tema e reordenação foram ampliadas pelos resultados mais recentes consolidados na Seção 10. As observações de menu contextual aberto após cancelamento, ciclo de conclusão/reabertura pendente e Foco de Hoje pendente foram resolvidas/validadas posteriormente; consultar a tabela atualizada da Seção 10. Permanecem sem teste o toque em CA5.1 e o cenário adicional de grande volume no popover. A mensagem transitória de carregamento foi removida e validada após recarga; o indicador de status do Pyodide continua funcionando. A limitação observada em navegador móvel antigo está registrada genericamente, sem aparelho ou versão. Workflow `db37ac91`: Nu HTML Checker sem erros/avisos e auditoria de contraste aprovada. A implementação da Fase 5 está concluída; o aceite integral aguarda o teste de toque exigido por CA5.1.
- **Situação local:** antes da rodada de testes funcionais, o usuário confirmou a branch local alinhada à origem e sem alterações pendentes.

---

## 8. Próxima Ação Recomendada

1. Realizar, quando houver dispositivo disponível, o teste manual de drag and drop por toque exigido em CA5.1; registrar o resultado por dispositivo.
2. O cenário de grande volume no popover permanece como verificação adicional não realizada, sem defeito identificado e sem constituir critério de aceite explícito.
3. Não iniciar a Fase 6 até concluir a revisão e o aceite da Fase 5.
5. Manter CA4.1 como parcialmente verificado; não antecipar `replaceState` nem importação, pertencentes à Fase 6.

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