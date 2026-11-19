"""Repositorio em memoria, usado quando nao ha banco configurado."""

from typing import List, Optional

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMemoria(RepositorioPessoas):
    """Guarda as pessoas em uma lista durante a execucao."""

    def __init__(self) -> None:
        """Cria a lista vazia."""
        self.__pessoas: List[Pessoa] = []

    def cadastrar(self, pessoa: Pessoa) -> None:
        """Adiciona a pessoa ao fim da lista."""
        self.__pessoas.append(pessoa)

    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Retorna a primeira pessoa com o nome informado."""
        for pessoa in self.__pessoas:
            if pessoa.get_nome() == nome:
                return pessoa
        return None

    def listar(self) -> List[Pessoa]:
        """Devolve uma copia da lista para nao expor o estado interno."""
        return list(self.__pessoas)

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Substitui a pessoa encontrada e informa se encontrou."""
        for indice, pessoa in enumerate(self.__pessoas):
            if pessoa.get_nome() == nome:
                self.__pessoas[indice] = nova_pessoa
                return True
        return False
