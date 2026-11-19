# Rastreabilidade e autoria

## De onde veio cada parte

| Etapa da disciplina | Evidência no repositório | Autoria |
| --- | --- | --- |
| Código-base e primeiras features (02/09 a 06/10) | commits `d9f05c7` a `e28c402` | professor Juliano — base do curso |
| Aula 9 — testes automatizados | PR #1 e commit `12eb767` | máquina do laboratório (`L16-M01`) |
| Aula 10 — Gerência de Configuração | PR #2, commit `1c5f210`, `src/repositorio_pessoas.py` | `9eb9aa4` pelo colega Luis Dutra; merge por Cler Andrade |
| Aula 11 — Docker e replicação MySQL | `infra/compose.yaml`, commit `4629f9f` | Cler Andrade |
| Aula 12 — persistência e colaboração | PR #1 no repo do So1d, PR #3, commit `e289160`, `src/repositorio_pessoas_mysql.py` | PR aberto por ClerAndrade; merge por Cler Andrade |
| Padronização e qualidade | commits `5794cc2`, `b50847c`, `2441169` | Cler Andrade |
| Testes ampliados | commit `73e525c` | Cler Andrade |
| Documentação e relatório | commits `docs: ...` | Cler Andrade |

## O problema de identidade `L16-M01`

Alguns commits feitos nas aulas 9 e 12 aparecem como
`L16-M01 <l16-m01@laboratorio.local>` porque a configuração local do Git na
máquina do laboratório estava assim:

- `19e498a` e `12eb767` — preparação e testes da Aula 9 neste repositório;
- `3881778`, `df8955b` e `6f646af` — correção, documentação e DAO MySQL no
  repositório do colega, dentro do PR #1 aberto pela conta `ClerAndrade`.

Isso é um erro de configuração, não uma autoria diferente. Não reescrevi esses
commits: eles já estão publicados, fazem parte de PRs mesclados e alterar os
hashes quebraria a evidência da colaboração. A correção foi aplicada no
repositório em 19/11:

```powershell
git config user.name "Cler Andrade"
git config user.email "115158502+ClerAndrade@users.noreply.github.com"
```

A partir do commit `e289160`, todos os commits novos saem com **Cler Andrade**
como autor. O e-mail é o `noreply` da conta GitHub, o mesmo usado nos merges
de 21/10 e 04/11.

## Sobre o requisito de 17 semanas

O histórico real não tem um commit próprio por semana letiva desde o início da
disciplina. Os primeiros registros com a minha participação são de 14/10; o
resto das semanas iniciais é código publicado pelo professor. Não foram
criados commits com data retroativa. A continuação está planejada em
`documentos/plano-semanal.md`, com atividades reais para as semanas restantes.

## Links dos Pull Requests

- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3
- https://github.com/So1d/gqs-cadatro-pessoas/pull/1
