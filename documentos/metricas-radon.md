# MÃ©tricas de complexidade â€” RADON

Comandos usados, sempre da raiz do repositÃ³rio:

```powershell
python -m radon cc src -a -s
python -m radon raw src
python -m radon mi src
```

`cc` mede complexidade ciclomÃ¡tica, `raw` conta linhas e comentÃ¡rios, e `mi`
calcula o Ã­ndice de manutenibilidade.

## Antes (commit `e289160`)

```text
src\main.py
    F 158:0 executar - B (8)
    F 108:0 analisar_faixa_etaria - A (4)
    ...
48 blocks (classes, functions, methods) analyzed.
Average complexity: A (1.8541666666666667)
```

O bloco mais problemÃ¡tico era `executar()`: o `while` com o `if/elif` de todas
as opÃ§Ãµes do menu dava complexidade B(8). NÃ£o estava errado, mas era o ponto
mais difÃ­cil de testar e de alterar.

## Depois (commit `2441169`)

Separei o despacho das opÃ§Ãµes em `processar_opcao()`, com um dicionÃ¡rio de
aÃ§Ãµes, e `executar()` ficou sÃ³ com o laÃ§o do menu:

```text
src\main.py
    F 112:0 analisar_faixa_etaria - A (4)
    F 124:0 analisar_contato - A (4)
    F 134:0 analisar_email - A (4)
    F 159:0 processar_opcao - A (3)
    F 182:0 executar - A (2)
    ...
49 blocks (classes, functions, methods) analyzed.
Average complexity: A (1.7959183673469388)
```

| Indicador | Antes | Depois |
| --- | --- | --- |
| Blocos analisados | 48 | 49 |
| MÃ©dia de complexidade | A (1,85) | A (1,80) |
| Pior bloco | `executar` â€” B (8) | trÃªs funÃ§Ãµes â€” A (4) |
| Blocos com nota B ou C | 1 | 0 |

O `radon mi src` deu **A para os seis mÃ³dulos** de `src`. NÃ£o persegui nota
perfeita: o objetivo foi eliminar o Ãºnico bloco B e deixar o menu fÃ¡cil de
ler. O hook do pre-commit roda o `radon cc` em cada commit para a mÃ©trica
continuar visÃ­vel.
