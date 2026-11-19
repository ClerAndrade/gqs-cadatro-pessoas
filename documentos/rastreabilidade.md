# Rastreabilidade e autoria

## De onde veio cada parte

| Etapa da disciplina | EvidÃªncia no repositÃ³rio | Autoria |
| --- | --- | --- |
| CÃ³digo-base e primeiras features (02/09 a 06/10) | commits `d9f05c7` a `e28c402` | professor Juliano â€” base do curso |
| Aula 9 â€” testes automatizados | PR #1 e commit `12eb767` | mÃ¡quina do laboratÃ³rio (`L16-M01`) |
| Aula 10 â€” GerÃªncia de ConfiguraÃ§Ã£o | PR #2, commit `1c5f210`, `src/repositorio_pessoas.py` | `9eb9aa4` pelo colega Luis Dutra; merge por Cler Andrade |
| Aula 11 â€” Docker e replicaÃ§Ã£o MySQL | `infra/compose.yaml`, commit `4629f9f` | Cler Andrade |
| Aula 12 â€” persistÃªncia e colaboraÃ§Ã£o | PR #1 no repo do So1d, PR #3, commit `e289160`, `src/repositorio_pessoas_mysql.py` | PR aberto por ClerAndrade; merge por Cler Andrade |
| PadronizaÃ§Ã£o e qualidade | commits `5794cc2`, `b50847c`, `2441169` | Cler Andrade |
| Testes ampliados | commit `73e525c` | Cler Andrade |
| DocumentaÃ§Ã£o e relatÃ³rio | commits `docs: ...` | Cler Andrade |

## O problema de identidade `L16-M01`

Alguns commits feitos nas aulas 9 e 12 aparecem como
`L16-M01 <l16-m01@laboratorio.local>` porque a configuraÃ§Ã£o local do Git na
mÃ¡quina do laboratÃ³rio estava assim:

- `19e498a` e `12eb767` â€” preparaÃ§Ã£o e testes da Aula 9 neste repositÃ³rio;
- `3881778`, `df8955b` e `6f646af` â€” correÃ§Ã£o, documentaÃ§Ã£o e DAO MySQL no
  repositÃ³rio do colega, dentro do PR #1 aberto pela conta `ClerAndrade`.

Isso Ã© um erro de configuraÃ§Ã£o, nÃ£o uma autoria diferente. NÃ£o reescrevi esses
commits: eles jÃ¡ estÃ£o publicados, fazem parte de PRs mesclados e alterar os
hashes quebraria a evidÃªncia da colaboraÃ§Ã£o. A correÃ§Ã£o foi aplicada no
repositÃ³rio em 19/11:

```powershell
git config user.name "Cler Andrade"
git config user.email "115158502+ClerAndrade@users.noreply.github.com"
```

A partir do commit `e289160`, todos os commits novos saem com **Cler Andrade**
como autor. O e-mail Ã© o `noreply` da conta GitHub, o mesmo usado nos merges
de 21/10 e 04/11.

## Sobre o requisito de 17 semanas

O histÃ³rico real nÃ£o tem um commit prÃ³prio por semana letiva desde o inÃ­cio da
disciplina. Os primeiros registros com a minha participaÃ§Ã£o sÃ£o de 14/10; o
resto das semanas iniciais Ã© cÃ³digo publicado pelo professor. NÃ£o foram
criados commits com data retroativa. A continuaÃ§Ã£o estÃ¡ planejada em
`documentos/plano-semanal.md`, com atividades reais para as semanas restantes.

## Links dos Pull Requests

- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3
- https://github.com/So1d/gqs-cadatro-pessoas/pull/1
