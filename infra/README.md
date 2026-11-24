# Infraestrutura MySQL

Compose usado na Aula 11: um principal e uma réplica MySQL 8.4.13, com GTID.
A aplicação escreve sempre no principal; a réplica recebe as alterações por
replicação assíncrona.

## Configuração local da senha

O compose não contém senha literal. Antes de qualquer comando, copie o modelo
e defina a senha apenas no seu arquivo local:

```powershell
Copy-Item .env.example .env
# edite .env e substitua valor_local_do_laboratorio pela senha do laboratório
$env:MYSQL_ROOT_PASSWORD = (Get-Content .env | Where-Object { $_ -like 'MYSQL_ROOT_PASSWORD=*' }).Split('=', 2)[1]
docker compose config --quiet
```

O arquivo `.env` está listado no `.gitignore` do repositório: nunca versionar,
nunca enviar ao GitHub e nunca reutilizar a senha em outro ambiente. Se o
Docker Compose carregar `.env` automaticamente, a variável já estará disponível;
caso contrário, exporte-a no PowerShell como no exemplo acima.

## Subir os serviços

No PowerShell, a partir da raiz do projeto:

```powershell
Set-Location infra
docker compose config
docker compose pull
docker compose up -d
docker compose ps
```

As portas publicadas são `127.0.0.1:3307` (principal) e `127.0.0.1:3308`
(réplica). Os dados ficam nos volumes `principal-data` e `replica-data`.

## Vínculo de replicação

`docker compose up -d` cria os contêineres, mas não configura o canal de
replicação em um volume novo. Na primeira execução, no console do principal:

```sql
CREATE USER IF NOT EXISTS 'repl'@'%' IDENTIFIED BY 'senha_local_de_replicacao';
ALTER USER 'repl'@'%' IDENTIFIED BY 'senha_local_de_replicacao';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
```

No console da réplica:

```sql
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='principal',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='senha_local_de_replicacao',
  SOURCE_AUTO_POSITION=1,
  GET_SOURCE_PUBLIC_KEY=1;
START REPLICA;
SET PERSIST read_only = ON;
SET PERSIST super_read_only = ON;
SHOW REPLICA STATUS\G
```

O comando `CHANGE REPLICATION SOURCE` é só da primeira configuração. Em
volumes já existentes, use `SHOW REPLICA STATUS\G` e, se o canal estiver
parado, `START REPLICA;`.

## Tabela usada pelo DAO

```sql
CREATE DATABASE cadastro CHARACTER SET utf8mb4;
USE cadastro;
CREATE TABLE pessoa (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  idade INT NOT NULL,
  email VARCHAR(200) NOT NULL UNIQUE
);
```

## Parar sem perder dados

```powershell
docker compose stop
docker compose start
```

Não execute `docker compose down --volumes`: isso apaga os dois volumes.
Replicação não substitui backup.
