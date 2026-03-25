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
    def pickStudentRoom(cls, turma):
        try:
            DB = Database()
            sql = "SELECT * FROM `alunos` WHERE `turma` = %s"
            result = DB.execute(sql, (turma,))
            return cls._getObjectList(result)
        
        except Exception as e:
            print(f"Erro em buscar aluno {e}")
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
            

if __name__ == "__main__":
    print("iniciando o teste...")
    #Room.updateRoom("", )
    #print(Room.showClass(1))
    #print(Room.status(1))
    
    
