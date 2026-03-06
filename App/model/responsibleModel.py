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

    @classmethod
    def create(cls, name, cpf):
            DB = Database()
            sql = "INSERT INTO responsaveis(nome, cpf) VALUES (%s, %s)"
            valores = (name, cpf)
            novo_id = DB.insert(sql, valores)
            print('Cadastrado com sucesso')
            return novo_id


        

    def update(self):
        #Atualiza o responsável
        pass

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*user) for user in lista]

    @classmethod
    def getAll(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM responsaveis"
            result = DB.fetchall(sql)
            return cls._getObjectList(result)
        except Exception as e:
            print(f'Erro ao buscar os responsaveis{e}')
            raise RuntimeError
        

    def getUnique(self):
        #Busca responsáveis individualmente
        pass

    def searchLegalGuardian(self):
        #Busca responsáveis legais
        pass
    
    @classmethod
    #def delete(cls, id):
        #DB = Database()
        #sql = "DELETE FROM responsaveis WHERE id= %s"
        #d = (id,)
        #excluse = DB.execute(sql, d)
        #return excluse

if __name__ == "__main__":
    todosResponsaveis = Responsavel.getAll()
    print(todosResponsaveis)
    Responsavel.create("Yuri Alberto", "12345678903")
    #Responsavel.delete(4)


