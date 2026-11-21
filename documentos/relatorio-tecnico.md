Quando chegou a versão final do enunciado, eu já tinha o projeto quase fechado, mas não tinha parado para conferir se ele batia com tudo o que estava sendo pedido. Então abri o Git, abri os slides de novo e fui comparando uma coisa por vez. O que está aqui é esse levantamento, escrito do meu jeito, com os comandos que rodei e também com as coisas que deram errado no caminho.

## 19/11 — o dia em que destravei o PR

Voltei para o repositório e a primeira coisa que fiz foi `git status`. A `main` estava um commit atrás da `origin/main` e o PR #3 do So1d ainda estava aberto. Ele devolvia o DAO MySQL para o meu projeto. Puxei o trabalho para `review/pr-3`, dei uma olhada e fechei com `e289160 Merge pull request #3 from So1d/main`.

Depois disso fui arrumando o que estava ruim, um commit por vez:

- `5794cc2`: nomes dos métodos em `snake_case`, docstrings escritas e as regras que estavam desligadas no `.pylintrc` tiradas dali;
- `2441169`: o menu tinha um `if/elif` enorme dentro de `executar()`. Separei isso em `processar_opcao()` e o bloco saiu de B(8) para A(2) no RADON;
- `4629f9f`: o `compose.yaml` da Aula 11 entrou em `infra/`, junto com o manual do banco e as dependências no `requirements.txt`;
- `73e525c`: a suíte foi para 23 testes, incluindo o DAO com um conector falso;
- `b50847c`: o `.pylintrc` passou a dizer `py-version=3.15`, que é a versão que realmente roda aqui;
- `ac055fd`, `3b80a72`, `c440534`, `2f152d9`: documentação, PDF e uma correção de acentos que tinha saído toda torta.

## 20/11 — conferindo com o enunciado e com os slides

Hoje li o enunciado final com calma e reli os PDFs das Aulas 1 a 12. Achei três coisas que faltavam ou que estavam mal explicadas.

A primeira era o checklist preenchido da Aula 6. O modelo `documentos/checklist-inspecao.md` já existia, mas o formulário com os achados estava só no repositório paralelo. Copiei para `checklist-inspecao-preenchido-aula6.md`. Quase fiz besteira de copiar por cima do modelo — só percebi porque o `git diff` mostrou mais linhas apagadas do que eu esperava. Recuperei o original com `git checkout` e deixei os dois arquivos.

A segunda era `tests/test_pessoa.py`. A Aula 8 mostrava essa pasta e esse arquivo na estrutura proposta. Escrevi quatro testes bem simples de getters e setters e a suíte foi para 27.

A terceira era aquele nome estranho nos commits da máquina do laboratório: `L16-M01 <l16-m01@laboratorio.local>`. Coloquei um `.mailmap` e liguei `git config log.mailmap true`. Agora `git log` mostra Cler Andrade no lugar dele.

Também criei a tag `v1.0.0-entrega` para marcar o ponto de entrega, e deixei tudo isso registrado em `documentos/auditoria-final.md`.

## 21/11 — esta capa e o texto do relatório

Você falou que o relatório não parecia feito por aluno. Tem razão. Eu tinha escrito demais como se estivesse preenchendo um formulário de avaliação. Reescrevi tudo outra vez, agora como diário: o que eu fiz, por que fiz e onde errei. A capa também entrou hoje, seguindo o modelo da UTFPR (instituição, campus, curso, título, autor, disciplina, professor e local/ano), com os dados que aparecem nos slides: COM1024, Ciência da Computação, professor Juliano Rodrigo Lamb, oferta 2026/2.

## Os slides

Os slides bateram com o que já tinha no repositório, com alguns reforços. Aula 4 e 5 eram RADON — está em `metricas-radon.md`. Aula 6 era Pylint — está no `checklist-pylint.md` e no formulário preenchido que trouxe hoje. Aula 8 queria PyTest e o teste da entidade — agora existe. Aula 9 e 10 falavam de itens de configuração, baseline, fork e Pull Request — além dos PRs, tem a tag. Aula 11 e 12 eram MySQL, réplica e DAO — estão em `infra/` e em `src/repositorio_pessoas_mysql.py`. Os exercícios de Selenium ficaram de fora, como o próprio enunciado final permite.

