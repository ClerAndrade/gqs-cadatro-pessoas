# Checklist de análise estática - Atividade 6

**Projeto:** Cadastro de Pessoas
**Branch:** `aula6/analise-estatica`
**Ferramenta:** PyLint 4.1.3
**Aluno(a):** Cler Elis Andrade

Este checklist registra a análise estática do código antes e depois das
correções, seguindo o ciclo trabalhado em aula:
*executar -> analisar -> corrigir -> executar novamente*.

## 1. Execução inicial (antes das correções)

| Item verificado | Situação | Apontamento do PyLint |
| --- | --- | --- |
| Docstrings em todas as funções e métodos | Pendente | C0116 (`missing-function-docstring`) |
| Nomes em snake_case (métodos e atributos) | Pendente | C0103 (`invalid-name`) |
| Sem espaços em branco no fim das linhas | Pendente | C0303 (`trailing-whitespace`) |
| Importações organizadas | OK | Nenhum apontamento |
| Código morto / linhas longas | OK | Nenhum apontamento |
| Nota do PyLint na execução inicial | Registrada | 8.74/10 |

## 2. Decisões de correção

| Apontamento | Decisão adotada |
| --- | --- |
| C0116 - docstrings ausentes | Criar docstring descritiva em cada método |
| C0103 - `getNome`, `getIdade`, ... | Renomear os métodos para snake_case (`get_nome`, ...) |
| C0303 - espaço no fim da linha | Remover o espaço em branco |

## 3. Reexecução (após as correções)

| Item verificado | Situação |
| --- | --- |
| Docstrings em todas as funções e métodos | OK |
| Nomes em snake_case (métodos e atributos) | OK |
| Sem espaços em branco no fim das linhas | OK |
| Nota final do PyLint | 10.00/10 |

## 4. Comparação das execuções

| Execução | Apontamentos | Nota |
| --- | --- | --- |
| Antes das correções | 18 (10 docstrings, 7 nomes, 1 espaço) | 8.74/10 |
| Depois das correções | 0 | 10.00/10 |

## 5. Observação

As alterações foram feitas no código, e não apenas na configuração da
ferramenta: nenhuma regra foi desabilitada no PyLint para obter a nota.
