# Cadastro de Pessoas â€” GQS

Projeto evolutivo da disciplina **GestÃ£o da Qualidade de Software**, UTFPR campus
Medianeira, 2026/2. Comecei com o cÃ³digo-base das aulas e fui acrescentando
testes, separaÃ§Ã£o entre regras de negÃ³cio e armazenamento, anÃ¡lise estÃ¡tica,
mÃ©tricas de complexidade, Docker, MySQL e colaboraÃ§Ã£o por Pull Request.

RepositÃ³rio: https://github.com/ClerAndrade/gqs-cadatro-pessoas

## O que o programa faz

Ã‰ um menu de terminal com seis opÃ§Ãµes: cadastrar, consultar, alterar, listar,
analisar e sair. A camada de regras (`CadastroPessoas`) nÃ£o sabe onde os dados
estÃ£o guardados: ela conversa com o contrato `RepositorioPessoas`. Na execuÃ§Ã£o
normal uso a implementaÃ§Ã£o em memÃ³ria; quando quero testar persistÃªncia, troco
para a implementaÃ§Ã£o MySQL sem mexer nas regras.

## Arquivos principais

| Arquivo | Para que serve |
| --- | --- |
| `src/pessoa.py` | entidade `Pessoa` |
| `src/cadastro.py` | regras de negÃ³cio do cadastro |
| `src/repositorio_pessoas.py` | contrato abstrato (ABC) |
| `src/repositorio_pessoas_memoria.py` | persistÃªncia em lista, usada por padrÃ£o |
| `src/repositorio_pessoas_mysql.py` | DAO MySQL (insert, select, update) |
| `src/main.py` | menu e escolha do repositÃ³rio |
| `infra/compose.yaml` | MySQL principal + rÃ©plica |
| `infra/README.md` | como subir o banco e montar a replicaÃ§Ã£o |
| `tests/` | testes PyTest, inclusive DAO com conector falso |
| `documentos/` | checklists, mÃ©tricas, rastreabilidade e relatÃ³rio |

## Preparando o ambiente (PowerShell)

```powershell
Set-Location C:\Users\Usuario\Desktop\GQS\Aula1410\gqs-cadastro-pessoas
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pre_commit install
```

O `pre-commit install` precisa ser repetido em cada clone novo: o hook fica em
`.git/hooks` e nÃ£o vai para o repositÃ³rio. O arquivo `.pre-commit-config.yaml`
sim, e jÃ¡ vem versionado.

## Executando

Modo padrÃ£o, sem banco:

```powershell
python src\main.py
```

Modo MySQL ( depois de subir o compose e criar a tabela conforme
`infra/README.md`):

```powershell
$env:CADASTRO_REPOSITORIO = "mysql"
$env:DB_HOST = "localhost"
$env:DB_PORT = "3307"
$env:DB_USER = "root"
$env:DB_PASSWORD = "root_lab_2026"
$env:DB_NAME = "cadastro"
python src\main.py
```

A senha acima Ã© a do laboratÃ³rio, usada sÃ³ no compose didÃ¡tico. Em qualquer
outro lugar, troque por uma senha local e nunca commite `.env` (jÃ¡ estÃ¡ no
`.gitignore`).

## VerificaÃ§Ãµes

```powershell
python -m pytest -v
python -m pylint src
python -m radon cc src -a -s
python -m radon mi src
python -m pre_commit run --all-files
```

Estado atual: **23 testes passando**, **Pylint 10.00/10** e **RADON A**
(mÃ©dia 1,80; nenhum bloco acima de A). Os nÃºmeros e o antes/depois estÃ£o em
`documentos/checklist-pylint.md` e `documentos/metricas-radon.md`.

Na raiz tambÃ©m tem um `.venv` usado nos hooks do pre-commit. Os comandos acima
assumem que ele jÃ¡ foi criado; se vocÃª estiver em outro clone, siga o passo de
preparaÃ§Ã£o.

## ColaboraÃ§Ã£o

- PR #1 â€” testes automatizados, integrado em 21/10/2026:
  https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- PR #2 â€” separaÃ§Ã£o do armazenamento, feito pelo So1d e integrado em 04/11:
  https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- PR #1 no repositÃ³rio do So1d â€” persistÃªncia MySQL, aberto por ClerAndrade e
  integrado em 18/11: https://github.com/So1d/gqs-cadatro-pessoas/pull/1
- PR #3 â€” contribuiÃ§Ã£o final do So1d trazendo o MySQL para este repositÃ³rio,
  revisada e integrada em 19/11:
  https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3

Detalhes de autoria, incluindo o problema de identidade `L16-M01` na mÃ¡quina do
laboratÃ³rio, estÃ£o em `documentos/rastreabilidade.md`.

## Entrega

O relatÃ³rio tÃ©cnico em PDF estÃ¡ em `documentos/relatorio-tecnico.pdf`.
