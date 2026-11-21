# Auditoria do projeto contra o enunciado final

Conferência feita em 20/11/2026. Comparei o texto final do Projeto Integrador,
os slides das Aulas 1 a 12, os relatórios/checklists que você já tinha e o
estado real do repositório (`git status`, `git log`, arquivos versionados).

## O que foi verificado

| Item do enunciado | Evidência no repositório | Situação |
| --- | --- | --- |
| Evolução do Cadastro de Pessoas | `src/pessoa.py`, `src/cadastro.py`, `src/main.py`, commits de 02/09 a 20/11 | OK |
| Funções, módulos e classes / OO | classes `Pessoa`, `CadastroPessoas`, `RepositorioPessoas` e implementações | OK |
| RADON e análise de complexidade | `documentos/metricas-radon.md`; `executar()` de B(8) para A(2) | OK |
| Pylint e correções | `documentos/checklist-pylint.md`; 9,83 para 10,00 | OK |
| pre-commit | `.pre-commit-config.yaml` com pylint, pytest e radon; hooks rodaram nos commits | OK |
| Padrões registrados | `CONTRIBUTING.md`, `.pylintrc` | OK |
| PyTest | `tests/` com 27 testes, incluindo `test_pessoa.py` da Aula 8 | OK |
| Git, branches e integração | `main`, branches locais, merges dos PRs | OK |
| Colaboração por fork/PR | PR #1 e #2 aqui, PR #1 no repo do So1d, PR #3 integrado | OK |
| DAO e MySQL | `src/repositorio_pessoas_mysql.py`; testes com conector falso | OK |
| Docker / Compose | `infra/compose.yaml` e `infra/README.md`; `docker compose config --quiet` passou | OK |
| Documentação técnica | README, CONTRIBUTING, checklists, métricas, rastreabilidade, relatório | OK |
| Rastreabilidade (GCS) | `documentos/rastreabilidade.md`, PRs, commits e tag de entrega | OK |
| Autoria identificável | `.mailmap`, commits novos como Cler Andrade, PRs verificáveis | OK, com ressalva histórica |
| 1 commit próprio por semana letiva (17) | histórico real começa em 14/10 | **Não atendido no passado**; não foi fabricado |
| Relatório técnico em PDF | `documentos/relatorio-tecnico.pdf`, com capa ABNT/UTFPR | OK |
| Selenium | fora do escopo, conforme item 9 do enunciado | Não versionado no projeto |

Sobre o item quantitativo: existem vários commits meus na mesma semana, mas
isso não cobre as semanas em que só aparecem commits do professor. Reescrever
datas para preencher o quadro seria fabricar histórico, então mantive o que
aconteceu e registrei o plano em `documentos/plano-semanal.md`.

## Conferência dos slides

| Aula | Prática trabalhada | Onde aparece no projeto |
| --- | --- | --- |
| 1 | Qualidade, revisão e inspeção | `documentos/checklist-inspecao.md` (modelo) |
| 2 | Inspeção com checklist | `checklist-inspecao.md` e `checklist-inspecao-preenchido-aula6.md` |
| 3 | Retrabalho a partir dos achados, funções e evolução com Git | modularização de `main.py` e commits `refactor:` |
| 4 | Medidas, métricas e complexidade ciclomática com RADON | `documentos/metricas-radon.md` |
| 5 | RADON e leitura das métricas | mesma evidência, com antes/depois |
| 6 | Padronização e Pylint | `documentos/checklist-pylint.md` e checklist preenchido da Aula 6 |
| 7 | Orientação a objetos e os cinco commits de refatoração | base do repositório + contrato de repositório |
| 8 | PyTest e a proposta de `tests/test_pessoa.py` | `tests/test_pessoa.py` e suíte com 27 testes |
| 9/10 | Gerência de configuração, itens, baseline, fork e Pull Request | PRs #1, #2 e #3, `rastreabilidade.md`, tag `v1.0.0-entrega` |
| 11 | MySQL em contêiner, principal e réplica | `infra/compose.yaml` e `infra/README.md` |
| 12 | DAO MySQL, ambiente sem segredo e integração da contribuição | `repositorio_pessoas_mysql.py`, PR #1 do So1d, PR #3 aqui |

O que os slides pediam e eu não executei até aqui: subir os contêineres com o
Docker Desktop ativo. O daemon não estava disponível na máquina durante a
revisão; o compose foi validado só no sintático e o DAO foi testado com mock.

## Autoria

O `.mailmap` mapeia `L16-M01 <l16-m01@laboratorio.local>` para
`Cler Andrade <115158502+ClerAndrade@users.noreply.github.com>`. Assim,
`git log --use-mailmap` e `git shortlog` mostram os commits da máquina do
laboratório com o nome correto. O `git config log.mailmap true` também foi
ativado neste clone.

Os objetos dos commits antigos não foram reescritos: eles sustentam os PRs que
já foram mesclados no GitHub. Os commits do professor continuam com o nome dele
porque são o ponto de partida permitido, e o commit do colega continua com o
nome dele porque é a evidência da colaboração. O que é trabalho meu está
identificado pelo `.mailmap` e pelos commits a partir de 19/11.
