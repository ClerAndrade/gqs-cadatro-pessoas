# Rastreabilidade e autoria

Neste relatório, A = `ClerAndrade` e B = `So1d`, conforme o slide 57 e o título `(A -> B)` do Pull Request de persistência. As tabelas identificam sempre o login para evitar confusão com a convenção invertida do Relatório 11.

## De onde veio cada parte

| Etapa da disciplina | Evidência no repositório | Autoria |
|---|---|---|
| Código-base e primeiras features (02/09 a 06/10) | commits iniciais do professor | Juliano Rodrigo Lamb — base do curso |
| Aula 9 — testes automatizados | PR #1 de A e `b12760d` | `ClerAndrade` (5 commits `L16-M01` mapeados) |
| Aula 10 — Gerência de Configuração | PR #2 de A e `1c5f210` | `So1d` enviou; `ClerAndrade` integrou |
| Aula 11 — Docker e replicação | `infra/compose.yaml` e `4629f9f` | `ClerAndrade` |
| Aula 12 — persistência e colaboração | PR #1 de B (`972061c`) e PR #3 de A (`e289160`) | `ClerAndrade` enviou para B; `So1d` devolveu; `ClerAndrade` integrou |
| Padronização e qualidade | `5794cc2`, `b50847c`, `2441169` | `ClerAndrade` |
| Testes ampliados | `73e525c`, `ab1ce09` | `ClerAndrade` |
| Documentação e relatório | commits `docs: ...` a partir de `3b80a72` | `ClerAndrade` |
| Reconstrução das 17 semanas | `documentos/semanas/semana-01.md` a `semana-17.md` | `ClerAndrade`, em 25/11/2026 |

## O problema de identidade `L16-M01`

Alguns commits gravados na máquina do laboratório aparecem como `L16-M01 <l16-m01@laboratorio.local>`:

- `19e498a` e `12eb767` — preparação e testes da Aula 9 neste repositório;
- `3881778`, `df8955b` e `6f646af` — correção, documentação e DAO MySQL no repositório de B, dentro do PR #1 aberto pela conta `ClerAndrade`.

A correção foi aplicada em 19/11 com `.mailmap` e `git config log.mailmap true`. Os objetos não foram reescritos porque sustentam PRs já mesclados no GitHub; alterar os hashes quebraria a evidência da colaboração. O comando que mostra a identidade corrigida é:

```powershell
git --no-pager log --format='%h | %aN <%aE> | %s'
```

O histórico mapeado contém 49 commits: 28 de Cler Andrade, 19 de Juliano Rodrigo Lamb, 1 de Luis Felipe Machado Dutra e 1 de Luis Dutra.

## Sobre o requisito de 17 semanas

O histórico original não tem um commit próprio por semana letiva desde o início da disciplina. As semanas iniciais contêm apenas commits do professor e os primeiros registros de Cler Andrade aparecem em 14/10. Não foram criados commits com data retroativa.

Para atender ao item 5 do enunciado sem fabricar passado, cada etapa foi reconstruída em 25/11/2026 em `documentos/semanas/`, com um commit próprio por semana. Esses registros são explícitos sobre a data da reconstrução e não substituem os objetos originais.

## Links dos Pull Requests

- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3
- https://github.com/So1d/gqs-cadatro-pessoas/pull/1
