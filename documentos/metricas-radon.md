# Métricas de complexidade — RADON

Comandos usados, sempre da raiz do repositório:

```powershell
python -m radon cc src -a -s
python -m radon raw src
python -m radon mi src
```

`cc` mede complexidade ciclomática, `raw` conta linhas e comentários, e `mi`
calcula o índice de manutenibilidade.

## Antes (commit `e289160`)

```text
src\main.py
    F 158:0 executar - B (8)
    F 108:0 analisar_faixa_etaria - A (4)
    ...
48 blocks (classes, functions, methods) analyzed.
Average complexity: A (1.8541666666666667)
```

O bloco mais problemático era `executar()`: o `while` com o `if/elif` de todas
as opções do menu dava complexidade B(8). Não estava errado, mas era o ponto
mais difícil de testar e de alterar.

## Depois (commit `2441169`)

Separei o despacho das opções em `processar_opcao()`, com um dicionário de
ações, e `executar()` ficou só com o laço do menu:

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
| Média de complexidade | A (1,85) | A (1,80) |
| Pior bloco | `executar` — B (8) | três funções — A (4) |
| Blocos com nota B ou C | 1 | 0 |

O `radon mi src` deu **A para os seis módulos** de `src`. Não persegui nota
perfeita: o objetivo foi eliminar o único bloco B e deixar o menu fácil de
ler. O hook do pre-commit roda o `radon cc` em cada commit para a métrica
continuar visível.
