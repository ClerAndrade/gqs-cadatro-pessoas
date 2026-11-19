"""Regras de negocio do cadastro de pessoas."""

from typing import List, Optional

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas
from repositorio_pessoas_memoria import RepositorioPessoasMemoria


class CadastroPessoas:
    """Gerencia as operacoes de cadastro de pessoas."""

    def __init__(self, repositorio: Optional[RepositorioPessoas] = None) -> None:
        """Usa o repositorio informado ou cria um em memoria."""
        self.__repositorio = repositorio or RepositorioPessoasMemoria()

    def cadastrar(self, nome, idade, email):
        """Cria a pessoa e delega a persistencia ao repositorio."""
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa

    def buscar_por_nome(self, nome):
        """Busca uma pessoa pelo nome no repositorio."""
        return self.__repositorio.buscar(nome)

    def listar(self) -> List[Pessoa]:
        """Lista as pessoas cadastradas."""
        return self.__repositorio.listar()

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Altera os dados delegando a escrita ao repositorio."""
        if self.__repositorio.buscar(nome) is None:
            return None

        nova_pessoa = Pessoa(novo_nome, nova_idade, novo_email)
        if self.__repositorio.alterar(nome, nova_pessoa):
            return nova_pessoa
        return None
