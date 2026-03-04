from App.config.database import Database

class Responsavel:

    id = None
    name = ""
    cpf = ""
    legal_guardian = True

    def __init__(self, id=None, name="", cpf="", legal_guardian=True):
        self.id = id
        self.name = name
        self.cpf = cpf
        self.legal_guardian = bool(legal_guardian)

    def create(self):
        #Cadastra o responsável
        pass

    def update(self):
        #Atualiza o responsável
        pass

    @classmethod
    def getAll(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM responsaveis"
            result = DB.fetchall(sql)
            return result
        except Exception as e:
            print(f'Erro ao buscar os responsaveis{e}')
            raise RuntimeError
        

    def getUnique(self):
        #Busca responsáveis individualmente
        pass

    def searchLegalGuardian(self):
        #Busca responsáveis legais
        pass

    def delete(self):
        # "Desativa" um responsável
        pass

if __name__ == "__main__":
    todosResponsaveis = Responsavel.getAll()
    print(todosResponsaveis) 


