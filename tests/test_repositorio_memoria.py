"""Testes do repositorio em memoria."""

from pessoa import Pessoa
from repositorio_pessoas_memoria import RepositorioPessoasMemoria


def test_cadastrar_e_buscar():
    """A pessoa cadastrada pode ser encontrada pelo nome."""
    repositorio = RepositorioPessoasMemoria()
    ana = Pessoa("Ana", 20, "ana@example.com")
    repositorio.cadastrar(ana)

    assert repositorio.buscar("Ana") is ana
    assert repositorio.buscar("Bia") is None


def test_listar_devolve_copia():
    """A lista interna nao vaza para quem chama listar."""
    repositorio = RepositorioPessoasMemoria()
    repositorio.cadastrar(Pessoa("Ana", 20, "ana@example.com"))

    copia = repositorio.listar()
    copia.clear()

    assert len(repositorio.listar()) == 1


def test_alterar_encontrado():
    """A pessoa encontrada e substituida."""
    repositorio = RepositorioPessoasMemoria()
    repositorio.cadastrar(Pessoa("Ana", 20, "ana@example.com"))
    bia = Pessoa("Bia", 31, "bia@example.com")

    assert repositorio.alterar("Ana", bia) is True
    assert repositorio.buscar("Ana") is None
    assert repositorio.buscar("Bia") is bia


def test_alterar_nao_encontrado():
    """Nada e alterado quando o nome nao existe."""
    repositorio = RepositorioPessoasMemoria()
    bia = Pessoa("Bia", 31, "bia@example.com")
    assert repositorio.alterar("Ana", bia) is False
