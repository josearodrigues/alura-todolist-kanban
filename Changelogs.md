# Changelog

Este arquivo registra alterações relevantes do projeto em ordem cronológica inversa. Os registros descrevem o que foi implementado e validado, sem antecipar funcionalidades planejadas.

## [Não lançado] — 2026-11-02

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
- Fases 3 a 6, conforme o plano de implementação.

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
