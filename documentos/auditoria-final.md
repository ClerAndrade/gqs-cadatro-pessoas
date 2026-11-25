# Auditoria do projeto contra o enunciado final

Conferência feita em 25/11/2026. Foram comparados o enunciado final do Projeto Integrador, os slides das Aulas 1 a 12, o Relatório 11, os checklists existentes e o estado real do repositório (`git status`, `git log`, arquivos versionados e saída das ferramentas).

## O que foi verificado

| Item do enunciado | Evidência no repositório | Situação |
|---|---|---|
| Evolução do Cadastro de Pessoas | `src/pessoa.py`, `src/cadastro.py`, `src/main.py` e commits de refatoração | OK |
| Funções, módulos e classes / OO | `Pessoa`, `CadastroPessoas`, `RepositorioPessoas` e duas implementações | OK |
| RADON e análise de complexidade | `documentos/metricas-radon.md`; `executar()` de B(8) para A(2) | OK |
| Pylint e correções | `documentos/checklist-pylint.md`; 9,83 para 10,00 | OK |
| pre-commit | `.pre-commit-config.yaml` com pylint, pytest e radon; hooks executados com sucesso | OK |
| Padrões registrados | `CONTRIBUTING.md`, `.pylintrc` | OK |
| PyTest | `tests/` com 27 testes, incluindo `test_pessoa.py` e DAO falso | OK |
| Git, branches e integração | `main`, branches locais e quatro merges verificáveis | OK |
| Colaboração por fork/PR | PR #1 e #2 em `ClerAndrade`; PR #1 em `So1d`; PR #3 em `ClerAndrade` | OK |
| DAO e MySQL | `src/repositorio_pessoas_mysql.py`; contrato com quatro operações | OK |
| Docker / Compose | `infra/compose.yaml`; `docker compose config --quiet` com código 0 | OK, com ressalva de daemon |
| Documentação técnica | README, CONTRIBUTING, checklists, métricas, rastreabilidade e relatório | OK |
| Rastreabilidade (GCS) | `documentos/rastreabilidade.md`, PRs, commits e tag `v1.0.0-entrega` | OK |
| Autoria identificável | `.mailmap` com 5 commits `L16-M01` mapeados para Cler Andrade | OK, com ressalva histórica |
| 1 commit próprio por semana letiva (17) | histórico original sem distribuição semanal; reconstrução em 25/11 | Reconstruído, não original |
| Relatório técnico em PDF | `documentos/relatorio-tecnico.pdf`, capa UTFPR e 8 figuras | OK |
| Selenium | fora do escopo conforme item 9 do enunciado | Não incluído |

## Situação do requisito quantitativo

O histórico original não possui um commit próprio em cada uma das 17 semanas letivas. Os primeiros commits de Cler Andrade no repositório aparecem em 14/10; antes disso há apenas commits do professor. Alterar datas para preencher o quadro seria fabricar histórico.

Como o item 5 do enunciado prevê a reconstrução quando a evolução não pode ser demonstrada, foram criados 17 registros reais em `documentos/semanas/`, um por semana, cada um com commit próprio e mensagem padronizada. Todos foram feitos em 25/11/2026 e estão identificados como reconstrução. Isso não apaga a ausência original, mas torna a trilha de cada prática verificável sem inventar passado.

## Conferência dos slides

| Aula | Prática trabalhada | Onde aparece no projeto |
|---|---|---|
| 1 | Qualidade, revisão e inspeção | `documentos/checklist-inspecao.md` e commits iniciais |
| 2 | Inspeção com checklist | `documentos/auditoria-aula2.md` e folha em `evidencias/` |
| 3 | Retrabalho a partir dos achados e funções | modularização de `src/main.py` e commits `refactor:` |
| 4 | Medidas, métricas e complexidade com RADON | `documentos/metricas-radon.md` |
| 5 | Leitura das métricas e refatoração | antes/depois em `metricas-radon.md` |
| 6 | Padronização e Pylint | `documentos/checklist-pylint.md` e checklist preenchido |
| 7 | Orientação a objetos e checkpoints | `documentos/checkpoints-aula7.md` e contrato de repositório |
| 8 | PyTest e entidade `Pessoa` | `tests/test_pessoa.py` e `casos-teste-ct01-ct02.md` |
| 9/10 | Configuração, baseline, fork e Pull Request | PRs #1/#2/#3, `baseline-indicadores.md`, tag de entrega |
| 11 | MySQL em contêiner, principal e réplica | `infra/compose.yaml` e `infra/README.md` |
| 12 | DAO MySQL, ambiente sem segredo e integração | `repositorio_pessoas_mysql.py`, PR #1 de `So1d`, PR #3 |

Não foram executados nesta máquina: a subida dos contêineres com Docker e os três experimentos de confiabilidade da Aula 12. O Compose foi validado apenas no sintático e o DAO foi testado com conector falso. As capturas de execução com banco real vêm do Relatório 11 e estão atribuídas em `documentos/evidencias/README.md`.

## Autoria

Neste relatório, A = `ClerAndrade` e B = `So1d`, conforme o slide 57 e o título `(A -> B)` do PR de persistência. O `.mailmap` mapeia `L16-M01 <l16-m01@laboratorio.local>` para `Cler Andrade <115158502+ClerAndrade@users.noreply.github.com>`, sem reescrever os objetos publicados.

O histórico mapeado tem 69 commits: 48 de Cler Andrade, 19 de Juliano Rodrigo Lamb, 1 de Luis Felipe Machado Dutra e 1 de Luis Dutra. Os commits do professor continuam com o nome dele porque são o ponto de partida permitido; os do colega permanecem com a autoria original porque são evidência da colaboração.
