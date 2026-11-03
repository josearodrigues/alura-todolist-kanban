# To-Do List Kanban | Engenharia de Software

Aplicação web de gerenciamento de tarefas no formato **Kanban**, desenvolvida como **Desafio 3** da *Imersão Engenharia de Software: Dev na Era da IA*, iniciativa da **Alura Imersões** em parceria com o **Google for Startups**.

O projeto utiliza Python como linguagem central para as regras de negócio e foi planejado para execução integral no navegador por meio de WebAssembly, com hospedagem estática no GitHub Pages. A implementação segue fases controladas, com requisitos, decisões técnicas, critérios de aceitação e evidências registrados na documentação.

O desenvolvimento tem finalidade educacional: praticar Engenharia de Software por meio da compreensão dos requisitos, planejamento, implementação, testes, validação e explicação das decisões. Ferramentas de inteligência artificial podem apoiar atividades do processo, mas não substituem a análise técnica nem a compreensão do código.

> **Estado atual (03/11/2026):** Fase 1 concluída e validada; Fase 2 implementada com validação manual parcial; Fase 3 implementada e inspecionada; Fase 4 implementada e validada funcionalmente pela API JS/Python, com CA4.1 parcialmente verificado. A implementação da Fase 5 está concluída na branch `fase-5-interacoes`, com pendência de homologação por toque em CA5.1. A Fase 6 está implementada na branch `fase-6-relatorios-backup`; execução automatizada e homologação manual dos critérios CA6.1–CA6.7 ainda pendentes.

Este projeto é independente, não é um produto oficial da Alura ou do Google e não representa endosso dessas organizações.

---

## O que você encontra neste projeto

- **Quadro Kanban:** três colunas com cartões renderizados a partir do estado persistido, contadores dinâmicos e menus para editar, mover e excluir tarefas.
- **Domínio em Python:** entidade de tarefa, validações, regras de transição entre estados, serviços, métricas e validação do contrato JSON.
- **Acessibilidade estrutural:** HTML semântico, navegação por teclado, nomes acessíveis, foco visível e diálogos nativos.
- **Interações da Fase 5:** busca por título e descrição com normalização de acentos; drag and drop por Pointer Events; movimentação pelo menu contextual; calendário mensal com marcadores e popover; resumo e Foco de Hoje calculados pelo domínio Python.
- **Validação automatizada:** testes Python com pytest e workflow do GitHub Actions para o Nu HTML Checker.
- **Documentação de engenharia:** requisitos, decisões arquiteturais, plano de implementação, estado atual e histórico de alterações.

A Fase 5 já foi exercitada manualmente nos cenários descritos em `docs/ESTADO-ATUAL.md`; permanece pendente o teste por toque exigido em CA5.1. A mensagem transitória de carregamento foi removida e validada. Relatórios dinâmicos, exportação JSON e importação com validação estrita e substituição transacional foram implementados na Fase 6; consulte `docs/ESTADO-ATUAL.md` para o estado de validação.

---

## Tecnologias e recursos

| Tecnologia / Recurso | Utilização |
|---|---|
| Python 3.14 ou superior | Linguagem central e implementação do domínio |
| pytest | Testes automatizados do domínio Python |
| pytest-cov | Medição de cobertura de linhas e branches |
| HTML5 | Estrutura semântica da interface |
| CSS3 modular | Design system, temas claro/escuro e layout responsivo (Fase 3) |
| Python (script padrão) | Auditoria matemática das combinações de contraste WCAG 2.2 AA |
| JavaScript ES Modules | Ponte com Pyodide, persistência local e coordenação da inicialização (Fase 4) |
| HTML Dialog | Estrutura nativa dos diálogos |
| GitHub Actions | Automação da validação de HTML |
| Nu HTML Checker | Verificação de conformidade do HTML |
| GitHub Pages | Hospedagem estática prevista para a aplicação final |
| Pyodide 314.0.7 / WebAssembly | Execução de Python 3.14.2 no navegador via CDN (Fase 4) |

