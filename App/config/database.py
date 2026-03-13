import mysql.connector
from os import getenv
from dotenv import load_dotenv
from contextlib import contextmanager
from App.utils.singleton import Singleton

load_dotenv(override=True)


class Database(metaclass=Singleton):
    def __init__(self):
        self.host = getenv("DB_HOST")
        self.port = int(getenv("DB_PORT"))
        self.user = getenv("DB_USER")
        self.password = getenv("DB_PASSWORD")
        self.database = getenv("DB_NAME")
    def connect(self):
        try:
            conexao = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database,
                use_pure = True
            )
            return conexao
        except Exception as e:
            print(f"Error conexao: {e}")
            raise RuntimeError("Erro ao conectar ao banco de dados.")
        
    @contextmanager
    def getCursor(self, dictionary=True):
        conn = self.connect()
        cursor = conn.cursor(dictionary=dictionary)
        try: 
            yield conn, cursor
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            try:
                cursor.close()
            finally:
                conn.close()

    def execute(self, sql, params=None): 
        with self.getCursor() as (_, cursor):
            cursor.execute(sql, params)
            return cursor.rowcount
        
    def insert(self, sql, params=None):
        with self.getCursor() as (_, cursor):
            cursor.execute(sql, params)
            return cursor.lastrowid
        
    def fetchOne(self, sql, params=None):
        with self.getCursor() as (_, cursor):
            cursor.execute(sql, params)
            return cursor.fetchone()
        
    def fetchAll(self, sql, params=None):
        with self.getCursor() as (_, cursor):
            cursor.execute(sql, params)
            return cursor.fetchall()

if __name__ == "__main__":
    DB = Database()
    print(id(DB))
    # result = DB.fetchall("SELECT * FROM alunos")  