## O que me deu trabalho

O README estava errado. Mandava `python cadastro.py`, mas o arquivo sempre foi `src/main.py`. Corrigi e aproveitei para colocar os comandos de ambiente, banco e verificação.

O CONTRIBUTING mandava clonar o repositório do professor. Troquei pelo fluxo que usamos de verdade: branch, commit, push, PR e os quatro Pull Requests da atividade.

A função `alterar()` mudava o objeto na mão: buscava a pessoa e chamava os setters nela. Agora monto uma `Pessoa` nova e chamo `repositorio.alterar()`. O teste `test_alterar_delega_ao_repositorio` cobre essa delegação. Sem essa separação, trocar memória por MySQL ia obrigar a reescrever a regra de negócio.

O Pylint dava 9,83 porque quatro regras estavam desligadas no `.pylintrc` (`invalid-name`, `missing-function-docstring`, `missing-class-docstring` e `trailing-whitespace`). Tirei as exceções, renomeei os métodos e escrevi as docstrings. Subiu para 10,00. O antes e depois está no checklist.

O RADON apontava um bloco B no `executar()`. A média do projeto caiu de 1,85 para 1,80 e não sobrou nenhum bloco B ou C em `src/`.

O pre-commit só chamava o Pylint, e com o Python do sistema, que não tem as dependências do projeto. Apontei os três hooks para `.venv/Scripts/python.exe` e incluí pytest e RADON.

Os acentos corrompidos foram por causa do PowerShell 5.1: ele leu meus `.ps1` sem BOM como ANSI e o PDF saiu com letras erradas. Corrigi os arquivos de `cp1252` para `utf-8` e passei a salvar os scripts novos com BOM.

O Docker não cooperou. `docker info` falhou em conectar no pipe do Linux, então não subi os contêineres. Validei o compose com `docker compose config --quiet` (saída 0) e testei o DAO com um conector falso. Não vou fingir que o banco rodou de ponta a ponta.

## Como repetir o que eu fiz

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

Para usar o MySQL, entre em `infra`, rode `docker compose up -d`, crie a tabela conforme `infra/README.md` e volte para a raiz:

```powershell
$env:CADASTRO_REPOSITORIO = "mysql"
$env:DB_HOST = "localhost"
$env:DB_PORT = "3307"
$env:DB_USER = "root"
$env:DB_PASSWORD = "root_lab_2026"
$env:DB_NAME = "cadastro"
python src\main.py
```

A senha é a mesma do compose didático. Só para conferir o arquivo sem subir contêiner: `Set-Location infra`, `docker compose config --quiet`.

Na última rodada deu isso:

```
python -m pytest -q           -> 27 passed
python -m pylint src          -> 10.00/10
python -m radon cc src -a     -> 49 blocos, média A (1,80)
git status --short --branch   -> ## main...origin/main
docker compose config --quiet -> código de saída 0
```

## Autoria

Três commits de 14/10 e 17/11 saíram com `L16-M01` porque era a identidade configurada na máquina do laboratório. O `.mailmap` agora faz o Git mostrar Cler Andrade:

```
Cler Andrade <115158502+ClerAndrade@users.noreply.github.com> L16-M01 <l16-m01@laboratorio.local>
```

Não reescrevi os objetos desses commits. Eles sustentam os PRs já mesclados e mudar os hashes quebraria essa evidência. Os commits do professor continuam com o nome dele, porque são o ponto de partida permitido, e o do colega continua com o nome dele, porque é a prova da colaboração. Todo commit que fiz de 19/11 para cá sai como Cler Andrade.

Os PRs são estes:

- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/1
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/2
- https://github.com/ClerAndrade/gqs-cadatro-pessoas/pull/3
- https://github.com/So1d/gqs-cadatro-pessoas/pull/1

## O que ainda não fechei

O requisito das 17 semanas. Meu histórico começa em 14/10, e os commits anteriores são do professor. Não inventei data antiga nem commit vazio para completar o quadro; deixei isso claro em `plano-semanal.md` e `rastreabilidade.md`. O teste com MySQL rodando também ficou para quando o Docker subir.

Fora isso, o repositório está limpo, a `main` está igual à do GitHub e a tag `v1.0.0-entrega` marca a versão entregue.