A tabela distingue tecnologias já utilizadas daquelas previstas na arquitetura e nas próximas fases. A alternância de tema claro/escuro foi implementada na Fase 3 e salva a preferência visual no navegador; isso não representa a implementação da persistência das tarefas.

---

## Estrutura do Projeto

```text
alura-todolist-kanban/
├── .github/
│   └── workflows/
│       └── validar-html.yml
├── docs/
│   ├── design/
│   │   └── referencias/
│   │       └── todolist-kanban-1.0-mockup.png
│   ├── ESTADO-ATUAL.md
│   ├── PLANO-IMPLEMENTACAO.md
│   └── REQUISITOS.md
├── scripts/
│   └── verify_coverage.py
├── src/
│   └── todolist/
│       ├── __init__.py
│       ├── metrics.py
│       ├── models.py
│       ├── schema.py
│       └── services.py
├── tests/
├── CHANGELOG.md
├── index.html
├── LICENSE
├── pyproject.toml
└── README.md
```

- **`src/todolist/`:** pacote Python com o modelo de domínio, serviços, métricas e validação do schema.
- **`tests/`:** testes automatizados do domínio.
- **`css/`:** tokens de design, estilos base, layout responsivo, quadro Kanban e componentes.
- **`js/`:** inicialização da aplicação, ponte Pyodide, persistência, renderização Kanban, drag and drop e calendário.
- **`scripts/`:** ferramentas auxiliares de validação, incluindo a verificação de cobertura e a auditoria de contraste.
- **`docs/`:** requisitos, plano de implementação, estado operacional e referência visual aprovada.
- **`.github/workflows/`:** automação da validação HTML.
- **`index.html`:** estrutura atual da interface web.

Os módulos JavaScript da Fase 4 e da Fase 5 estão presentes. A validação funcional em navegador da Fase 5 foi realizada parcialmente; consulte `docs/ESTADO-ATUAL.md` para os critérios aprovados e pendentes.

---

## Como Executar

### Requisitos

- Python **3.14 ou superior** para instalar e executar o projeto Python, conforme declarado em `pyproject.toml`.
- Navegador moderno para visualizar a estrutura HTML.
- Git, caso deseje clonar o repositório.

### Visualizar a interface atual

Na raiz do repositório, execute:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Acesse:

```text
http://127.0.0.1:8000
```

O servidor disponibiliza os arquivos estáticos localmente e fica restrito ao próprio computador. Para encerrá-lo, volte ao terminal e pressione `Ctrl+C`.

**Importante:** a aplicação carrega tarefas a partir do `localStorage`. Em um navegador sem estado salvo, o quadro inicia vazio. O Pyodide carrega os módulos Python no navegador; criação, edição, movimentação e exclusão usam a ponte JS/Python e a persistência preventiva. A interface da Fase 5 foi validada manualmente de forma parcial; consulte o estado atual para os limites da validação.

---

## Como Executar os Testes Automatizados

Os testes Python utilizam `pytest` e `pytest-cov`, declarados como dependências opcionais de desenvolvimento.

### Instalar as dependências de desenvolvimento

Na raiz do repositório:

```bash
python -m pip install -e ".[dev]"
```

### Executar a suíte e verificar a cobertura

```bash
pytest && python scripts/verify_coverage.py
```

O procedimento oficial exige aprovação integral dos testes, cobertura de linhas de pelo menos 90% e cobertura de branches de pelo menos 85%.

### Resultados registrados

**Fase 1 — Domínio Python e testes**

- **48/48 testes aprovados**.
- **96,16%** de cobertura de linhas.
- **92,78%** de cobertura de branches.
- Procedimento oficial executado com sucesso.

**Fase 2 — HTML e acessibilidade**

