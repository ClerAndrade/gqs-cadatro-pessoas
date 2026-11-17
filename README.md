# Cadastro de Pessoas
Projeto evolutivo da disciplina de Gestão da Qualidade de Software (GQS). O sistema cadastra pessoas e mantém a persistência separada das regras de negócio por meio do contrato `RepositorioPessoas`.

## Objetivo
Aplicar, em um mesmo projeto, práticas de qualidade de software: modularização, testes automatizados, análise estática, gerência de configuração, persistência em MySQL e replicação.

## Organização dos arquivos
| Arquivo | Responsabilidade |
|---|---|
| `src/pessoa.py` | entidade Pessoa |
| `src/repositorio_pessoas.py` | contrato abstrato (ABC) |
| `src/repositorio_pessoas_memoria.py` | implementação em lista |
| `src/repositorio_pessoas_mysql.py` | persistência no MySQL |
| `src/cadastro.py` | regras de negócio |
| `src/main.py` | menu e escolha do repositório |
| `infra/compose.yaml` | MySQL principal + réplica |
| `tests/test_cadastro.py` | testes PyTest |

## Requisitos
- Python 3
- Docker Desktop
- dependências listadas em `requirements.txt`
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    pre-commit install
Em novos terminais, repetir somente a ativação da `.venv`.

## Docker, contêineres e replicação
Na pasta `infra/`, onde está o `compose.yaml`:
    cd infra
    docker compose up -d
    docker compose ps
- `principal`: porta `3307` no Windows → `3306` no contêiner.
- `replica`: porta `3308` no Windows → `3306` no contêiner.
`docker compose up -d` apenas inicia os serviços. O vínculo de replicação
(usuário `repl`, `CHANGE REPLICATION SOURCE`, `START REPLICA`) segue o
roteiro da Aula 11. Verifique com `SHOW REPLICA STATUS\G` na réplica.

## Tabela e variáveis de ambiente
Banco: `cadastro`. Tabela: `pessoa (id, nome, idade, email)`.
    $env:DB_HOST = "localhost"
    $env:DB_PORT = "3307"
    $env:DB_USER = "root"
    $env:DB_PASSWORD = Read-Host "Informe a senha do MySQL"
    $env:DB_NAME = "cadastro"
As variáveis valem só na sessão atual do terminal. Não registre senhas
nem arquivos `.env` no repositório.

## Executar e escolher a persistência
Na raiz do projeto, com a `.venv` ativa:

    python src/main.py

Em `src/main.py`, a constante `USAR_MYSQL` define o repositório:
- `True` → `RepositorioPessoasMySQL` (dados persistentes no principal);
- `False` → `RepositorioPessoasMemoria` (dados só durante a execução).

## Verificação
    python -m pytest -v
    pylint src
A escrita acontece sempre no principal. A réplica recebe as alterações
por replicação assíncrona e pode apresentar atraso.