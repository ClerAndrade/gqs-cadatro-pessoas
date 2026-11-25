# Semana 11 — MySQL e Docker Compose

Este arquivo é um índice complementar de rastreabilidade, elaborado em 25/11/2026 a partir de evidências já existentes. Não afirma que a atividade ocorreu nesta data, não substitui commits das semanas originais e não é apresentado como cumprimento do requisito quantitativo.

## Atividade

Principal e réplica MySQL 8.4.13, volumes e healthchecks.

## Evidências

`infra/compose.yaml`; `infra/README.md`; `infra/.env.example`; commit `4629f9f`.

## Como verificar

```powershell
Set-Location infra; docker compose config --quiet
```

Este arquivo corresponde ao commit $(System.Collections.Hashtable.msg).
