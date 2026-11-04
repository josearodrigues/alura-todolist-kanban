# To-Do List Kanban | Engenharia de Software

Aplicação web de gerenciamento de tarefas no formato Kanban, desenvolvida como **Desafio 3** da *Imersão Engenharia de Software: Dev na Era da IA* (Alura + Google for Startups).

O projeto utiliza Python como núcleo das regras de negócio, executado no navegador por WebAssembly (Pyodide). A interface é construída com HTML, CSS e JavaScript ES Modules; os dados são persistidos localmente no navegador.

Este é um projeto educacional. O processo prioriza compreender requisitos, planejar, implementar, testar, validar e explicar as decisões. O uso de ferramentas de IA não substitui a revisão técnica nem a compreensão do código.

> **Estado em 03/11/2026:** Fase 7 implementada. CA7.1–CA7.9 e a regressão funcional RF01–RF16 foram aprovados nos cenários executados. A validação final permanece em andamento: o workflow Python ainda precisa ser executado na branch desta fase e a CA7.12 (segurança) está em avaliação.

O projeto é independente, não é produto oficial da Alura ou do Google e não representa endosso dessas organizações.

## Funcionalidades

- Quadro Kanban com as colunas A Fazer, Em Andamento e Concluídas.
- Criação, edição, movimentação, reordenação e exclusão de tarefas.
- Busca por título e descrição, calendário, resumo e Foco de Hoje.
- Relatórios calculados pelo domínio Python.
- Exportação e importação de backup JSON com validação estrita. A importação substitui integralmente os dados após validação e confirmação.
- Seleção individual e coletiva de tarefas, com confirmação e exclusão em operação única.
- Temas claro e escuro, layout responsivo e recursos de acessibilidade por teclado.
- Persistência local com restauração do estado anterior em caso de falha de gravação.

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python 3.14 | Modelo, validações, serviços, métricas e regras de negócio |
| Pyodide / WebAssembly | Execução de Python no navegador |
| HTML5 e CSS3 | Estrutura semântica, componentes, temas e responsividade |
| JavaScript ES Modules | Interface, integração com Pyodide e persistência no navegador |
| pytest e pytest-cov | Testes automatizados e cobertura do domínio Python |
| GitHub Actions | Validação de HTML/contraste e testes Python/cobertura |
| Nu HTML Checker | Verificação de conformidade do HTML |

A aplicação carrega a fonte Inter do Google Fonts e o Pyodide do CDN jsDelivr. Não foi identificada outra dependência externa nos arquivos de aplicação examinados nesta revisão.

## Estrutura do repositório

```text
alura-todolist-kanban/
├── .github/workflows/       # Workflows de HTML/contraste e testes Python
├── css/                     # Tokens, layout, Kanban e componentes
├── docs/                    # Requisitos, plano, estado e referências visuais
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

Documentos operacionais:
- [Requisitos](docs/REQUISITOS.md)
- [Plano de Implementação](docs/PLANO-IMPLEMENTACAO.md)
- [Estado Atual](docs/ESTADO-ATUAL.md)
- [Histórico de Alterações](CHANGELOG.md)

## Executar localmente

Requer Python 3.14 para executar a suíte de testes. Para servir a aplicação web, basta um navegador moderno e um servidor HTTP local.

Na raiz do repositório:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Abra `http://127.0.0.1:8000` no navegador. O servidor fica restrito ao computador local. Para encerrá-lo, pressione `Ctrl+C` no terminal.

A aplicação armazena as tarefas em `localStorage`. Em um navegador sem dados salvos, o quadro inicia vazio. O runtime Pyodide e os módulos Python são carregados pelo navegador.

## Executar os testes Python

Instale as dependências de desenvolvimento:

```bash
python -m pip install -e ".[dev]"
```

Execute a suíte e a verificação oficial de cobertura:

```bash
pytest && python scripts/verify_coverage.py
```

Metas: 100% de aprovação dos testes, cobertura de linhas ≥ 90% e cobertura de branches ≥ 85%.

### Evidências registradas

- **Fase 1:** 48 testes aprovados; 96,16% de cobertura de linhas e 92,78% de branches.
- **Fase 7:** 65 testes aprovados; 95,83% de cobertura de linhas e 92,54% de branches, conforme execução local registrada. A execução do workflow Python na branch atual ainda está pendente.
- **Workflow HTML/contraste:** execução `41742982859` aprovada na branch `fase-7-selecao-exclusao-coletiva`, commit `faa12e9`.
- **Workflow Python/cobertura:** execução `41742344451` aprovada na `main`, commit `6a967af`; por ser anterior à Fase 7, não comprova o estado atual da branch de trabalho.

Os números acima são registros históricos, não resultados de uma execução realizada durante esta revisão documental.

## Estado de validação

| Área | Estado registrado |
|---|---|
| Fases 1 a 6 | Implementadas; pendências de homologação específicas permanecem registradas em `docs/ESTADO-ATUAL.md` |
| Fase 7 | CA7.1–CA7.9 aprovados nos cenários testados; regressão RF01–RF16 aprovada nos cenários executados |
| RNF03 / CA7.11 | Parcial: workflow HTML aprovado na branch atual; workflow Python aprovado somente na `main` |
| CA7.12 — Segurança | Em andamento; inspeção estática e testes dinâmicos iniciais registrados no estado atual |
| Validação final | Em andamento; não declarar homologação integral |

### Validação de segurança em andamento

Os testes dinâmicos iniciais não identificaram execução de JavaScript nos cenários de XSS testados no título e na descrição. A importação de um backup com payload foi aceita e substituiu as tarefas existentes, conforme a semântica de restauração definida em RF14; a confirmação da renderização literal do conteúdo importado ainda precisa ser registrada. A inspeção estática identificou oportunidades de hardening, sem vulnerabilidades críticas ou altas confirmadas no escopo examinado. Consulte `docs/ESTADO-ATUAL.md` para evidências, limitações e pendências.

## Licença

Disponibilizado sob a licença [MIT](LICENSE).
