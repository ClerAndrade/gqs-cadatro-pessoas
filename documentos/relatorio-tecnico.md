# Relatório técnico — Cadastro de Pessoas

**Disciplina:** Gestão da Qualidade de Software — UTFPR, campus Medianeira, 2026/2  
**Autor:** Cler Andrade  
**Data:** 19 de novembro de 2026  
**Repositório:** https://github.com/ClerAndrade/gqs-cadatro-pessoas

## 1. O que era para entregar

O trabalho não era criar um projeto novo do zero, e sim continuar o mesmo
Cadastro de Pessoas ao longo da disciplina, deixando cada prática registrada no
Git: funções e classes, análise estática com Pylint e RADON, padrões de
commit, hooks de pre-commit, testes com PyTest, colaboração com outro
estudante por fork e Pull Request, camada de persistência com DAO e MySQL,
Docker Compose, documentação e um diário/how-to em PDF.

O repositório que usei foi `gqs-cadatro-pessoas` (o nome do remoto mesmo está
assim, com "cadatro"). Ele já existia e já tinha histórico, então continuei a
partir dele em vez de abrir outro.

## 2. Diário de desenvolvimento

### 02/09 a 06/10 — o ponto de partida

O código-base e as primeiras features foram publicados pelo professor
Juliano. Tem menu, `Pessoa`, `CadastroPessoas`, operações de consulta, alteração
e lista. Não sou autor desses commits e não mexi neles para fingir autoria.

### 14/10 — Aula 9, testes automatizados

Preparei o ambiente e escrevi os primeiros testes do cadastro. O merge do PR
#1 em 21/10 fechou essa etapa. A máquina do laboratório estava com o Git
configurado como `L16-M01 <l16-m01@laboratorio.local>`, e foi com essa
identidade que esses dois commits saíram. Mais adiante explico como isso foi
tratado.

### 03/11 a 04/11 — Aula 10, separar regras de armazenamento

O colega Luis Dutra (So1d) contribuiu com o contrato `RepositorioPessoas` e a
implementação em memória pelo PR #2. Eu revisei e integrei em 04/11. Antes
disso, `CadastroPessoas` guardava tudo numa lista própria; depois, passou a
delegar para o repositório. Essa separação foi o que permitiu trocar memória
por MySQL sem reescrever as regras.

### 11/11 a 18/11 — Aula 11 e 12, Docker, MySQL e colaboração

Montei o principal e a réplica MySQL 8.4.13 com o compose da Aula 11, com
GTID e volumes separados. Na Aula 12 escrevi o DAO `RepositorioPessoasMySQL`
no repositório do colega: `INSERT`, `SELECT` e `UPDATE`, com leitura das
variáveis de ambiente e `ClientFlag.FOUND_ROWS` para o `UPDATE` devolver
quantas linhas foram afetadas. Abri o PR #1 no repositório dele, que foi
integrado em 18/11. No mesmo período corrigi o `alterar()` para delegar a
escrita ao repositório em vez de mudar diretamente o objeto retornado pela
busca.

Em 18/11 o So1d abriu o PR #3 aqui, devolvendo essa persistência para o meu
repositório.

### 19/11 — revisão, consolidação e arrumos

Foi o dia de maior volume, e cada mudança virou um commit separado:

| Commit | O que mudou |
| --- | --- |
| `e289160` | merge revisado do PR #3, com mensagem de merge real |
| `5794cc2` | nomes em `snake_case`, docstrings e Pylint sem exceções escondidas |
| `2441169` | `executar()` de B(8) para A(2) com dicionário de ações |
| `4629f9f` | `infra/compose.yaml`, manual do banco, dependências de qualidade |
| `73e525c` | suíte de 23 testes, incluindo DAO com conector falso |
| `b50847c` | Pylint passou a usar a versão 3.15 que realmente roda aqui |
| `ac055fd` | README, CONTRIBUTING, métricas e rastreabilidade |

## 3. Problemas que encontrei e como resolvi

- **README mentia sobre a execução.** Mandava `python cadastro.py`, mas o
  arquivo sempre foi `src/main.py`. Corrigi e acrescentei os comandos de
  ambiente, MySQL e verificações.
- **CONTRIBUTING mandava clonar o repositório do professor.** Agora fala do
  fluxo que usamos de verdade e dos quatro PRs envolvidos.
- **`alterar()` mudava o objeto na mão.** A versão antiga buscava a pessoa e
  chamava os setters nela. Agora monta uma `Pessoa` nova e chama
  `repositorio.alterar()`. O teste `test_alterar_delega_ao_repositorio` cobre
  essa delegação.
