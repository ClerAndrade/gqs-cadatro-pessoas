# Semana 4 — Métricas com RADON

Este registro foi reconstruído em 25/11/2026 a partir de evidências já existentes no repositório. As datas dos commits originais não foram alteradas; este arquivo apenas torna explícita a etapa correspondente do semestre.

## Atividade

Medição da complexidade antes da refatoração do menu.

## Evidências

`documentos/metricas-radon.md`: maior bloco B(8), média A(1,85).

## Como verificar

```powershell
python -m radon cc src -a -s
```

Este arquivo corresponde ao commit $(System.Collections.Hashtable.msg).
