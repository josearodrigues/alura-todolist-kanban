# To-Do List Kanban

Projeto do Desafio 3 da Imersão Engenharia de Software: Dev na Era da IA (Alura + Google for Startups).

Aplicação Kanban com núcleo de domínio em Python, planejada para execução no navegador por WebAssembly. O desenvolvimento é realizado em fases; funcionalidades ainda não integradas permanecem desabilitadas.

## Estado atual

- Fase 1: domínio Python e testes automatizados concluídos e validados.
- Fase 2: estrutura HTML semântica implementada; validação Nu HTML Checker aprovada.
- Fases 3 a 6: ainda não iniciadas.

## Executar localmente

Requisitos: Python 3 e um navegador moderno. Não são necessárias dependências Python adicionais para servir os arquivos estáticos.

Na raiz do repositório, execute:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Abra no navegador:

```text
http://127.0.0.1:8000
```

O servidor fica restrito à interface de loopback do próprio computador. Para encerrá-lo, volte ao terminal e pressione `Ctrl+C`.

## Verificação manual da Fase 2

A Fase 2 prioriza semântica HTML e acessibilidade estrutural. Como a apresentação CSS ainda pertence à Fase 3, a página pode aparecer sem o layout visual definitivo. Faça as verificações funcionais abaixo:

1. Use `Tab` e `Shift+Tab` para percorrer os controles interativos.
2. Use `Enter` ou `Espaço` para ativar botões e controles apropriados.
3. Pressione `Ctrl+K` e confirme que o foco vai para o campo de busca.
4. Abra cada diálogo disponível e verifique o foco inicial, a permanência do foco dentro do diálogo e o retorno ao controle que o abriu após o fechamento.
5. Pressione `Esc` para fechar o diálogo ou menu contextual ativo.
6. No menu contextual, verifique a abertura e o fechamento pelo teclado.
7. Confira se os campos dos formulários possuem rótulos associados.
8. Verifique se os botões e campos têm nomes acessíveis compreensíveis.

Registre cada item como **Aprovado**, **Reprovado** ou **Não aplicável**, anotando o comportamento observado. A inspeção visual completa do layout, do foco e dos estados visuais será realizada após a implementação CSS da Fase 3.

> Nesta fase, operações de negócio como salvar, editar, excluir e mover tarefas ainda não estão integradas. Seus controles permanecem desabilitados; isso é esperado.

## Validação automática de HTML

O workflow [Validar HTML](.github/workflows/validar-html.yml) executa o Nu HTML Checker quando há alterações relevantes em `index.html`, em pull requests direcionados à `main`, ou por acionamento manual na aba **Actions** do GitHub.

A validação aprovada mais recente registrou zero erros e zero avisos. A pipeline não substitui a verificação manual de acessibilidade descrita acima.

## Documentação

- [Requisitos](docs/REQUISITOS.md)
- [Plano de Implementação](docs/PLANO-IMPLEMENTACAO.md)
- [Estado Atual](docs/ESTADO-ATUAL.md)
