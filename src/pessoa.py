"""Entidade que representa uma pessoa no cadastro."""


class Pessoa:
    """Guarda os dados basicos de uma pessoa cadastrada."""

    def __init__(self, nome, idade, email):
        """Inicializa a pessoa com nome, idade e e-mail."""
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def get_nome(self):
        """Retorna o nome da pessoa."""
        return self.__nome

    def get_idade(self):
        """Retorna a idade da pessoa."""
        return self.__idade

    def get_email(self):
        """Retorna o e-mail da pessoa."""
        return self.__email

    def set_nome(self, nome):
        """Atualiza o nome da pessoa."""
        self.__nome = nome

    def set_idade(self, idade):
        """Atualiza a idade da pessoa."""
        self.__idade = idade

    def set_email(self, email):
        """Atualiza o e-mail da pessoa."""
        self.__email = email
