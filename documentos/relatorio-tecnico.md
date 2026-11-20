# Relatório técnico — Cadastro de Pessoas

**Disciplina:** Gestão da Qualidade de Software · UTFPR, campus Medianeira · 2026/2  
**Autor:** Cler Andrade  
**Última revisão:** 20 de novembro de 2026  
**Repositório:** https://github.com/ClerAndrade/gqs-cadatro-pessoas

---

Não escrevi isto de uma vez no fim. É o que ficou registrado enquanto eu voltava
ao projeto para conferir as coisas: abri o `git log`, reli os slides, rodei as
ferramentas e fui anotando onde cada prática aparece. Se algum comando aqui
aparece duas vezes, é porque eu rodei mesmo — primeiro para descobrir o que
estava errado, depois para confirmar que tinha ficado certo.

## 19/11: arrumando o que estava aberto

Quando entrei no repositório, a `main` estava um commit atrás da `origin/main`
e o PR #3 do So1d ainda estava pendente. Antes de mexer em qualquer arquivo
rodei `git status` e `git log --oneline`. O PR devolvia o DAO MySQL para o meu
repositório; em vez de deixar ele aberto, puxei para `review/pr-3`, revisei e
fechei com `e289160 Merge pull request #3 from So1d/main`.

Depois disso fui consertando uma coisa por vez, sempre com commit separado:

- `5794cc2` — passei os métodos para `snake_case`, escrevi as docstrings e tirei
  do `.pylintrc` as regras que estavam desligadas para o Pylint "dar 10";
- `2441169` — quebrei a cadeia de `if/elif` do menu. `executar()` saiu de B(8)
  para A(2) no RADON depois que o dicionário de ações virou `processar_opcao()`;
- `4629f9f` — trouxe o `compose.yaml` da Aula 11 para `infra/`, com o manual do
  banco e as dependências de qualidade no `requirements.txt`;
- `73e525c` — subi a suíte de 23 testes, incluindo o DAO com conector falso;
- `b50847c` — o `.pylintrc` passou a dizer `py-version=3.15`, que é a versão que
  realmente roda na máquina;
- `ac055fd`, `3b80a72`, `c440534`, `2f152d9` — documentação, relatório em PDF e
  uma correção de acentos que tinha saído torto.

## 20/11: conferindo com o enunciado e com os slides

Hoje recebi a versão final do enunciado e comparei com o que estava no repo.
Também reli os PDFs das Aulas 1 a 12. O resultado dessa conferência está em
`documentos/auditoria-final.md`, mas o resumo é este:

- o modelo de `documentos/checklist-inspecao.md` já existia, mas o formulário
  **preenchido** na Aula 6 estava só no repositório paralelo. Copiei para
  `checklist-inspecao-preenchido-aula6.md`. Quase fiz besteira de copiar por
  cima do modelo; vi no `git diff` e recuperei o original com `git checkout`,
  deixando os dois arquivos;
- a Aula 8 pedia `tests/test_pessoa.py`. Criei quatro testes de getters/setters
  e a suíte foi para 27;
- os commits feitos na máquina do laboratório apareciam como `L16-M01`. Coloquei
  um `.mailmap` e liguei `git config log.mailmap true`;
- fechei a conferência com uma tag anotada `v1.0.0-entrega`, para marcar o ponto
  de entrega como linha de base.

Os slides bateram com o que já tinha, com um ou outro reforço. Aula 4 e 5 eram
RADON — está em `metricas-radon.md`. Aula 6 era Pylint — está no
`checklist-pylint.md` e no formulário preenchido que acabei de trazer. Aula 8
queria PyTest e o teste da entidade — agora existe. Aula 9 e 10 falavam de itens
de configuração, fork e Pull Request — além dos PRs, tem a tag. Aula 11 e 12
eram MySQL, réplica e DAO — estão em `infra/` e em
`src/repositorio_pessoas_mysql.py`. Os exercícios de Selenium ficaram de fora,
como o próprio enunciado final permite.

## Coisas que deram trabalho

**O README mentia.** Mandava `python cadastro.py`, mas o arquivo sempre foi
`src/main.py`. Agora o README diz como criar a `.venv`, instalar, rodar testes e
subir o banco.

**O CONTRIBUTING mandava clonar o repo do professor.** Foi trocado pelo fluxo
que usamos de verdade: branch, commit, push, PR e os quatro Pull Requests da
atividade.

**`alterar()` mudava o objeto na mão.** A função antiga buscava a pessoa e
chamava os setters nela. Passei a montar uma `Pessoa` nova e chamar
`repositorio.alterar()`. O teste `test_alterar_delega_ao_repositorio` cobre isso.
Sem essa separação, trocar memória por MySQL ia exigir reescrever a regra de
negócio.

