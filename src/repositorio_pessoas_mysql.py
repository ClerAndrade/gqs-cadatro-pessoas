"""Persistencia de pessoas em MySQL."""

import os
from typing import List, Optional

import mysql.connector
from mysql.connector.constants import ClientFlag

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMySQL(RepositorioPessoas):
    """Persiste pessoas na tabela pessoa do MySQL principal."""

    def __init__(self, config):
        """Recebe a configuracao de conexao ja montada."""
        self._config = dict(config)
        self._config["client_flags"] = [ClientFlag.FOUND_ROWS]

    @classmethod
    def a_partir_do_ambiente(cls):
        """Le host, porta, usuario, senha e banco das variaveis de ambiente."""
        senha = os.environ.get("DB_PASSWORD")
        if not senha:
            raise ValueError("Defina DB_PASSWORD antes de usar o MySQL")

        config = {
            "host": os.environ.get("DB_HOST", "localhost"),
            "port": int(os.environ.get("DB_PORT", "3307")),
            "user": os.environ.get("DB_USER", "root"),
            "password": senha,
            "database": os.environ.get("DB_NAME", "cadastro"),
        }
        return cls(config)

    def _conectar(self):
        """Abre uma nova conexao com o MySQL principal."""
        return mysql.connector.connect(**self._config)

    def _executar(self, sql, valores):
        """Executa INSERT/UPDATE em transacao e devolve linhas afetadas."""
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(sql, valores)
                conexao.commit()
                return cursor.rowcount
            finally:
                cursor.close()
        except mysql.connector.Error:
            conexao.rollback()
            raise
        finally:
            conexao.close()

    def _consultar(self, sql, valores=()):
        """Executa um SELECT e devolve todas as linhas."""
        conexao = self._conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(sql, valores)
                return cursor.fetchall()
            finally:
                cursor.close()
        finally:
            conexao.close()

    def cadastrar(self, pessoa: Pessoa) -> None:
        """Insere uma pessoa na tabela pessoa."""
        sql = "INSERT INTO pessoa (nome, idade, email) VALUES (%s, %s, %s)"
        valores = (pessoa.get_nome(), pessoa.get_idade(), pessoa.get_email())
        self._executar(sql, valores)

    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca a primeira pessoa com o nome informado."""
        sql = (
            "SELECT nome, idade, email FROM pessoa "
            "WHERE nome = %s ORDER BY id LIMIT 1"
        )
        linhas = self._consultar(sql, (nome,))
        return self._para_pessoa(linhas[0]) if linhas else None

    def listar(self) -> List[Pessoa]:
        """Lista todas as pessoas do banco em ordem de id."""
        sql = "SELECT nome, idade, email FROM pessoa ORDER BY id"
        linhas = self._consultar(sql)
        return [self._para_pessoa(linha) for linha in linhas]

    @staticmethod
    def _para_pessoa(linha) -> Pessoa:
        """Converte uma linha do banco em objeto Pessoa."""
        nome, idade, email = linha
        return Pessoa(nome, idade, email)

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Atualiza a pessoa encontrada pelo nome."""
        sql = (
            "UPDATE pessoa SET nome = %s, idade = %s, email = %s "
            "WHERE nome = %s"
        )
        valores = (
            nova_pessoa.get_nome(),
            nova_pessoa.get_idade(),
            nova_pessoa.get_email(),
            nome,
        )
        return self._executar(sql, valores) > 0
