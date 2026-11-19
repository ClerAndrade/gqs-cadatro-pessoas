# RelatÃ³rio tÃ©cnico â€” Cadastro de Pessoas

**Disciplina:** GestÃ£o da Qualidade de Software â€” UTFPR, campus Medianeira, 2026/2  
**Autor:** Cler Andrade  
**Data:** 19 de novembro de 2026  
**RepositÃ³rio:** https://github.com/ClerAndrade/gqs-cadatro-pessoas

## 1. O que era para entregar

O trabalho nÃ£o era criar um projeto novo do zero, e sim continuar o mesmo
Cadastro de Pessoas ao longo da disciplina, deixando cada prÃ¡tica registrada no
Git: funÃ§Ãµes e classes, anÃ¡lise estÃ¡tica com Pylint e RADON, padrÃµes de
commit, hooks de pre-commit, testes com PyTest, colaboraÃ§Ã£o com outro
estudante por fork e Pull Request, camada de persistÃªncia com DAO e MySQL,
Docker Compose, documentaÃ§Ã£o e um diÃ¡rio/how-to em PDF.

O repositÃ³rio que usei foi `gqs-cadatro-pessoas` (o nome do remoto mesmo estÃ¡
assim, com "cadatro"). Ele jÃ¡ existia e jÃ¡ tinha histÃ³rico, entÃ£o continuei a
partir dele em vez de abrir outro.

## 2. DiÃ¡rio de desenvolvimento

### 02/09 a 06/10 â€” o ponto de partida

O cÃ³digo-base e as primeiras features foram publicados pelo professor
Juliano. Tem menu, `Pessoa`, `CadastroPessoas`, operaÃ§Ãµes de consulta, alteraÃ§Ã£o
e lista. NÃ£o sou autor desses commits e nÃ£o mexi neles para fingir autoria.

### 14/10 â€” Aula 9, testes automatizados

Preparei o ambiente e escrevi os primeiros testes do cadastro. O merge do PR
#1 em 21/10 fechou essa etapa. A mÃ¡quina do laboratÃ³rio estava com o Git
configurado como `L16-M01 <l16-m01@laboratorio.local>`, e foi com essa
identidade que esses dois commits saÃ­ram. Mais adiante explico como isso foi
tratado.

### 03/11 a 04/11 â€” Aula 10, separar regras de armazenamento

O colega Luis Dutra (So1d) contribuiu com o contrato `RepositorioPessoas` e a
implementaÃ§Ã£o em memÃ³ria pelo PR #2. Eu revisei e integrei em 04/11. Antes
disso, `CadastroPessoas` guardava tudo numa lista prÃ³pria; depois, passou a
delegar para o repositÃ³rio. Essa separaÃ§Ã£o foi o que permitiu trocar memÃ³ria
por MySQL sem reescrever as regras.

### 11/11 a 18/11 â€” Aula 11 e 12, Docker, MySQL e colaboraÃ§Ã£o

Montei o principal e a rÃ©plica MySQL 8.4.13 com o compose da Aula 11, com
GTID e volumes separados. Na Aula 12 escrevi o DAO `RepositorioPessoasMySQL`
no repositÃ³rio do colega: `INSERT`, `SELECT` e `UPDATE`, com leitura das
variÃ¡veis de ambiente e `ClientFlag.FOUND_ROWS` para o `UPDATE` devolver
quantas linhas foram afetadas. Abri o PR #1 no repositÃ³rio dele, que foi
integrado em 18/11. No mesmo perÃ­odo corrigi o `alterar()` para delegar a
escrita ao repositÃ³rio em vez de mudar diretamente o objeto retornado pela
busca.

Em 18/11 o So1d abriu o PR #3 aqui, devolvendo essa persistÃªncia para o meu
repositÃ³rio.

### 19/11 â€” revisÃ£o, consolidaÃ§Ã£o e arrumos

Foi o dia de maior volume, e cada mudanÃ§a virou um commit separado:

| Commit | O que mudou |
| --- | --- |
| `e289160` | merge revisado do PR #3, com mensagem de merge real |
| `5794cc2` | nomes em `snake_case`, docstrings e Pylint sem exceÃ§Ãµes escondidas |
| `2441169` | `executar()` de B(8) para A(2) com dicionÃ¡rio de aÃ§Ãµes |
| `4629f9f` | `infra/compose.yaml`, manual do banco, dependÃªncias de qualidade |
| `73e525c` | suÃ­te de 23 testes, incluindo DAO com conector falso |
| `b50847c` | Pylint passou a usar a versÃ£o 3.15 que realmente roda aqui |
| `ac055fd` | README, CONTRIBUTING, mÃ©tricas e rastreabilidade |

## 3. Problemas que encontrei e como resolvi

- **README mentia sobre a execuÃ§Ã£o.** Mandava `python cadastro.py`, mas o
  arquivo sempre foi `src/main.py`. Corrigi e acrescentei os comandos de
  ambiente, MySQL e verificaÃ§Ãµes.
- **CONTRIBUTING mandava clonar o repositÃ³rio do professor.** Agora fala do
  fluxo que usamos de verdade e dos quatro PRs envolvidos.
- **`alterar()` mudava o objeto na mÃ£o.** A versÃ£o antiga buscava a pessoa e
  chamava os setters nela. Agora monta uma `Pessoa` nova e chama
  `repositorio.alterar()`. O teste `test_alterar_delega_ao_repositorio` cobre
  essa delegaÃ§Ã£o.
