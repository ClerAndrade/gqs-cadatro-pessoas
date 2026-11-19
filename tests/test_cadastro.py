"""Testes das operacoes de CadastroPessoas."""

from cadastro import CadastroPessoas
from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioEspiao(RepositorioPessoas):
    """Registra as chamadas para conferir a delegacao da alteracao."""

    def __init__(self):
        self.pessoa = Pessoa("Ana", 20, "ana@example.com")
        self.alteracoes = []

    def cadastrar(self, pessoa):
        self.pessoa = pessoa

    def buscar(self, nome):
        if nome == self.pessoa.get_nome():
            return self.pessoa
        return None

    def listar(self):
        return [self.pessoa]

    def alterar(self, nome, nova_pessoa):
        self.alteracoes.append((nome, nova_pessoa))
        self.pessoa = nova_pessoa
        return True


def test_cadastrar_pessoa():
    """Confere armazenamento e quantidade."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    pessoas = cadastro.listar()

    assert len(pessoas) == 1
    assert pessoas[0].get_nome() == "Ana"
    assert pessoas[0].get_idade() == 20
    assert pessoas[0].get_email() == "ana@example.com"


def test_buscar_por_nome():
    """Encontra uma pessoa ja cadastrada."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    encontrada = cadastro.buscar_por_nome("Ana")

    assert encontrada is not None
    assert encontrada.get_nome() == "Ana"
    assert encontrada.get_idade() == 20
    assert encontrada.get_email() == "ana@example.com"


def test_buscar_por_nome_nao_encontrado():
    """Retorna None quando o nome nao esta cadastrado."""
    cadastro = CadastroPessoas()
    assert cadastro.buscar_por_nome("Ana") is None


def test_listar_inicialmente_vazio():
    """A lista comeca vazia."""
    assert not CadastroPessoas().listar()


def test_cadastrar_varias_pessoas():
    """Mantem a quantidade e a ordem dos cadastros."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")
    cadastro.cadastrar("Bia", 31, "bia@example.com")

    pessoas = cadastro.listar()

    assert len(pessoas) == 2
    assert pessoas[0].get_nome() == "Ana"
    assert pessoas[1].get_nome() == "Bia"


def test_alterar_pessoa():
    """Atualiza os dados da pessoa encontrada."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    alterada = cadastro.alterar(
        "Ana", "Ana Maria", 21, "ana.maria@example.com"
    )

    assert alterada is not None
    assert alterada.get_nome() == "Ana Maria"
    assert alterada.get_idade() == 21
    assert alterada.get_email() == "ana.maria@example.com"
    assert cadastro.buscar_por_nome("Ana") is None
    assert cadastro.buscar_por_nome("Ana Maria") is alterada


def test_alterar_pessoa_inexistente():
    """Retorna None ao alterar nome nao cadastrado."""
    cadastro = CadastroPessoas()
    assert cadastro.alterar("Ana", "Bia", 30, "bia@example.com") is None


def test_alterar_delega_ao_repositorio():
    """A regra de negocio nao altera o objeto diretamente."""
    repositorio = RepositorioEspiao()
    cadastro = CadastroPessoas(repositorio)

    alterada = cadastro.alterar("Ana", "Bia", 30, "bia@example.com")

    assert alterada is repositorio.pessoa
    assert repositorio.alteracoes[0][0] == "Ana"
    assert repositorio.alteracoes[0][1].get_nome() == "Bia"
