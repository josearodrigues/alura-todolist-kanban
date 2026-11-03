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
  - *Ações realizadas nesta revisão:* correções de código, testes e documentação registradas diretamente na branch `main`. Nenhuma tag, release ou publicação da aplicação foi criada. Último commit de código conhecido: `db37ac91` (refino do status e calendário).
- **Mockup Oficial de Referência:**
  - Arquivo `Painel Kanban de Tarefas Pastel.png`, localizado na Biblioteca do projeto Desafios Alura e consultado durante a revisão visual de 2026-11-02/03.
  - O PNG histórico versionado em `docs/design/referencias/todolist-kanban-1.0-mockup.png` permanece preservado intacto.

---

## 2.1 Revisão de fidelidade ao mockup e telas secundárias — 2026-11-03\n\n- Reestabelecida a hierarquia da barra superior: busca à esquerda; indicador verde “Aplicação Online” e alternância de tema à direita; sem avatar/identificação de usuário no cabeçalho; mascote ilustrativo mantido na barra lateral.\n- Saudação preservada como “Olá!” conforme requisito aprovado, com ilustração de mão acenando.\n- Reintroduzidas as descrições das três colunas; refinados ícones, cores e tipografia.\n- Calendário lateral com cabeçalho azul-marinho, mês, setas visuais e grade alinhada a novembro de 2025; criado painel de calendário em tela própria. Os controles de mês estão desabilitados, pois a navegação funcional pertence à Fase 5.\n- Resumo corrigido: 7 tarefas; 2 concluídas (29%) e 5 pendentes (71%), sendo pendentes a soma de A Fazer + Em Andamento. Restauradas duas barras de progresso independentes (concluídas e pendentes).\n- Rodapé recuperou o crédito completo “Desenvolvido com Python • Pyodide • ♥ Alura + Google for Startups”, com versão e última atualização à direita.\n- Criadas telas demonstrativas estáticas para Relatórios, Importar/Exportar e Configurações, além do Calendário. Ações e dados dessas telas não são funcionais; integrações permanecem nas fases previstas.\n- Workflow `41560866108` aprovado no commit `db37ac91`: Nu HTML Checker sem erros/avisos e auditoria de contraste aprovada. Inspeção visual manual e aceite do usuário ainda pendentes.\n\n## 3. Estado da Governança Documental

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
| ↳ *Fase 2: HTML e Acessibilidade* | **Implementada; validação manual parcial** | `index.html` contém estrutura semântica, três colunas, widgets, formulários, seis diálogos nativos, template de cartão, nomes acessíveis, atalhos e gerenciamento de foco. Foram aprovadas 20 verificações automatizadas gerais em Chromium; os seis diálogos também foram exercitados individualmente. Nu HTML Checker: execução `41520632228`, zero erros e zero avisos. Na verificação manual desta sessão: `Tab`, `Shift + Tab`, `Enter`, `Espaço`, `Ctrl + K`, foco inicial/contenção/restauração no diálogo Nova Tarefa e fechamento desse diálogo por `Esc` aprovados pelo usuário. Menu contextual não testado: controle `⋮` está desativado; usuário também identificou divergência visual do ícone em relação ao mockup. Inspeção visual dos rótulos/nome dos controles sem problemas aparentes, mas leitor de tela não testado. Validação formal da fase permanece parcial; itens não verificados não são considerados aprovados. |
| ↳ *Fase 3: CSS e Validação Visual* | **Implementada; inspeção visual manual concluída** | Refinamentos visuais e mocks estáticos mantidos. Navegação lateral recolhível em telas de até 960 px, com fechamento por `Esc`, clique no fundo e seleção de seção, restauração e contenção de foco; ícone `⋮` ajustado visualmente, sem ativar o menu contextual. Usuário aprovou Desktop, Tablet (1024 × 768) e Mobile (390 × 844), nos temas Claro e Escuro. Teste manual de `prefers-reduced-motion` também aprovado. Workflow `41553398236`: 25 combinações de contraste aprovadas, zero reprovações e Nu HTML Checker sem erros/avisos. CA3.1–CA3.5 considerados atendidos conforme as evidências registradas; não implica validação funcional das telas demonstrativas. |
| ↳ *Fase 4: WebAssembly e Persistência* | Implementação registrada; validação local pendente | Pyodide 314.0.7 via CDN; cinco módulos no virtual FS; ponte JS ↔ Python; estado JSON único em `localStorage`; confirmação pós-gravação e notificação em falha. Arquivos: `js/pyodide_bridge.js`, `js/storage.js`, `js/app.js`, `index.html` e `css/components.css`. CA4.1–CA4.6 ainda não homologados. |
| ↳ *Fase 5: Interações (Pointer Events)* | Não iniciada | Drag and drop unificado, touch, menu acessível, busca e calendário. |
| ↳ *Fase 6: Relatórios e Backup JSON* | Não iniciada | Modal de relatórios, exportação e importação atômica estrita. |
| **Etapa 6 — Validação Final** | **Não iniciada** | Homologação integrada e testes de aceitação. |

