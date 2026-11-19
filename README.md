# Cadastro de Pessoas — GQS

Projeto evolutivo da disciplina **Gestão da Qualidade de Software**, UTFPR campus
Medianeira, 2026/2. Comecei com o código-base das aulas e fui acrescentando
testes, separação entre regras de negócio e armazenamento, análise estática,
métricas de complexidade, Docker, MySQL e colaboração por Pull Request.

Repositório: https://github.com/ClerAndrade/gqs-cadatro-pessoas

## O que o programa faz

É um menu de terminal com seis opções: cadastrar, consultar, alterar, listar,
analisar e sair. A camada de regras (`CadastroPessoas`) não sabe onde os dados
estão guardados: ela conversa com o contrato `RepositorioPessoas`. Na execução
normal uso a implementação em memória; quando quero testar persistência, troco
para a implementação MySQL sem mexer nas regras.

## Arquivos principais

| Arquivo | Para que serve |
| --- | --- |
| `src/pessoa.py` | entidade `Pessoa` |
| `src/cadastro.py` | regras de negócio do cadastro |
| `src/repositorio_pessoas.py` | contrato abstrato (ABC) |
| `src/repositorio_pessoas_memoria.py` | persistência em lista, usada por padrão |
| `src/repositorio_pessoas_mysql.py` | DAO MySQL (insert, select, update) |
| `src/main.py` | menu e escolha do repositório |
| `infra/compose.yaml` | MySQL principal + réplica |
| `infra/README.md` | como subir o banco e montar a replicação |
| `tests/` | testes PyTest, inclusive DAO com conector falso |
| `documentos/` | checklists, métricas, rastreabilidade e relatório |

## Preparando o ambiente (PowerShell)

```powershell
Set-Location C:\Users\Usuario\Desktop\GQS\Aula1410\gqs-cadastro-pessoas
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pre_commit install
```

O `pre-commit install` precisa ser repetido em cada clone novo: o hook fica em
`.git/hooks` e não vai para o repositório. O arquivo `.pre-commit-config.yaml`
sim, e já vem versionado.

## Executando

Modo padrão, sem banco:

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

A senha acima é a do laboratório, usada só no compose didático. Em qualquer
outro lugar, troque por uma senha local e nunca commite `.env` (já está no
`.gitignore`).

## Verificações

```powershell
python -m pytest -v
python -m pylint src
python -m radon cc src -a -s
python -m radon mi src
python -m pre_commit run --all-files
```

Estado atual: **23 testes passando**, **Pylint 10.00/10** e **RADON A**
(média 1,80; nenhum bloco acima de A). Os números e o antes/depois estão em
`documentos/checklist-pylint.md` e `documentos/metricas-radon.md`.

Na raiz também tem um `.venv` usado nos hooks do pre-commit. Os comandos acima
assumem que ele já foi criado; se você estiver em outro clone, siga o passo de
preparação.

## Colaboração

- PR #1 — testes automatizados, integrado em 21/10/2026:
  https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- PR #2 — separação do armazenamento, feito pelo So1d e integrado em 04/11:
  https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- PR #1 no repositório do So1d — persistência MySQL, aberto por ClerAndrade e
  integrado em 18/11: https://github.com/So1d/gqs-cadatro-pessoas/pull/1
- PR #3 — contribuição final do So1d trazendo o MySQL para este repositório,
  revisada e integrada em 19/11:
  https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3

Detalhes de autoria, incluindo o problema de identidade `L16-M01` na máquina do
laboratório, estão em `documentos/rastreabilidade.md`.

## Entrega

O relatório técnico em PDF está em `documentos/relatorio-tecnico.pdf`.
