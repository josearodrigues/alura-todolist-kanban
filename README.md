# To-Do List Kanban — v1.0.0

Aplicação web de gerenciamento de tarefas no formato Kanban, desenvolvida em Python como **Desafio 3** da iniciativa [Imersão Engenharia de Software: Dev na Era da IA](https://www.alura.com.br/), promovida pela Alura em parceria com o Google for Startups.

> Projeto educacional independente. Não é um produto oficial nem representa endosso da Alura ou do Google.

O projeto aplica conceitos de Engenharia de Software desde a definição dos requisitos e o planejamento técnico até a implementação, os testes, a validação e a documentação.

## Acesse o projeto

- **Aplicação publicada:** https://josearodrigues.github.io/alura-todolist-kanban/
- **Repositório:** https://github.com/josearodrigues/alura-todolist-kanban
- **Versão:** [v1.0.0](https://github.com/josearodrigues/alura-todolist-kanban/tree/v1.0.0)

## Sobre a aplicação

O To-Do List Kanban permite organizar tarefas em três etapas de execução:

- **A Fazer:** tarefas ainda não iniciadas.
- **Em Andamento:** tarefas em execução.
- **Concluídas:** tarefas finalizadas.

A aplicação utiliza Python como núcleo das regras de negócio, executado diretamente no navegador por meio do Pyodide e WebAssembly. A interface é construída com HTML5, CSS3 e JavaScript ES Modules.

Os dados são armazenados localmente no navegador, sem necessidade de um backend próprio.

## Funcionalidades

- Quadro Kanban com três colunas e movimentação de tarefas.
- Criação, edição, reordenação e exclusão individual.
- Seleção e exclusão coletiva com confirmação.
- Busca por título e descrição.
- Calendário com navegação mensal e identificação de vencimentos.
- Resumo do projeto com indicadores e percentuais.
- Foco de Hoje para acompanhamento das tarefas relevantes.
- Relatórios com indicadores calculados pelo domínio Python.
- Exportação e importação de backups JSON com validação.
- Temas claro e escuro.
- Interface responsiva e recursos de acessibilidade por teclado.
- Persistência local com preservação do estado anterior em caso de falha de gravação.

## Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python 3.14 | Domínio, validações, serviços, métricas e regras de negócio |
| Pyodide / WebAssembly | Execução de Python no navegador |
| HTML5 | Estrutura semântica da aplicação |
| CSS3 | Layout, componentes, temas e responsividade |
| JavaScript ES Modules | Interface, interações, integração com Python e persistência |
| pytest e pytest-cov | Testes automatizados e cobertura do domínio Python |
| GitHub Actions | Automação das verificações e testes |
| Nu HTML Checker | Validação estrutural do HTML |

A aplicação carrega o runtime Pyodide pelo CDN jsDelivr e utiliza a fonte Inter do Google Fonts.

## Arquitetura e organização

A solução separa as responsabilidades entre o domínio Python, a interface Web e os mecanismos de persistência.

- **Domínio Python:** concentra as entidades, regras de negócio, validações e cálculos.
- **Pyodide:** executa os módulos Python no navegador por WebAssembly.
- **JavaScript:** integra o domínio à interface e coordena as interações e a persistência.
- **localStorage:** armazena os dados das tarefas no próprio navegador.

### Estrutura do repositório

```text
alura-todolist-kanban/
├── .github/workflows/       # Workflows de validação
├── css/                     # Tokens, layout, Kanban e componentes
├── docs/                    # Requisitos, plano, estado e referências
├── js/                      # Interface, Pyodide, persistência e interações
├── scripts/                 # Verificação de cobertura e contraste
├── src/todolist/            # Domínio, serviços, métricas e schema Python
├── tests/                   # Testes automatizados e fixtures
├── CHANGELOG.md
├── index.html
├── LICENSE
├── pyproject.toml
└── README.md
```

## Como executar localmente

### Requisitos

- Python 3.14 para executar os testes automatizados.
- Navegador moderno para utilizar a aplicação.
- Conexão com a internet para carregar o Pyodide e a fonte externa.

### Iniciar a aplicação

Na raiz do repositório, execute:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Acesse:

```text
http://127.0.0.1:8000
```

Para encerrar o servidor, pressione `Ctrl+C`.

O servidor disponibiliza os arquivos localmente. A aplicação executa o Python no próprio navegador e armazena as tarefas no `localStorage`.

Em um navegador sem dados salvos, o quadro inicia vazio.

## Como executar os testes

### Instalar dependências

```bash
python -m pip install -e ".[dev]"
```

### Executar a suíte automatizada

```bash
pytest
```

### Verificar a cobertura

```bash
python scripts/verify_coverage.py
```

Também é possível executar os dois procedimentos em sequência:

```bash
pytest && python scripts/verify_coverage.py
```

### Metas de qualidade

| Indicador | Meta |
|---|---:|
| Aprovação dos testes | 100% |
| Cobertura de linhas | ≥ 90% |
| Cobertura de branches | ≥ 85% |

## Evidências de validação

Os resultados abaixo correspondem a execuções registradas durante o desenvolvimento e encerramento acadêmico do projeto.

| Verificação | Evidência | Resultado |
|---|---|---|
| Testes Python e cobertura | [Workflow 41753321406](https://github.com/josearodrigues/alura-todolist-kanban/actions/runs/41753321406) | 68 testes aprovados; 95,59% de linhas e 92,17% de branches |
| HTML, JavaScript e contraste | [Workflow 41753384763](https://github.com/josearodrigues/alura-todolist-kanban/actions/runs/41753384763) | Workflow aprovado |
| Integração Python/Pyodide | Inspeção funcional no navegador | Ordem e vencimento consistentes nas 30 tarefas examinadas |
| Regressão funcional | RF01–RF16 | Aprovada nos cenários exercitados |
| Persistência e rollback | Testes manuais de falha | Estado anterior preservado nos cenários registrados |

**Importante:** os dois workflows foram executados em commits diferentes. Portanto, não se afirma que ambos validaram exatamente o mesmo snapshot do código. Os resultados são registros históricos, não uma nova execução realizada durante a leitura deste documento.

## Limites conhecidos da validação

A versão foi encerrada para fins acadêmicos com ressalvas documentadas. Isso não significa homologação integral de todos os requisitos não funcionais.

- **RNF01 — Hospedagem e comunicação:** execução no GitHub Pages confirmada; auditoria completa de tráfego não realizada.
- **RNF05 — Responsividade:** houve inspeção visual em Desktop, Tablet e Mobile, mas o reteste visual integrado final não foi concluído.
- **RNF06 — Acessibilidade:** HTML, contraste e parte dos testes de teclado e foco foram verificados. Não houve teste com leitor de tela; não se declara conformidade integral com WCAG 2.2 AA.
- **RNF07 — Feedback:** estados de carregamento e sucesso foram confirmados; o estado de erro não foi testado dinamicamente.
- **CA5.1 — Interação por toque:** teste físico em dispositivo com tela sensível ao toque não realizado.
- **CA7.12 — Segurança:** avaliação delimitada, sem confirmação de vulnerabilidade crítica ou alta no escopo examinado. Não equivale a pentest ou auditoria abrangente.

A matriz completa de evidências, decisões e limitações está em [docs/ESTADO-ATUAL.md](docs/ESTADO-ATUAL.md), especialmente na Seção 22.

## Documentação

A documentação do projeto mantém a rastreabilidade entre requisitos, decisões técnicas, implementação e validação.

- [Requisitos do projeto](docs/REQUISITOS.md)
- [Plano de implementação](docs/PLANO-IMPLEMENTACAO.md)
- [Estado atual e evidências](docs/ESTADO-ATUAL.md)
- [Histórico de alterações](CHANGELOG.md)

## Contexto acadêmico e ferramentas de IA

O projeto foi desenvolvido no contexto do **Desafio 3 — To-Do List Kanban**, da Imersão Engenharia de Software: Dev na Era da IA.

O desenvolvimento contou com o apoio do **Google Antigravity** e do **ChatGPT** em atividades de análise, planejamento, implementação, revisão e documentação.

O uso de ferramentas de inteligência artificial foi acompanhado da análise das propostas, compreensão das decisões técnicas e validação dos resultados.

O princípio de aprendizagem adotado foi:

**Compreender, implementar, validar e explicar.**

## Licença

Este projeto está disponibilizado sob a licença [MIT](LICENSE).

Consulte o arquivo de licença para conhecer os termos de utilização, modificação e distribuição.
