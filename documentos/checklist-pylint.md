# Checklist de anÃ¡lise estÃ¡tica â€” Pylint

Projeto: Cadastro de Pessoas. Ferramenta: Pylint 4.1.3, Python 3.15.

## ExecuÃ§Ã£o antes das correÃ§Ãµes

Comando:

```powershell
python -m pylint src
```

SaÃ­da no commit `e289160` (antes da padronizaÃ§Ã£o):

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

| Apontamento | CorreÃ§Ã£o |
| --- | --- |
| C0114 nos mÃ³dulos de repositÃ³rio | docstring de mÃ³dulo adicionada |
| C0115 nas classes abstratas e de memÃ³ria | docstring de classe adicionada |
| Nomes `getNome` / `buscarPorNome` | renomeados para `get_nome` / `buscar_por_nome` |
| Regras desabilitadas no `.pylintrc` | configuraÃ§Ã£o reescrita; sÃ³ mensagens internas continuam desabilitadas |

Alguns apontamentos nÃ£o apareciam na nota porque a configuraÃ§Ã£o antiga
desabilitava `invalid-name`, `trailing-whitespace`,
`missing-function-docstring` e `missing-class-docstring`. Isso escondia
problema real: havia mÃ©todo em `camelCase` e arquivo sem docstring. Preferi
tirar essas exceÃ§Ãµes e corrigir o cÃ³digo.

## ExecuÃ§Ã£o depois

```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.83/10, +0.17)
```

O `fail-under` estÃ¡ em 10, entÃ£o qualquer regressÃ£o faz o hook falhar e o
commit nÃ£o entra.
