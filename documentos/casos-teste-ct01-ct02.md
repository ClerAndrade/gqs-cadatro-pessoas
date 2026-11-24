# Casos de teste CT-01 e CT-02

Modelo solicitado na Aula 8. Os casos abaixo descrevem o comportamento observável do cadastro e a delegação da persistência.

## CT-01 — Cadastro com persistência em memória

| Campo | Descrição |
|---|---|
| Entrada | nome `amaldo`, idade `23`, e-mail `amaldo@example.com`; opção `1` do menu |
| Ação | chamar `CadastroPessoas.cadastrar()` com uma `Pessoa` válida |
| Resultado esperado | `cadastrar` é delegates ao repositório; `listar()` devolve a pessoa cadastrada |
| Resultado observado | testes `test_cadastrar_delega_ao_repositorio` e `test_listar_delega_ao_repositorio` passam |
| Evidência | `tests/test_cadastro.py`; Figura 2 do relatório final para a execução com MySQL |

## CT-02 — Alteração delegada ao repositório

| Campo | Descrição |
|---|---|
| Entrada | nome `amaldo`, nova idade `22`, mantidos nome e e-mail |
| Ação | chamar `alterar()` com os dados novos |
| Resultado esperado | uma nova `Pessoa` é montada e `repositorio.alterar(nome, nova_pessoa)` é chamado; o repositório devolve `True` |
| Resultado observado | `test_alterar_delega_ao_repositorio` passa; execução real mostrou a idade mudando de 23 para 22 (Figura 3) |
| Evidência | `tests/test_cadastro.py`, commit `3881778`, Figura 3 do relatório final |

## Observação

O termo `delegates` no CT-01 foi mantido como aparece nos testes; a redação em português correspondente é "delega". A suíte completa tem 27 testes e é executada com `python -m pytest -q`.
