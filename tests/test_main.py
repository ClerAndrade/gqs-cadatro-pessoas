"""Testes da escolha de repositorio e do despacho do menu."""

import main
from repositorio_pessoas_memoria import RepositorioPessoasMemoria
from repositorio_pessoas_mysql import RepositorioPessoasMySQL


def test_criar_repositorio_padrao(monkeypatch):
    """Sem variavel de ambiente, usa memoria."""
    monkeypatch.delenv("CADASTRO_REPOSITORIO", raising=False)
    assert isinstance(main.criar_repositorio(), RepositorioPessoasMemoria)


def test_criar_repositorio_mysql(monkeypatch):
    """Com CADASTRO_REPOSITORIO=mysql, usa o DAO MySQL."""
    monkeypatch.setenv("CADASTRO_REPOSITORIO", "mysql")
    monkeypatch.setenv("DB_PASSWORD", "senha-teste")
    assert isinstance(main.criar_repositorio(), RepositorioPessoasMySQL)


def test_criar_repositorio_desconhecido(monkeypatch, capsys):
    """Valor desconhecido cai em memoria e avisa no terminal."""
    monkeypatch.setenv("CADASTRO_REPOSITORIO", "outra")
    repositorio = main.criar_repositorio()
    saida = capsys.readouterr().out

    assert isinstance(repositorio, RepositorioPessoasMemoria)
    assert "desconhecido" in saida


def test_processar_opcao_invalida(capsys):
    """Opcao fora do menu apenas avisa."""
    cadastro = main.CadastroPessoas()
    continuar = main.processar_opcao(cadastro, 99)

    assert continuar is True
    assert "Opcao invalida" in capsys.readouterr().out


def test_processar_opcao_sair(capsys):
    """A opcao 6 encerra o laco do menu."""
    cadastro = main.CadastroPessoas()
    continuar = main.processar_opcao(cadastro, 6)

    assert continuar is False
    assert "Saindo..." in capsys.readouterr().out
