import mysql.connector
from os import getenv
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv(override=True)

class Database():
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
                database = self.database
            )
            return conexao
        except Exception as e:
            print(f"Error conexao: {e}")
            raise RuntimeError("Erro ao conectar ao banco de dados.")
        
    @contextmanager
    def getCursor(self):
        conn = self.connect()
        cursor = conn.cursor()
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


cursor = conexao.cursor()
cursor.execute("SELECT * FROM usuarios")

resp = cursor.fetchall()
conexao.close()

print(resp)