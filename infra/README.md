# Infraestrutura MySQL

Compose usado na Aula 11: um principal e uma réplica MySQL 8.4.13, com GTID.
A aplicação escreve sempre no principal; a réplica recebe as alterações por
replicação assíncrona.

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

A senha `root_lab_2026` no compose é uma simplificação didática do
laboratório. Não é uma prática recomendada para produção e não deve ser
reutilizada em outro ambiente.

## Vínculo de replicação

`docker compose up -d` cria os contêineres, mas não configura o canal de
replicação em um volume novo. Na primeira execução, no console do principal:

```sql
CREATE USER IF NOT EXISTS 'repl'@'%' IDENTIFIED BY 'repl_lab_2026';
ALTER USER 'repl'@'%' IDENTIFIED BY 'repl_lab_2026';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
```

No console da réplica:

```sql
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='principal',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='repl_lab_2026',
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
