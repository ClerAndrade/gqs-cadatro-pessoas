"""Testes da entidade Pessoa."""

from pessoa import Pessoa


def test_criar_pessoa():
    """Guarda os dados informados."""
    pessoa = Pessoa("Ana", 20, "ana@example.com")

    assert pessoa.get_nome() == "Ana"
    assert pessoa.get_idade() == 20
    assert pessoa.get_email() == "ana@example.com"


def test_alterar_nome():
    """O nome pode ser atualizado."""
    pessoa = Pessoa("Ana", 20, "ana@example.com")
    pessoa.set_nome("Ana Maria")

    assert pessoa.get_nome() == "Ana Maria"


def test_alterar_idade():
    """A idade pode ser atualizada."""
    pessoa = Pessoa("Ana", 20, "ana@example.com")
    pessoa.set_idade(21)

    assert pessoa.get_idade() == 21


def test_alterar_email():
    """O e-mail pode ser atualizado."""
    pessoa = Pessoa("Ana", 20, "ana@example.com")
    pessoa.set_email("ana.maria@example.com")

    assert pessoa.get_email() == "ana.maria@example.com"
