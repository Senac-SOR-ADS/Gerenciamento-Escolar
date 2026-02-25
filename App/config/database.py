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
                database= self.database
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



cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
resp = cursor.fetchall()
conn.close()

print(resp)