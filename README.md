# To-Do List Kanban — v1.0.0

Aplicação web de gerenciamento de tarefas no formato Kanban, desenvolvida como **Desafio 3** da *Imersão Engenharia de Software: Dev na Era da IA* (Alura + Google for Startups).

<sub>Projeto educacional independente. Não é produto oficial nem representa endosso da Alura ou do Google.</sub>

A aplicação utiliza Python como núcleo das regras de negócio, executado no navegador por WebAssembly (Pyodide). A interface usa HTML, CSS e JavaScript ES Modules; os dados são persistidos localmente no navegador.

**Versão:** [tag anotada v1.0.0](https://github.com/josearodrigues/alura-todolist-kanban/tree/v1.0.0)  
**Repositório:** [josearodrigues/alura-todolist-kanban](https://github.com/josearodrigues/alura-todolist-kanban)

## Funcionalidades

- Quadro Kanban com as colunas A Fazer, Em Andamento e Concluídas.
- Criação, edição, movimentação, reordenação e exclusão individual de tarefas.
- Seleção e exclusão coletiva com confirmação.
- Busca por título e descrição, calendário, resumo do projeto e Foco de Hoje.
- Relatórios calculados pelo domínio Python.
- Exportação e importação de backup JSON com validação estrita e confirmação.
- Temas claro e escuro, layout responsivo e recursos de acessibilidade por teclado.
- Persistência local com preservação do estado anterior em caso de falha de gravação.

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python 3.14 | Modelo, validações, serviços, métricas e regras de negócio |
| Pyodide / WebAssembly | Execução de Python no navegador |
| HTML5 e CSS3 | Estrutura, componentes, temas e responsividade |
| JavaScript ES Modules | Interface, integração com Pyodide e persistência local |
| pytest e pytest-cov | Testes automatizados e cobertura do domínio Python |
| GitHub Actions | Validação de HTML/JavaScript/contraste e testes Python/cobertura |
| Nu HTML Checker | Verificação do HTML |

A aplicação carrega a fonte Inter do Google Fonts e o Pyodide do CDN jsDelivr.

## Estrutura do repositório

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

### Documentação

- [Requisitos](docs/REQUISITOS.md)
- [Plano de Implementação](docs/PLANO-IMPLEMENTACAO.md)
- [Estado Atual e ressalvas da entrega](docs/ESTADO-ATUAL.md)
- [Changelog](CHANGELOG.md)

## Executar localmente

Requisitos: Python 3.14 para os testes. Para executar a aplicação web, use um navegador moderno e um servidor HTTP local.

Na raiz do repositório:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Abra http://127.0.0.1:8000 no navegador. O servidor fica acessível somente no computador local. Para encerrá-lo, pressione `Ctrl+C`.

As tarefas são armazenadas em `localStorage`. Em um navegador sem dados salvos, o quadro inicia vazio. O Pyodide e os módulos Python são carregados pelo navegador.

## Executar os testes Python

Instale as dependências de desenvolvimento:

```bash
python -m pip install -e ".[dev]"
```

Execute a suíte e a verificação de cobertura:

```bash
pytest && python scripts/verify_coverage.py
```

Metas do projeto:
- 100% de aprovação dos testes;
- cobertura de linhas igual ou superior a 90%;
- cobertura de branches igual ou superior a 85%.

## Evidências da versão acadêmica

| Verificação | Evidência registrada | Resultado |
|---|---|---|
| Testes Python e cobertura | [Workflow 41753321406](https://github.com/josearodrigues/alura-todolist-kanban/actions/runs/41753321406), commit `c37ff886` | 68 testes aprovados; 95,59% linhas; 92,17% branches |
| HTML, JavaScript e contraste | [Workflow 41753384763](https://github.com/josearodrigues/alura-todolist-kanban/actions/runs/41753384763), commit `5adc3021` | Sucesso |
| RNF02 — integração Python/Pyodide | Inspeção funcional no navegador com 30 tarefas | Ordem e vencimento consistentes em 30/30 tarefas examinadas |
| RF01–RF16 | Regressão funcional manual | Aprovada nos cenários exercitados |
| Persistência / rollback | Testes manuais de falha | Estado anterior preservado nos cenários registrados |

Os workflows foram aprovados em commits diferentes; não se afirma que ambos avaliaram o mesmo snapshot. Os resultados acima são evidências históricas registradas, não uma execução realizada durante a leitura deste README.

## Limites conhecidos da validação

A versão foi encerrada para fins acadêmicos, com ressalvas documentadas. Não se declara homologação integral de todos os requisitos não funcionais.

- **RNF01:** execução no GitHub Pages confirmada; auditoria completa de tráfego não realizada.
- **RNF05:** há inspeção visual anterior em Desktop, Tablet e Mobile; o reteste visual integrado final não foi concluído.
- **RNF06:** HTML, contraste e parte dos testes de teclado/foco foram verificados; leitor de tela não testado. Não se declara conformidade WCAG 2.2 AA integral.
- **RNF07:** estados de carregamento e sucesso confirmados; estado de erro não testado dinamicamente.
- **CA5.1:** teste físico por toque não realizado.
- **CA7.12:** avaliação de segurança delimitada; nenhuma vulnerabilidade crítica ou alta foi confirmada no escopo examinado. Não equivale a pentest ou auditoria abrangente.

A matriz completa de evidências, decisões e limitações está em [docs/ESTADO-ATUAL.md](docs/ESTADO-ATUAL.md), Seção 22.

## Licença

Disponibilizado sob a licença [MIT](LICENSE).
