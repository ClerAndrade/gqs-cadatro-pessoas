# Contribuindo com o projeto

Regras para mexer neste repositÃ³rio sem quebrar o que jÃ¡ funciona. SÃ£o poucas
coisas, mas todas verificÃ¡veis antes do commit.

## Antes de comeÃ§ar

```powershell
git switch main
git pull
git status
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pre_commit install
```

Crie uma branch com nome curto e identificÃ¡vel. Exemplos que jÃ¡ existem no
histÃ³rico: `aula9/testes-automatizados`, `feature/consolidacao-final`.

## PadrÃµes de cÃ³digo

| Item | ConvenÃ§Ã£o adotada |
| --- | --- |
| Python | 3.15 no laboratÃ³rio (Pylint configurado para 3.15) |
| Classes | `PascalCase` |
| FunÃ§Ãµes, mÃ©todos, variÃ¡veis e mÃ³dulos | `snake_case` (`get_nome`, `buscar_por_nome`) |
| Constantes | `MAIUSCULAS_COM_UNDERLINE` |
| Docstring | em mÃ³dulo, classe, funÃ§Ã£o e mÃ©todo |
| IndentaÃ§Ã£o | 4 espaÃ§os |
| Linha | atÃ© 100 colunas |
| EspaÃ§o no fim da linha | nÃ£o |
| Lista vazia | `if not lista:` |
| Atributo interno | prefixo `__` |
| PersistÃªncia | sempre atrÃ¡s de `RepositorioPessoas` |

NÃ£o desabilito regra do Pylint para "limpar" relatÃ³rio. Se um apontamento fizer
sentido, corrijo o cÃ³digo; se nÃ£o fizer, registro o motivo no commit. O
`.pylintrc` atual sÃ³ desabilita mensagens internas do prÃ³prio Pylint.

## Antes de cada commit

Os hooks locais rodam sozinhos no `git commit` e verificam:

1. `pylint src` â€” anÃ¡lise estÃ¡tica;
2. `pytest -q` â€” testes;
3. `radon cc src -a -s` â€” complexidade, sÃ³ para mostrar o resultado.

Se quiser rodar na mÃ£o:

```powershell
python -m pylint src
python -m pytest -v
python -m radon cc src -a -s
python -m pre_commit run --all-files
```

Para cÃ³digo novo, mantenha os blocos com nota A no RADON. Se aparecer B ou C,
quebre a funÃ§Ã£o em partes menores â€” foi exatamente o que fiz com `executar()`,
que passou de B(8) para A(2).

## Mensagens de commit

Use `feat`, `refactor`, `chore`, `fix`, `docs` ou `test`, seguidos de uma frase
curta no imperativo e sem ponto final. Exemplos reais do histÃ³rico:

```text
refactor: reduz complexidade do menu principal
test: amplia cobertura com pytest e dao mysql
chore: configura Docker Compose e dependencias de qualidade
docs: registra metricas radon e checklist pylint
```

Nada de `update`, `final`, `arrumado` ou data alterada de propÃ³sito. Se o
commit corrigir um defeito, escreva `fix:` e diga qual foi o defeito.

## ColaboraÃ§Ã£o com outro estudante

O fluxo usado na disciplina foi fork â†’ branch â†’ commit â†’ push â†’ Pull Request â†’
revisÃ£o â†’ merge:

1. quem contribui clona/forka o repositÃ³rio do colega e cria uma branch;
2. roda testes e Pylint antes de abrir o PR;
3. descreve no PR o que mudou e quais comandos usou para verificar;
4. o dono do repositÃ³rio revisa e sÃ³ integra quando estiver coerente.

Foi assim que entraram o repositÃ³rio em memÃ³ria (PR #2) e a persistÃªncia MySQL
(PR #1 no repo do So1d e PR #3 neste repo). PR aberto sem revisÃ£o nÃ£o conta como
integrado.

## Banco de dados

Nunca commite senha real nem `.env`. O DAO lÃª `DB_HOST`, `DB_PORT`, `DB_USER`,
`DB_PASSWORD` e `DB_NAME` do ambiente. Os testes usam um conector falso e nÃ£o
precisam de MySQL rodando. Se vocÃª subir o compose, use `docker compose stop`
para parar; `down --volumes` apaga os dados.
