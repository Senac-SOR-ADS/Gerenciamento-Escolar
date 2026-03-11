from App.config.database import Database

class Room:
    id = None
    turmas = ""
    ativo = True

    def __init__(self, id=None, turmas="", ativo=False):
        self.id = id
        self.turmas = turmas
        self.ativo = bool(ativo)

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*user) for user in lista]

    @classmethod
    def status(cls, id_status):
        try:
            DB = Database()
            sql = "SELECT `ativo` FROM salas WHERE id = %s"
            params = (id_status,)
            result = DB.fetchone(sql, params)
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
    def pickStudentRoom(cls):
        "Procurar aluno pela sala de aula que frequenta"
        pass
    
    @classmethod
    def showRoom(cls):
        try:
            DB = Database()
            sql = "SELECT `turmas` FROM salas"
            result = DB.fetchall(sql)
            return result
        except Exception as e:
            print(f"Erro ao acessar as turmas {e} !")

   
    @classmethod
    def updateRoom(cls, room: Room):
        try:
            DB = Database()
            sql = "UPDATE salas SET `turmas` = %s WHERE id = %s"
            params = (room.turmas, room.id_sala)
            DB.execute(sql, params)
            return True
        
        except Exception as e:
            print(f"Erro ao atualizar a sala: {e}") 
            return False
        
    @classmethod
    def getAll(cls):
        try:
            DB = Database()
            sql = "SELECT `id`, `turmas`, `ativo` FROM salas"
            result = DB.fetchall(sql)
            return result
        except Exception as e:
            print(f"Erro ao acessar as salas {e} !")
            

if __name__ == "__main__":
    print("Iniciando o teste...")
    
    roomUpdate = Room(id_sala=2, turmas="2º Ano B") 
    print(Room.updateRoom(roomUpdate))

    
