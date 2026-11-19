# Checklist de análise estática — Pylint

Projeto: Cadastro de Pessoas. Ferramenta: Pylint 4.1.3, Python 3.15.

## Execução antes das correções

Comando:

```powershell
python -m pylint src
```

Saída no commit `e289160` (antes da padronização):

```text
************* Module repositorio_pessoas
src\repositorio_pessoas.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src\repositorio_pessoas.py:6:0: C0115: Missing class docstring (missing-class-docstring)
************* Module repositorio_pessoas_memoria
src\repositorio_pessoas_memoria.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src\repositorio_pessoas_memoria.py:6:0: C0115: Missing class docstring (missing-class-docstring)

Your code has been rated at 9.83/10
```

## O que foi corrigido

| Apontamento | Correção |
| --- | --- |
| C0114 nos módulos de repositório | docstring de módulo adicionada |
| C0115 nas classes abstratas e de memória | docstring de classe adicionada |
| Nomes `getNome` / `buscarPorNome` | renomeados para `get_nome` / `buscar_por_nome` |
| Regras desabilitadas no `.pylintrc` | configuração reescrita; só mensagens internas continuam desabilitadas |

Alguns apontamentos não apareciam na nota porque a configuração antiga
desabilitava `invalid-name`, `trailing-whitespace`,
`missing-function-docstring` e `missing-class-docstring`. Isso escondia
problema real: havia método em `camelCase` e arquivo sem docstring. Preferi
tirar essas exceções e corrigir o código.

## Execução depois

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.83/10, +0.17)
```

O `fail-under` está em 10, então qualquer regressão faz o hook falhar e o
commit não entra.
