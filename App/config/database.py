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
        self.database= getenv("DB_NAME")
    
    def connect(self):
        try:
            
            conn = mysql.connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database= self.database,
                use_pure = True
            )
            return conn
        except Exception as e:
            print(f'Error conexão: {e}')
            raise RuntimeError

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

    def execute(self , sql , params=None):
        """Executa INSERT/UPDATE/DELETE"""
        with self.getCursor() as (_ , cursor):
            cursor.execute(sql, params)
            return cursor.rowcount
        
    def insert(self , sql , params=None):
        with self.getCursor() as (_ , cursor):
            cursor.execute(sql, params)
            return cursor.lastrowid
        
    def fetchOne(self, sql , params=None):
        with self.getCursor() as (_ , cursor):
            cursor.execute(sql, params)
            return cursor.fetchone()
    
    def fetchAll(self, sql , params=None):
        with self.getCursor() as (_ , cursor):
            cursor.execute(sql, params)
            return cursor.fetchall()
    

if __name__ == "__main__":
    db = Database()
    resultado = db.fetchAll("SELECT * FROM alunos")
    print(resultado)