**Pylint com exceções escondidas.** A configuração anterior desligava
`invalid-name`, `missing-function-docstring`, `missing-class-docstring` e
`trailing-whitespace`. Tirei as exceções, renomeei os métodos e escrevi as
docstrings. A nota foi de 9,83 para 10,00. O antes/depois está no checklist.

**RADON apontava um bloco B.** Era o `executar()` com a cadeia de opções do
menu. A média do projeto caiu de 1,85 para 1,80 e não sobrou nenhum bloco B ou
C em `src/`.

**pre-commit não verificava teste nenhum.** Só chamava o Pylint, e com o Python
do sistema, que não tem as dependências do projeto. Apontei os três hooks para
`.venv/Scripts/python.exe` e incluí pytest e RADON. Eles rodaram nos commits
desta auditoria.

**Acentos corrompidos.** O PowerShell 5.1 leu meus `.ps1` sem BOM como ANSI e
o PDF saiu com "Relat?rio" e "gest?o". Corrigi os arquivos de `cp1252` para
`utf-8` e passei a salvar os scripts novos com BOM UTF-8. O PDF foi regerado.

**Docker.** O daemon não subiu na máquina (`docker info` falhou em conectar no
pipe do Linux). Validei o compose com `docker compose config --quiet`, que
devolveu 0, e testei o DAO com um conector falso. O teste com MySQL de verdade
ficou pendente e está anotado como limitação.

## Como reproduzir

No PowerShell, na raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pre_commit install
python -m pytest -q
python -m pylint src
python -m radon cc src -a -s
python src\main.py
```

Se quiser usar o banco, entre em `infra`, rode `docker compose up -d`, crie a
tabela conforme `infra/README.md` e volte para a raiz:

```powershell
$env:CADASTRO_REPOSITORIO = "mysql"
$env:DB_HOST = "localhost"
$env:DB_PORT = "3307"
$env:DB_USER = "root"
$env:DB_PASSWORD = "root_lab_2026"
$env:DB_NAME = "cadastro"
python src\main.py
```

A senha é a mesma do compose didático. Para só conferir o arquivo sem subir
contêiner: `Set-Location infra`, `docker compose config --quiet`.

## O que conferi de novo hoje

```
python -m pytest -q        -> 27 passed in 0.16s
python -m pylint src       -> 10.00/10
python -m radon cc src -a  -> 49 blocos, média A (1,80)
git status --short --branch -> ## main...origin/main
docker compose config --quiet -> código de saída 0
```

O PDF em `documentos/relatorio-tecnico.pdf` saiu deste Markdown. Deixei o HTML
intermediário em `documentos/relatorio-tecnico.html` para conferir o conteúdo
sem precisar abrir o leitor de PDF.

## Autoria

Parte dos commits de 14/10 e 17/11 saiu com `L16-M01
<l16-m01@laboratorio.local>` porque era a identidade configurada na máquina do
laboratório. Hoje coloquei no `.mailmap`:

```
Cler Andrade <115158502+ClerAndrade@users.noreply.github.com> L16-M01 <l16-m01@laboratorio.local>
```

e ativei `git config log.mailmap true`. Com isso, `git log` e `git shortlog`
mostram **Cler Andrade** no lugar daquele nome estranho. Não reescrevi os
objetos dos commits antigos: eles sustentam os Pull Requests já mesclados no
GitHub e mudar os hashes quebraria essa evidência. Os commits do professor
continuam com o nome dele porque são o ponto de partida permitido; o commit do
colega continua com o nome dele porque é a prova da colaboração. Todo commit que
eu fiz de 19/11 em diante sai como Cler Andrade.

Os PRs que compõem a evidência:

- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3
- https://github.com/So1d/gqs-cadatro-pessoas/pull/1

## As 17 semanas

Não tenho como apresentar um commit meu em cada uma das 17 semanas letivas. O
histórico começa com os commits do professor e a minha participação aparece a
partir de 14/10. Deixei isso registrado em `plano-semanal.md` e em
`rastreabilidade.md`, sem inventar data nem commit vazio para completar o
quadro. O que der para fazer é continuar commitando cada atividade real que
aparecer.

## O que ficou de fora

O teste ponta a ponta com o MySQL rodando. O código do DAO e o compose estão
prontos e foram validados separadamente, mas o Docker Desktop não estava com o
daemon ativo durante esta revisão. Assim que ele subir, o comando é o que está
em `infra/README.md`; não muda nada do que foi medido acima.
