from App.config.database import Database
from typing import Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Room:
    id: Optional[int] = None
    turmas: str = ""
    ativo: bool = True
    date: datetime = None
    

    def __init__(self, id=None, turmas="", ativo=False, data=""):
        self.id = id
        self.turmas = turmas
        self.ativo = bool(ativo)
        self.date = data

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*user.values()) for user in lista]

    @classmethod
    def status(cls, id):
        try:
            DB = Database()
            sql = "SELECT ativo FROM salas WHERE id = %s"
            params = (id,)
            result = DB.fetchOne(sql, params)
            if result and result[0] == 1:
                print("Sala Ativa!")
                return True
            else: 
                print("Sala Inativa!")
                return False
            
        except Exception as e:
            print(f"Erro em obter informações do {e}")
            return False      

    @classmethod
    def showClass(cls, id):
        try:
            DB = Database()
            sql = "SELECT `turmas` FROM salas WHERE id = %s"
            params = (id,)
            result = DB.fetchAll(sql, params)
            return result
        except Exception as e:
            print(f"Erro ao acessar as turmas {e} !")

    @classmethod
    def deactivateRoom(cls, roomId):
        try:
            DB = Database()
            sql = "UPDATE salas SET ativo = 0 WHERE id = %s" 
            params = (roomId,)
            result = DB.execute(sql, params)
            return result
        except Exception as e:
            raise Exception(f"Erro ao desativar sala: {e}")

    @classmethod
    def getById(cls, id):
        try:
            DB = Database()
            sql = "SELECT turmas FROM salas WHERE id = %s"
            params = (id,)
            result = DB.fetchOne(sql, params)
            return result
        except Exception as e:
            print(f"Erro ao buscar turma! {e}")
    
    @classmethod
    def createRoom(cls, turma, data):

        data = str(data)
        turma = str(turma)

        try:
            DB = Database()
            sql = "INSERT INTO `salas` (`turmas`, `data`) VALUES (%s, %s)"
            params = (turma, data)
            result = DB.insert(sql, params)
            if not result:
                return "Nao foi possivel adicionar!"
            return f"Turma {turma} adicionada com sucesso na data {data}"
        except Exception as e:
            print(f"Erro ao inserir {e}")
            return "Erro interno ao adicionar turma!"

    @classmethod
    def setAlwaysActive(cls, roomId):
        try:
            DB = Database()
            sql = "UPDATE salas SET ativo = 1 WHERE id = %s"
            params = (roomId,)
            result = DB.execute(sql, params)
            return result
        except Exception as e:
            raise Exception(f"Erro ativar a sala{e}")

    @classmethod
    def updateRoom(cls, turmas, id):
        try:
            DB = Database()
            sql = "UPDATE salas SET `turmas` = %s WHERE id = %s"
            params = (turmas, id)
            result = DB.execute(sql, params)
            if result == True:
                print("Atualizado com sucesso!")
            return True
            
        except Exception as e:
            print(f"Erro ao atualizar a sala: {e} ") 
            return False
        
    @classmethod
    def getAll(cls):
        try:
            DB = Database()
            sql = "SELECT `id`, `turmas`, `ativo` FROM salas"
            result = DB.fetchAll(sql)
            return result
        except Exception as e:
            print(f"Erro ao acessar as salas {e} !")

    @classmethod
    def deleteRoom(cls, id):
        try:
            DB = Database()
            sql = "DELETE FROM `salas` WHERE id = %s"
            params = (id,)
            result = DB.execute(sql, params)
            return result
        except Exception as e:
            print(f"Erro em deletar turma {e} ")
            
    @classmethod
    def getByYear(cls, year):
        try:
            DB = Database()
            year = year or datetime.now().year
            sql = "SELECT * FROM salas WHERE YEAR(data) = %s"
            params = (year,)
            result = DB.fetchAll(sql, params)
            # print(result)
            result = cls._getObjectList(result)
            return result
        except Exception as e:
            print(f"Erro ao obter dados {e}")


if __name__ == "__main__":
    print("iniciando o teste...")
    #Room.updateRoom("", )
    #print(Room.showClass(1))
    # print(Room.createRoom("3º Ano A - Portugues", "2027-02-05"))
    # print(Room.createRoom("3º Ano A - Portugues", "01/01/2000"))
    # print(Room.getByYear())
    # print(Room.deleteRoom(7))

    




