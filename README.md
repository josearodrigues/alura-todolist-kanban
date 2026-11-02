# To-Do List Kanban | Engenharia de Software

Aplicação web de gerenciamento de tarefas no formato **Kanban**, desenvolvida como **Desafio 3** da *Imersão Engenharia de Software: Dev na Era da IA*, iniciativa da **Alura Imersões** em parceria com o **Google for Startups**.

O projeto utiliza Python como linguagem central para as regras de negócio e foi planejado para execução integral no navegador por meio de WebAssembly, com hospedagem estática no GitHub Pages. A implementação segue fases controladas, com requisitos, decisões técnicas, critérios de aceitação e evidências registrados na documentação.

O desenvolvimento tem finalidade educacional: praticar Engenharia de Software por meio da compreensão dos requisitos, planejamento, implementação, testes, validação e explicação das decisões. Ferramentas de inteligência artificial podem apoiar atividades do processo, mas não substituem a análise técnica nem a compreensão do código.

> **Estado atual:** Fase 1 (domínio Python e testes) concluída e validada. Fase 2 (HTML e acessibilidade estrutural) implementada, com validação automática de HTML aprovada; o checklist manual ainda está pendente. As Fases 3 a 6 não foram iniciadas. A aplicação ainda não está publicada para uso final no GitHub Pages.

Este projeto é independente, não é um produto oficial da Alura ou do Google e não representa endosso dessas organizações.

---

## O que você encontra neste projeto

- **Quadro Kanban:** estrutura com três colunas — A Fazer, Em Andamento e Concluídas — e contadores.
- **Domínio em Python:** entidade de tarefa, validações, regras de transição entre estados, serviços, métricas e validação do contrato JSON.
- **Acessibilidade estrutural:** HTML semântico, navegação por teclado, nomes acessíveis, foco visível e diálogos nativos.
- **Planejamento funcional:** requisitos para criação, edição, movimentação, reordenação, busca, calendário, relatórios, importação, exportação e alternância de tema.
- **Validação automatizada:** testes Python com pytest e workflow do GitHub Actions para o Nu HTML Checker.
- **Documentação de engenharia:** requisitos, decisões arquiteturais, plano de implementação, estado atual e histórico de alterações.

As funcionalidades de interação e persistência ainda não integradas permanecem desabilitadas na interface. A lista acima não significa que todos esses recursos estejam disponíveis nesta etapa.

---

## Tecnologias e recursos

| Tecnologia / Recurso | Utilização |
|---|---|
| Python 3.14 ou superior | Linguagem central e implementação do domínio |
| pytest | Testes automatizados do domínio Python |
| pytest-cov | Medição de cobertura de linhas e branches |
| HTML5 | Estrutura semântica da interface |
| JavaScript | Comportamentos mínimos de teclado e abertura/fechamento dos diálogos nesta fase |
| HTML Dialog | Estrutura nativa dos diálogos |
| GitHub Actions | Automação da validação de HTML |
| Nu HTML Checker | Verificação de conformidade do HTML |
| GitHub Pages | Hospedagem estática prevista para a aplicação final |
| Pyodide / WebAssembly | Execução de Python no navegador, prevista para a Fase 4 |

A tabela distingue tecnologias já utilizadas daquelas previstas na arquitetura e nas próximas fases.

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
- **`scripts/`:** ferramentas auxiliares de validação, incluindo a verificação de cobertura.
- **`docs/`:** requisitos, plano de implementação, estado operacional e referência visual aprovada.
- **`.github/workflows/`:** automação da validação HTML.
- **`index.html`:** estrutura atual da interface web.

A arquitetura prevê módulos JavaScript e CSS separados nas fases correspondentes. Eles não devem ser considerados componentes já implementados.

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

**Importante:** nesta etapa, a página apresenta a estrutura HTML e os recursos de acessibilidade implementados. O layout visual definitivo depende da Fase 3; a execução do domínio Python no navegador depende da Fase 4. Os controles de operações de negócio permanecem desabilitados até a integração correspondente.

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
- Checklist manual de acessibilidade ainda pendente.

Os resultados acima registram as evidências já obtidas; não representam uma nova execução dos testes nesta atualização documental. A validação automatizada não substitui a inspeção manual prevista no plano.

---

## Fases de Desenvolvimento

| Fase | Escopo | Situação |
|---|---|---|
| 1. Domínio Python e testes | Entidade, regras de negócio, serviços, métricas, schema e testes | Concluída e validada |
| 2. HTML e acessibilidade | Estrutura semântica, diálogos, teclado, foco e validação HTML | Implementada; checklist manual pendente |
| 3. CSS e validação visual | Design system, temas, responsividade e contraste WCAG 2.2 AA | Não iniciada |
| 4. WebAssembly e persistência | Integração Pyodide, execução Python no navegador e persistência local | Não iniciada |
| 5. Interações | Movimentação, reordenação, busca e calendário | Não iniciada |
| 6. Relatórios e backup JSON | Relatórios, exportação e importação com validação e consistência | Não iniciada |

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

## Acessibilidade e Verificação Manual da Fase 2

A estrutura atual inclui navegação semântica, link para pular ao conteúdo principal, rótulos associados aos campos, nomes acessíveis, foco visível, atalho de busca e diálogos nativos.

Para concluir a verificação manual desta fase:

1. Use `Tab` e `Shift + Tab` para percorrer os controles.
2. Use `Enter` ou `Espaço` para ativar os controles apropriados.
3. Pressione `Ctrl + K` e confirme o foco no campo de busca.
4. Abra cada diálogo e verifique o foco inicial, a permanência do foco dentro dele e o retorno ao controle de origem.
5. Pressione `Esc` para fechar o diálogo ou menu contextual ativo.
6. Verifique a abertura e o fechamento do menu contextual pelo teclado.
7. Confira os rótulos dos campos e os nomes acessíveis dos controles.

Registre cada item como **Aprovado**, **Reprovado** ou **Não aplicável**, anotando o comportamento observado. O roteiro também está descrito no plano de implementação. A inspeção visual completa será realizada após a Fase 3.

---

## Limitações Conhecidas

- A interface ainda não possui o layout CSS definitivo.
- O domínio Python está implementado e testado, mas ainda não está integrado ao navegador por Pyodide.
- Persistência no navegador, movimentação interativa, busca funcional, calendário, relatórios e backup ainda não foram implementados.
- Os controles correspondentes às funcionalidades não integradas permanecem desabilitados.
- O checklist manual da Fase 2 ainda precisa ser executado.
- A aplicação final ainda não foi homologada nem publicada no GitHub Pages.

---

## Estado do Projeto

- **Fase 1:** concluída e validada.
- **Fase 2:** implementada; validação automática de HTML aprovada; checklist manual pendente.
- **Fases 3 a 6:** não iniciadas.
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