---

## 5. Matriz de Rastreabilidade

- **Planejado:** Aplicação To-Do Kanban estática com Python via WebAssembly (Pyodide), 3 colunas, drag and drop via Pointer Events, calendário integrado, métricas em tempo real e backup JSON.
- **Aprovado:** Versão 1.7 de Requisitos (RNF06 alinhado à WCAG 2.2 AA), Etapa 3 (Arquitetura Técnica) e Etapa 4 (Plano de Implementação, versão 2.1) formalmente aprovadas.
- **Implementado:** Em 2026-11-03, a interface da Fase 3 recebeu refinamento visual e dados demonstrativos estáticos para tarefas, calendário, resumo e status. Na branch `revisao-visual-d83bbee`, a correção posterior adicionou navegação lateral recolhível em telas de até 960 px e ajustou o símbolo `⋮` para pontos verticais sólidos. O controle contextual continua desabilitado; apenas sua apresentação foi corrigida. Fase 1 implementada: pacote Python `src/todolist/` (`models.py`, `services.py`, `metrics.py`, `schema.py`, `__init__.py`), configuração `pyproject.toml`, suíte `tests/` e script `scripts/verify_coverage.py`. Fase 2 implementada em `index.html`; workflow `.github/workflows/validar-html.yml` criado para validação Nu HTML Checker. Fases 4 a 6 não iniciadas.
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

- **Ambiente Git:** Repositório remoto `josearodrigues/alura-todolist-kanban`, branch de trabalho `revisao-visual-d83bbee`; alterações desta sessão registradas diretamente na branch remota. A cópia local não foi inspecionada.
- **Implementação e validação manual:** Fase 1 concluída e validada. Fase 2 implementada e submetida a 20 verificações automatizadas; Nu HTML Checker sem erros/avisos. Checklist manual parcialmente executado: `Tab`, `Shift + Tab`, `Enter`, `Espaço`, `Ctrl + K`, gerenciamento de foco e `Esc` no diálogo Nova Tarefa aprovados pelo usuário. Menu contextual permanece desativado; leitor de tela não testado. Fase 3: estilos modulares, temas, responsividade e movimento reduzido implementados; workflow `41553398236` aprovado (25 combinações, zero reprovações; HTML sem erros/avisos). Inspeção manual aprovada nos seis cenários de breakpoint/tema e teste de `prefers-reduced-motion` aprovado pelo usuário. Fases 4 a 6 permanecem não iniciadas.

---

## 8. Próxima Ação Recomendada

1. **Fase 4 — implementação remota registrada:** Pyodide 314.0.7, carregamento dos cinco módulos Python, ponte JS ↔ Python e persistência preventiva em `localStorage` foram implementados na branch `fase-4-pyodide-persistencia`. A gravação antecede a confirmação do estado em memória e a atualização do quadro; falhas são notificadas sem aplicar o candidato.
2. **Validação pendente com o usuário:** executar a aplicação localmente por servidor HTTP, confirmar carregamento do runtime e importação de `todolist`, testar criação, edição, movimentação e exclusão com recarga da página e simular falha de `localStorage.setItem`. Só depois registrar os critérios CA4 correspondentes como aprovados.
3. **Fase 5:** não iniciada. Não antecipar drag and drop, busca, calendário ou ativação dos controles dos cartões nesta etapa.
