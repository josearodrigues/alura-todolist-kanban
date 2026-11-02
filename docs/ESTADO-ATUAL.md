# Estado Atual do Projeto — To-Do List Kanban

## 1. Identificação do Desafio e Objetivo

- **Projeto:** Desafio 3 – Construção de uma aplicação To-Do List Kanban com Python e hospedagem no GitHub Pages.
- **Programa:** Imersão Engenharia de Software: Dev na Era da IA (Alura + Google for Startups).
- **Princípio Pedagógico:** Compreender, planejar, implementar, validar e explicar.
- **Linguagem Central:** Python (executado via WebAssembly no navegador).
- **Ambiente de Hospedagem:** GitHub Pages (aplicação 100% estática).

---

## 2. Estado Operacional do Repositório e Ambiente

- **Diretório de Trabalho:** `/home/joserodrigues/1h/Alura/20261026-Imersão Engenharia de Software- Dev na Era da IA/projetos/alura-kanban-python`
- **Controle de Versão (Git):**
  - *Branch atual:* Pendente de verificação via terminal.
  - *Último commit confirmado:* Pendente de verificação via terminal.
  - *Estado local vs. remoto:* Não verificado por comando shell devido a restrições operacionais do sandbox nesta sessão. Nenhuma operação de commit, push ou publicação foi realizada.
- **Mockup Oficial de Referência:**
  - `docs/design/referencias/todolist-kanban-1.0-mockup.png`: Presente, verificado e preservado intacto.

---

## 3. Estado da Governança Documental

A tríade documental mandatória encontra-se plenamente estabelecida:
- **`docs/REQUISITOS.md`:** Criado e atualizado (Versão 1.5 Corrigida).
- **`docs/PLANO-IMPLEMENTACAO.md`:** Criado e atualizado (Versão 1.5 Corrigida).
- **`docs/ESTADO-ATUAL.md`:** Criado e atualizado (este documento).

---

## 4. Situação de Cada Etapa e Fase do Projeto

| Etapa / Fase | Situação | Descrição / Entregáveis |
| :--- | :--- | :--- |
| **Etapa 1 — Descoberta e Requisitos** | **Concluída** | Levantamento via método Grill Me; decisões aprovadas e registradas. |
| **Etapa 2 — Planejamento Funcional** | **Concluída** | Especificação de RF01–RF15, RNF01–RNF07, contratos de dados, matriz de transições e documentação gerada. |
| **Etapa 3 — Arquitetura Técnica** | **Pendente** | Desenho arquitetural, comparativo Pyodide vs. PyScript, estratégia de persistência e estrutura de pastas. |
| **Etapa 4 — Plano de Implementação** | **Pendente** | Detalhamento técnico antes do início da codificação. |
| **Etapa 5 — Implementação Controlada** | **Não iniciada** | Zero código-fonte implementado. Aguardando autorização expressa. |
| ↳ *Fase 1: Domínio Python e Testes* | Não iniciada | Estrutura de domínio e suíte `pytest`. |
| ↳ *Fase 2: HTML e Acessibilidade* | Não iniciada | Marcação semântica e conformidade estrutural. |
| ↳ *Fase 3: CSS e Validação Visual* | Não iniciada | Design system, temas Claro/Escuro e ajuste do mockup ("Olá!"). |
| ↳ *Fase 4: WebAssembly e Persistência* | Não iniciada | Ponte JS $\leftrightarrow$ Python e `localStorage` com rollback. |
| ↳ *Fase 5: Interações (D&D e Calendário)* | Não iniciada | Drag and drop, touch, busca e popover. |
| ↳ *Fase 6: Relatórios e Backup JSON* | Não iniciada | Modal de relatórios, exportação e importação estrita. |
| **Etapa 6 — Validação Final** | **Não iniciada** | Homologação integrada e testes de aceitação. |

---

## 5. Matriz de Rastreabilidade

- **Planejado:** Aplicação To-Do Kanban estática com Python via WebAssembly, 3 colunas, drag and drop, calendário integrado, métricas em tempo real e backup JSON.
- **Aprovado:** Versão 1.5 Corrigida do Planejamento Funcional e tríade documental em `docs/`.
- **Implementado:** Zero código de aplicação implementado até o momento.
- **Testado:** Nenhum teste automatizado executado ainda (código de teste não iniciado).
- **Validado:** Auditoria estrutural documental e leitura direta do mockup oficial.
- **Commitado / Enviado ao GitHub / Publicado:** Nenhuma alteração foi commitada ou publicada.

---

## 6. Resumo das Decisões Aprovadas

1. **Estado Inicial Obrigatório:** Toda tarefa começa em `a_fazer`; sem seleção de estado no formulário.
2. **Identidade Visual e Exceção de Saudação:** Mockup oficial seguido fielmente, exceto pela saudação no banner, definida como `"Olá!"` (em vez de "Olá, João!"). O PNG original permanece preservado como registro histórico.
3. **Contrato Fechado:** Exatamente 10 atributos nas tarefas; rejeição integral de campos desconhecidos no envelope e nas tarefas.
4. **Semântica de Metadados:** Reordenações intra-coluna atualizam a `data_atualizacao` apenas da tarefa diretamente movida; tarefas apenas reindexadas mantêm suas datas originais. Timestamp global atualiza em mutações efetivas.
5. **Garantia contra Falhas de Persistência:** Falha na gravação impede que a alteração seja considerada realizada, revertendo o estado em memória e na interface com feedback claro de erro.
6. **Métricas de Resumo:** Concluídas calculadas com uma casa decimal e pendentes por diferença em relação a 100,0% ($0,0\%$ para total zero).
7. **Backup JSON:** Portabilidade e backup externo, com durabilidade dependente da conservação do arquivo pelo usuário.

---

## 7. Pendências Técnicas Abertas (Reservadas para a Etapa 3)

1. Comparativo e escolha formal entre **Pyodide direto** e **PyScript**.
2. Avaliação de UUID v4 para o identificador `id`.
3. Definição da arquitetura de persistência: documento JSON único vs. duas fases (shadow key) e mecanismos técnicos de rollback.
4. Validação formal da sequência de `ordem`: valores únicos, contíguos e iniciando em zero por coluna.
5. Verificações formais de coerência temporal cronológica entre as datas.
6. Estrutura do domínio Python: orientação a objetos (classes), funções puras ou abordagem híbrida.
7. Consolidação das metas quantitativas de cobertura de código no `pytest-cov`.
8. Escolha das ferramentas de teste, linters e validação de acessibilidade do frontend.
9. Arquitetura modular de diretórios e componentes.

---

## 8. Próxima Ação Recomendada

- **Apresentação da documentação criada para revisão final do usuário.**
- **Aguardar a declaração de encerramento formal da Etapa 2.**
- **Obter autorização explícita para início da Etapa 3 — Arquitetura e Planejamento Técnico.**
