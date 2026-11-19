"""Testes do DAO MySQL com um conector falso, sem servidor de banco."""

import pytest

from pessoa import Pessoa
from repositorio_pessoas_mysql import RepositorioPessoasMySQL


class CursorFalso:
    """Simula o cursor do mysql-connector."""

    def __init__(self):
        self.linhas = []
        self.rowcount = 0
        self.sql = ""
        self.valores = ()

    def execute(self, sql, valores=()):
        """Guarda o comando e devolve linhas para SELECT."""
        self.sql = sql
        self.valores = valores
        if sql.startswith("SELECT"):
            self.linhas = [("Ana", 20, "ana@example.com")]
        else:
            self.rowcount = 1

    def fetchall(self):
        """Devolve as linhas do ultimo SELECT."""
        return self.linhas

    def close(self):
        """Fecha o cursor falso."""
        return None


class ConexaoFalsa:
    """Simula os metodos usados pela conexao com o banco."""

    def __init__(self, cursor):
        self._cursor = cursor
        self.commits = 0
        self.rollbacks = 0
        self.fechada = False

    def cursor(self):
        """Devolve o cursor falso."""
        return self._cursor

    def commit(self):
        """Conta os commits."""
        self.commits += 1

    def rollback(self):
        """Conta os rollbacks."""
        self.rollbacks += 1

    def close(self):
        """Marca a conexao como fechada."""
        self.fechada = True


@pytest.fixture
def conexao(monkeypatch):
    """Substitui mysql.connector.connect por uma conexao falsa."""
    cursor = CursorFalso()
    conn = ConexaoFalsa(cursor)
    monkeypatch.setattr("mysql.connector.connect", lambda **_: conn)
    return conn


def criar_repositorio():
    """Monta o DAO com configuracao fixa de teste."""
    config = {
        "host": "localhost",
        "port": 3307,
        "user": "root",
        "password": "senha-teste",
        "database": "cadastro",
    }
    return RepositorioPessoasMySQL(config)


def test_cadastrar_insere_no_banco(conexao):
    """O cadastro gera INSERT com commit."""
    criar_repositorio().cadastrar(Pessoa("Ana", 20, "ana@example.com"))
    cursor = conexao.cursor()

    assert "INSERT INTO pessoa" in cursor.sql
    assert cursor.valores == ("Ana", 20, "ana@example.com")
    assert conexao.commits == 1
    assert conexao.fechada is True


def test_buscar_retorna_pessoa(conexao):
    """O SELECT e convertido em objeto Pessoa."""
    encontrada = criar_repositorio().buscar("Ana")

    assert encontrada is not None
    assert encontrada.get_nome() == "Ana"
    assert encontrada.get_idade() == 20
    assert "WHERE nome = %s" in conexao.cursor().sql


def test_listar_retorna_pessoas(conexao):
    """A listagem devolve todas as linhas convertidas."""
    pessoas = criar_repositorio().listar()

    assert len(pessoas) == 1
    assert pessoas[0].get_email() == "ana@example.com"
    assert "ORDER BY id" in conexao.cursor().sql


def test_alterar_retorna_true(conexao):
    """O UPDATE usa FOUND_ROWS e retorna verdadeiro quando afeta linha."""
    bia = Pessoa("Bia", 31, "bia@example.com")
    assert criar_repositorio().alterar("Ana", bia) is True

    cursor = conexao.cursor()
    assert "UPDATE pessoa" in cursor.sql
    assert cursor.valores == ("Bia", 31, "bia@example.com", "Ana")


def test_a_partir_do_ambiente(monkeypatch):
    """As variaveis de ambiente montam a configuraÃ§Ã£o."""
    monkeypatch.setenv("DB_HOST", "127.0.0.1")
    monkeypatch.setenv("DB_PORT", "3307")
    monkeypatch.setenv("DB_USER", "root")
    monkeypatch.setenv("DB_PASSWORD", "senha-teste")
    monkeypatch.setenv("DB_NAME", "cadastro")

    repositorio = RepositorioPessoasMySQL.a_partir_do_ambiente()

    assert repositorio._config["host"] == "127.0.0.1"
    assert repositorio._config["port"] == 3307
    assert repositorio._config["password"] == "senha-teste"


def test_a_partir_do_ambiente_sem_senha(monkeypatch):
    """Sem DB_PASSWORD o erro e explicito."""
    monkeypatch.delenv("DB_PASSWORD", raising=False)
    with pytest.raises(ValueError, match="DB_PASSWORD"):
        RepositorioPessoasMySQL.a_partir_do_ambiente()
