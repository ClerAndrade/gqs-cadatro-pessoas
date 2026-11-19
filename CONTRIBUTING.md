# Contribuindo com o projeto

Regras para mexer neste repositório sem quebrar o que já funciona. São poucas
coisas, mas todas verificáveis antes do commit.

## Antes de começar

```powershell
git switch main
git pull
git status
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pre_commit install
```

Crie uma branch com nome curto e identificável. Exemplos que já existem no
histórico: `aula9/testes-automatizados`, `feature/consolidacao-final`.

## Padrões de código

| Item | Convenção adotada |
| --- | --- |
| Python | 3.15 no laboratório (Pylint configurado para 3.15) |
| Classes | `PascalCase` |
| Funções, métodos, variáveis e módulos | `snake_case` (`get_nome`, `buscar_por_nome`) |
| Constantes | `MAIUSCULAS_COM_UNDERLINE` |
| Docstring | em módulo, classe, função e método |
| Indentação | 4 espaços |
| Linha | até 100 colunas |
| Espaço no fim da linha | não |
| Lista vazia | `if not lista:` |
| Atributo interno | prefixo `__` |
| Persistência | sempre atrás de `RepositorioPessoas` |

Não desabilito regra do Pylint para "limpar" relatório. Se um apontamento fizer
sentido, corrijo o código; se não fizer, registro o motivo no commit. O
`.pylintrc` atual só desabilita mensagens internas do próprio Pylint.

## Antes de cada commit

Os hooks locais rodam sozinhos no `git commit` e verificam:

1. `pylint src` — análise estática;
2. `pytest -q` — testes;
3. `radon cc src -a -s` — complexidade, só para mostrar o resultado.

Se quiser rodar na mão:

```powershell
python -m pylint src
python -m pytest -v
python -m radon cc src -a -s
python -m pre_commit run --all-files
```

Para código novo, mantenha os blocos com nota A no RADON. Se aparecer B ou C,
quebre a função em partes menores — foi exatamente o que fiz com `executar()`,
que passou de B(8) para A(2).

## Mensagens de commit

Use `feat`, `refactor`, `chore`, `fix`, `docs` ou `test`, seguidos de uma frase
curta no imperativo e sem ponto final. Exemplos reais do histórico:

```text
refactor: reduz complexidade do menu principal
test: amplia cobertura com pytest e dao mysql
chore: configura Docker Compose e dependencias de qualidade
docs: registra metricas radon e checklist pylint
```

Nada de `update`, `final`, `arrumado` ou data alterada de propósito. Se o
commit corrigir um defeito, escreva `fix:` e diga qual foi o defeito.

## Colaboração com outro estudante

O fluxo usado na disciplina foi fork → branch → commit → push → Pull Request →
revisão → merge:

1. quem contribui clona/forka o repositório do colega e cria uma branch;
2. roda testes e Pylint antes de abrir o PR;
3. descreve no PR o que mudou e quais comandos usou para verificar;
4. o dono do repositório revisa e só integra quando estiver coerente.

Foi assim que entraram o repositório em memória (PR #2) e a persistência MySQL
(PR #1 no repo do So1d e PR #3 neste repo). PR aberto sem revisão não conta como
integrado.

## Banco de dados

Nunca commite senha real nem `.env`. O DAO lê `DB_HOST`, `DB_PORT`, `DB_USER`,
`DB_PASSWORD` e `DB_NAME` do ambiente. Os testes usam um conector falso e não
precisam de MySQL rodando. Se você subir o compose, use `docker compose stop`
para parar; `down --volumes` apaga os dados.
