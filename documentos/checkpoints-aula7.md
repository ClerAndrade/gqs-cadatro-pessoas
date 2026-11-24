# Checkpoints da Aula 7 — rastreabilidade

Os cinco checkpoints pedidos nos slides 19, 20, 22/26, 27 e 29 foram executados na linha `refactor/orientacao-objetos` e integrados em `main` pelo merge `2561c25`. Os commits abaixo são do professor e constituem o ponto de partida permitido; as mensagens e os arquivos estão conferidos no histórico do repositório.

| Checkpoint | Alteração pedida | Commit | Data |
|---|---|---|---|
| 1 — Estrutura | criar `src/` e mover `Cadastro.py` para `src/main.py` | `c379827` | 30/09/2026 |
| 2 — Pessoa | criar `src/pessoa.py` com estado privado e métodos explícitos | `6b23305` | 30/09/2026 |
| 3 — CadastroPessoas | criar `src/cadastro.py` e atualizar `main.py` | `4d5b556` | 30/09/2026 |
| 4 — Interface | separar `exibir_menu` e `executar` da regra de negócio | `fcbe0d5` | 30/09/2026 |
| 5 — Contribuição | ajustar `.gitignore`, `CONTRIBUTING.md` e orientações | `e7be830` | 30/09/2026 |

O roteiro de cada checkpoint era: conceito, alteração, código completo, execução com `python src\main.py`, inspeção com `git status` e `git diff`, `git add`, `git commit` e `git log --oneline`. A verificação final incluía cadastrar, consultar, alterar, listar, avaliar cadastro e encerrar, com a árvore limpa.

A orientação de contribuição foi atualizada outra vez em `e28c402`, em 06/10/2026. Este arquivo existe para fechar o item de rastreabilidade da Aula 7, que antes só estava implícito nos commits iniciais.