- **Pylint com regras desligadas.** A configuraÃ§Ã£o anterior desabilitava
  `invalid-name`, `missing-function-docstring`, `missing-class-docstring` e
  `trailing-whitespace`. Tirei as exceÃ§Ãµes, renomeei os mÃ©todos e escrevi as
  docstrings. Nota foi de 9,83 para 10,00. O detalhamento estÃ¡ em
  `documentos/checklist-pylint.md`.
- **RADON apontava um bloco B.** `executar()` tinha complexidade 8 por causa
  da cadeia de `if/elif` do menu. ExtraÃ­ `processar_opcao()` e deixei o laÃ§o
  simples. MÃ©dia do projeto caiu de 1,85 para 1,80 e nÃ£o sobrou bloco B.
- **pre-commit nÃ£o verificava testes nem mÃ©tricas.** SÃ³ rodava Pylint, e com o
  Python do sistema, que nÃ£o tem as dependÃªncias. Apontei os trÃªs hooks para
  `.venv/Scripts/python.exe` e incluÃ­ pytest e RADON. Os trÃªs passaram nos
  commits acima.
- **Faltava infraestrutura no repositÃ³rio.** O compose da Aula 11 existia no
  fork, mas nÃ£o aqui. Entrou em `infra/compose.yaml` com um README de como
  subir, criar a tabela e configurar a rÃ©plica.
- **SÃ³ dois testes.** Subiram para 23, cobrindo repositÃ³rio em memÃ³ria,
  escolha de repositÃ³rio no `main` e DAO MySQL com `mysql.connector.connect`
  substituÃ­do por um objeto falso. NÃ£o Ã© necessÃ¡rio ter banco rodando para
  rodar a suÃ­te.
- **Identidade de autor errada.** Resolvida para os commits novos e
  documentada; os commits jÃ¡ publicados nÃ£o foram reescritos.

## 4. Como reproduzir

No PowerShell, a partir da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pre_commit install
python -m pytest -v
python -m pylint src
python -m radon cc src -a -s
python src\main.py
```

Para usar o banco, primeiro `Set-Location infra`, `docker compose up -d` e a
criaÃ§Ã£o da tabela que estÃ¡ em `infra/README.md`. Depois, na raiz:

```powershell
$env:CADASTRO_REPOSITORIO = "mysql"
$env:DB_HOST = "localhost"
$env:DB_PORT = "3307"
$env:DB_USER = "root"
$env:DB_PASSWORD = "root_lab_2026"
$env:DB_NAME = "cadastro"
python src\main.py
```

A senha Ã© a do laboratÃ³rio, igual Ã  do compose didÃ¡tico. Para validar o
compose sem subir contÃªiner, rodei `docker compose config --quiet` na pasta
`infra` e o cÃ³digo de saÃ­da foi 0.

## 5. EvidÃªncias

| EvidÃªncia | Onde conferir |
| --- | --- |
| Testes automatizados | 23 passos em `tests/`, comando `python -m pytest -v` |
| AnÃ¡lise estÃ¡tica | `documentos/checklist-pylint.md`, nota 10,00/10 |
| Complexidade | `documentos/metricas-radon.md`, mÃ©dia A (1,80) |
| Docker / replicaÃ§Ã£o | `infra/compose.yaml` e `infra/README.md` |
| DAO MySQL | `src/repositorio_pessoas_mysql.py` e `tests/test_repositorio_mysql.py` |
| ColaboraÃ§Ã£o | PR #1 e #2 aqui, PR #1 no repo do So1d, PR #3 integrado |
| HistÃ³rico | `git log` do repositÃ³rio, mensagens `feat`, `fix`, `refactor`, `test`, `chore`, `docs` |

Links:

- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3
- https://github.com/So1d/gqs-cadatro-pessoas/pull/1

## 6. Autoria

TrÃªs commits publicados em 14/10 e 17/11 aparecem como `L16-M01
<l16-m01@laboratorio.local>` por causa da configuraÃ§Ã£o da mÃ¡quina do
laboratÃ³rio. O PR da Aula 12 foi aberto pela conta `ClerAndrade` e integrado
pelo colega, o que comprova de quem foi a iniciativa. Mantive esses commits do
jeito que estÃ£o: reescrever autoria em histÃ³rico jÃ¡ mesclado apagaria a
evidÃªncia dos PRs.

Em 19/11 configurei o repositÃ³rio com:

```powershell
git config user.name "Cler Andrade"
git config user.email "115158502+ClerAndrade@users.noreply.github.com"
```

DaÃ­ em diante todo commit sai com **Cler Andrade** como autor, incluindo o
merge do PR #3.

## 7. Sobre as 17 semanas

NÃ£o tenho como mostrar um commit meu por semana letiva desde 02/09: o
histÃ³rico inicial Ã© do professor e o meu comeÃ§a em 14/10. NÃ£o inventei data
antiga nem commit vazio para completar o quadro. O que deixei registrado foi
um plano honesto com atividades reais para as semanas restantes em
`documentos/plano-semanal.md`, e a partir de agora cada atividade vira um
commit quando acontecer.

## 8. LimitaÃ§Ãµes

NÃ£o subi os contÃªineres durante esta revisÃ£o porque o Docker Desktop nÃ£o
estava com o daemon ativo (`docker info` falhou em conectar no pipe do Linux).
O compose foi validado sintaticamente e o DAO foi testado com um conector
falso, mas o teste de ponta a ponta com MySQL rodando ficou para a prÃ³xima
sessÃ£o. Isso nÃ£o muda os resultados de Pylint, RADON e PyTest, que rodaram
localmente.

O PDF foi gerado a partir deste Markdown com `markdown` e WeasyPrint. O HTML
intermediÃ¡rio estÃ¡ junto, em `documentos/relatorio-tecnico.html`, para dar para
conferir o conteÃºdo sem abrir o PDF.
