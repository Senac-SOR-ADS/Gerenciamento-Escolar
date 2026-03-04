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
    def status(cls):
        "Mostrar se a sala esta ativa ou foi desativada."
        pass

    @classmethod
    def pickStudentRoom(cls):
        "Procurar aluno pela sala de aula que frequenta"
        pass
    
    @classmethod
    def showRoom(cls):
        "Mostrar salas que existem"
        pass

    @classmethod
    def editRoom(cls):
        "Modificar salas existentes, caso alguma sala troque alguma turma"
        pass
        
    @classmethod
    def getAll(cls):
        try:
            DB = Database()
            sql = "SELECT `id`, `turmas`, `ativo` FROM salas "
            result = DB.fetchall(sql)
            return result
        except Exception as e:
            print(f"Erro ao acessar as salas {e} !")
            

if __name__ == "__main__":
    print(Room.getAll())