- **Pylint com regras desligadas.** A configuração anterior desabilitava
  `invalid-name`, `missing-function-docstring`, `missing-class-docstring` e
  `trailing-whitespace`. Tirei as exceções, renomeei os métodos e escrevi as
  docstrings. Nota foi de 9,83 para 10,00. O detalhamento está em
  `documentos/checklist-pylint.md`.
- **RADON apontava um bloco B.** `executar()` tinha complexidade 8 por causa
  da cadeia de `if/elif` do menu. Extraí `processar_opcao()` e deixei o laço
  simples. Média do projeto caiu de 1,85 para 1,80 e não sobrou bloco B.
- **pre-commit não verificava testes nem métricas.** Só rodava Pylint, e com o
  Python do sistema, que não tem as dependências. Apontei os três hooks para
  `.venv/Scripts/python.exe` e incluí pytest e RADON. Os três passaram nos
  commits acima.
- **Faltava infraestrutura no repositório.** O compose da Aula 11 existia no
  fork, mas não aqui. Entrou em `infra/compose.yaml` com um README de como
  subir, criar a tabela e configurar a réplica.
- **Só dois testes.** Subiram para 23, cobrindo repositório em memória,
  escolha de repositório no `main` e DAO MySQL com `mysql.connector.connect`
  substituído por um objeto falso. Não é necessário ter banco rodando para
  rodar a suíte.
- **Identidade de autor errada.** Resolvida para os commits novos e
  documentada; os commits já publicados não foram reescritos.

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
criação da tabela que está em `infra/README.md`. Depois, na raiz:

```powershell
$env:CADASTRO_REPOSITORIO = "mysql"
$env:DB_HOST = "localhost"
$env:DB_PORT = "3307"
$env:DB_USER = "root"
$env:DB_PASSWORD = "root_lab_2026"
$env:DB_NAME = "cadastro"
python src\main.py
```

A senha é a do laboratório, igual à do compose didático. Para validar o
compose sem subir contêiner, rodei `docker compose config --quiet` na pasta
`infra` e o código de saída foi 0.

## 5. Evidências

| Evidência | Onde conferir |
| --- | --- |
| Testes automatizados | 23 passos em `tests/`, comando `python -m pytest -v` |
| Análise estática | `documentos/checklist-pylint.md`, nota 10,00/10 |
| Complexidade | `documentos/metricas-radon.md`, média A (1,80) |
| Docker / replicação | `infra/compose.yaml` e `infra/README.md` |
| DAO MySQL | `src/repositorio_pessoas_mysql.py` e `tests/test_repositorio_mysql.py` |
| Colaboração | PR #1 e #2 aqui, PR #1 no repo do So1d, PR #3 integrado |
| Histórico | `git log` do repositório, mensagens `feat`, `fix`, `refactor`, `test`, `chore`, `docs` |

Links:

- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3
- https://github.com/So1d/gqs-cadatro-pessoas/pull/1

## 6. Autoria

Três commits publicados em 14/10 e 17/11 aparecem como `L16-M01
<l16-m01@laboratorio.local>` por causa da configuração da máquina do
laboratório. O PR da Aula 12 foi aberto pela conta `ClerAndrade` e integrado
pelo colega, o que comprova de quem foi a iniciativa. Mantive esses commits do
jeito que estão: reescrever autoria em histórico já mesclado apagaria a
evidência dos PRs.

Em 19/11 configurei o repositório com:

```powershell
git config user.name "Cler Andrade"
git config user.email "115158502+ClerAndrade@users.noreply.github.com"
```

Daí em diante todo commit sai com **Cler Andrade** como autor, incluindo o
merge do PR #3.

## 7. Sobre as 17 semanas

Não tenho como mostrar um commit meu por semana letiva desde 02/09: o
histórico inicial é do professor e o meu começa em 14/10. Não inventei data
antiga nem commit vazio para completar o quadro. O que deixei registrado foi
um plano honesto com atividades reais para as semanas restantes em
`documentos/plano-semanal.md`, e a partir de agora cada atividade vira um
commit quando acontecer.

## 8. Limitações

Não subi os contêineres durante esta revisão porque o Docker Desktop não
estava com o daemon ativo (`docker info` falhou em conectar no pipe do Linux).
O compose foi validado sintaticamente e o DAO foi testado com um conector
falso, mas o teste de ponta a ponta com MySQL rodando ficou para a próxima
sessão. Isso não muda os resultados de Pylint, RADON e PyTest, que rodaram
localmente.

O PDF foi gerado a partir deste Markdown com `markdown` e WeasyPrint. O HTML
intermediário está junto, em `documentos/relatorio-tecnico.html`, para dar para
conferir o conteúdo sem abrir o PDF.
