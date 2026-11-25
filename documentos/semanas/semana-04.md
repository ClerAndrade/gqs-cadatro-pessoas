# Semana 4 — Métricas com RADON

Este arquivo é um índice complementar de rastreabilidade, elaborado em 25/11/2026 a partir de evidências já existentes. Não afirma que a atividade ocorreu nesta data, não substitui commits das semanas originais e não é apresentado como cumprimento do requisito quantitativo.

## Atividade

Medição da complexidade antes da refatoração do menu.

## Evidências

`documentos/metricas-radon.md`: maior bloco B(8), média A(1,85).

## Como verificar

```powershell
python -m radon cc src -a -s
```

Este arquivo corresponde ao commit $(System.Collections.Hashtable.msg).