- **20 verificações automatizadas gerais em Chromium aprovadas**.
- Os seis diálogos foram exercitados individualmente quanto ao foco inicial, contenção do foco, fechamento por `Esc` e restauração do foco.
- Nu HTML Checker: **zero erros e zero avisos** na execução [41520632228](https://github.com/josearodrigues/alura-todolist-kanban/actions/runs/41520632228).
- Checklist manual de acessibilidade parcialmente executado em 03/11/2026; resultados e pendências estão registrados abaixo.

Os resultados acima registram as evidências já obtidas; não representam uma nova execução dos testes nesta atualização documental. A validação automatizada não substitui a inspeção manual prevista no plano.

---

## Fases de Desenvolvimento

| Fase | Escopo | Situação |
|---|---|---|
| 1. Domínio Python e testes | Entidade, regras de negócio, serviços, métricas, schema e testes | Concluída e validada |
| 2. HTML e acessibilidade | Estrutura semântica, diálogos, teclado, foco e validação HTML | Implementada; checklist manual pendente |
| 3. CSS e validação visual | Design system, temas, responsividade, mocks e contraste WCAG 2.2 AA | Implementada; inspeção visual aprovada conforme registro |
| 4. WebAssembly e persistência | Integração Pyodide, execução Python no navegador e persistência local | Implementada e validada funcionalmente; CA4.1 parcialmente verificado |
| 5. Interações | Movimentação, reordenação, busca e calendário | Implementação inicial registrada; testes locais/manuais pendentes |
| 6. Relatórios e backup JSON | Relatórios, exportação e importação com validação e consistência | Implementada; validação automatizada e homologação manual pendentes |

Após as seis fases, o plano prevê uma etapa de validação final e homologação. Os critérios detalhados de conclusão estão em [docs/PLANO-IMPLEMENTACAO.md](docs/PLANO-IMPLEMENTACAO.md).

---

## Requisitos e Comportamentos Planejados

A aplicação final deverá contemplar:

- Criação de tarefas sempre no estado **A Fazer**.
- Edição dos campos permitidos, preservando os atributos controlados pelo domínio.
- Movimentação entre as três colunas e reordenação manual independente da prioridade.
- Busca por título e descrição, com suporte ao atalho `Ctrl + K`.
- Calendário integrado, resumo do projeto e indicadores de prazos.
- Relatórios calculados pelas rotinas Python.
- Exportação e importação de backup JSON com validação estrutural estrita.
- Persistência local com preservação do estado anterior em caso de falha de gravação.
- Temas claro e escuro, responsividade e acessibilidade conforme WCAG 2.2 nível AA.

Esses itens descrevem o escopo aprovado, não funcionalidades já concluídas. A especificação completa e as regras de negócio estão em [docs/REQUISITOS.md](docs/REQUISITOS.md).

---

## Verificação Visual da Fase 3\n\nA Fase 3 introduziu folhas de estilo modulares, temas claro e escuro, layout adaptativo e suporte a movimento reduzido. Para completar a validação, abra a aplicação localmente e inspecione:\n\n1. Desktop: largura igual ou superior a 1200 px.\n2. Tablet: largura entre 768 px e 1199 px.\n3. Mobile: largura inferior a 768 px.\n4. Cada uma das três larguras nos temas claro e escuro.\n5. Alternância de tema, recarga da página e preservação da preferência selecionada.\n6. Preferência de movimento reduzido ativada no sistema operacional ou navegador.\n\nA auditoria matemática está disponível pelo comando `python scripts/check_contrast.py`. O workflow do GitHub Actions também foi configurado para executá-la quando houver alterações relevantes em CSS ou no script. A inspeção visual humana e a confirmação da execução no Actions ainda precisam ser registradas.\n\n---\n\n## Acessibilidade e Verificação Manual da Fase 2

A estrutura atual inclui navegação semântica, link para pular ao conteúdo principal, rótulos associados aos campos, nomes acessíveis, foco visível, atalho de busca e diálogos nativos.

### Resultados da verificação manual — 03/11/2026

| Verificação | Resultado | Observação |
|---|---|---|
| `Tab` e `Shift + Tab` | **Aprovado** | Navegação nos controles testados. |
| `Enter` e `Espaço` | **Aprovado** | Ativação dos controles apropriados testados. |
| `Ctrl + K` | **Aprovado** | Foco direcionado ao campo de busca. |
| Diálogo Nova Tarefa: foco inicial, contenção e restauração | **Aprovado** | Confirmado pelo usuário nesse diálogo. |
| `Esc` no diálogo Nova Tarefa | **Aprovado** | O diálogo foi fechado. |
| `Esc` no menu contextual | **Pendente** | Menu contextual indisponível/desativado. |
| Navegação por teclado no menu contextual | **Pendente** | Controle `⋮` desativado; não foi possível abrir o menu. |
| Rótulos e identificação visual | **Sem problema visual observado** | Não equivale a teste com leitor de tela. |
| Nomes acessíveis com leitor de tela | **Não testado** | Requer validação específica com tecnologia assistiva. |

O checklist foi executado parcialmente. Não declarar a Fase 2 integralmente validada enquanto as pendências dos critérios CA2.3–CA2.6 não forem resolvidas ou justificadas. O ícone do menu `⋮` também foi apontado pelo usuário como divergente do mockup; a correção visual fica registrada para a etapa apropriada.

### Itens ainda previstos no roteiro

- Abrir e testar os demais diálogos individualmente, verificando foco inicial, contenção e retorno ao controle de origem.
- Verificar o comportamento contextual de `Esc` na busca e nos demais componentes ativos, conforme CA2.3.
- Verificar menus contextuais e formulários de criação/edição por teclado, conforme CA2.5.
- Inspecionar foco visível, estados e nomes acessíveis; realizar teste com leitor de tela se aplicável ao critério de aceite.

A inspeção visual completa da Fase 3 será realizada separadamente, após a conclusão das pendências da Fase 2.

---

## Limitações Conhecidas

- A Fase 5 ainda não recebeu aceite integral: movimentação por toque/caneta não foi testada; o popover com grande volume de tarefas também não foi exercitado.
- Foi observada falha de inicialização em navegador móvel antigo. A causa não foi comprovada; a limitação será mantida registrada de forma genérica, sem identificar aparelho ou versão. A investigação de compatibilidade não integra a próxima ação imediata.
- A mensagem transitória “Carregando tarefas...” foi removida para evitar deslocamento vertical do Kanban; o usuário confirmou após recarga o funcionamento do quadro e do indicador de status do Pyodide.
- Relatórios detalhados e importação/exportação permanecem reservados à Fase 6.

---

## Estado do Projeto

- **Fase 1:** concluída e validada.
- **Fase 2:** implementada; validação automática de HTML aprovada; checklist manual pendente.
- **Fase 3:** implementada; inspeção visual aprovada conforme registro.
- **Fase 4:** implementada e validada funcionalmente; CA4.1 parcialmente verificado.
- **Fase 5:** implementação registrada na branch `fase-5-interacoes`; validação manual parcial. CA5.2, CA5.3, CA5.4, CA5.6 e CA5.7 aprovados nos cenários exercitados; CA5.1 parcial (toque/caneta não testados). Pendente: teste de drag and drop por toque previsto em CA5.1.
- **Fase 6:** não iniciada.
- **Validação final:** pendente.
- **Publicação no GitHub Pages:** ainda não realizada.

O registro operacional atualizado prevalece sobre este resumo: [docs/ESTADO-ATUAL.md](docs/ESTADO-ATUAL.md).

---

## Contexto Acadêmico e Licença

Este projeto foi desenvolvido como atividade do **Desafio 3** da *Imersão Engenharia de Software: Dev na Era da IA*, no contexto da iniciativa educacional da **Alura Imersões** em parceria com o **Google for Startups**.

O objetivo é aplicar práticas de Engenharia de Software em um projeto evolutivo, com rastreabilidade entre requisitos, decisões, implementação e validação. A participação de ferramentas de IA no processo não elimina a responsabilidade de compreender o código, avaliar as sugestões e comprovar os resultados.

O projeto está disponibilizado sob a licença [MIT](LICENSE). Consulte o arquivo para conhecer os termos de uso, modificação e distribuição.

---

## Documentação

- [Requisitos do Projeto](docs/REQUISITOS.md)
- [Plano de Implementação](docs/PLANO-IMPLEMENTACAO.md)
- [Estado Atual](docs/ESTADO-ATUAL.md)
- [Histórico de Alterações](CHANGELOG.md)
- [Licença MIT](LICENSE)

Sugestões e relatos de problemas podem ser registrados por meio das *Issues* do repositório.
