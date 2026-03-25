from App.config.database import Database

class Parent:

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
        try:
            DB = Database()
            sql = "INSERT INTO responsaveis(nome, cpf) VALUES (%s, %s)"
            values = (name, cpf)
            newId = DB.insert(sql, values)
            print('Cadastrado com sucesso')
            return newId
        except Exception as e:
            print(f'Erro ao criar responsável!{e}')
            raise RuntimeError

    @classmethod
    def update(cls, parent:"Parent"):
        try:
            DB = Database()
            sql = "UPDATE responsaveis SET nome = %s, cpf = %s WHERE id = %s"
            values = (parent.name, parent.cpf, parent.id)
            updated = DB.execute(sql, values)
            print('Atualizado com sucesso!')
            return updated
        except Exception as e:
            print(f'Erro ao atualizar o responsável!{e}')
            raise RuntimeError

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*user) for user in lista]

    @classmethod
    def getAll(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM responsaveis"
            result = DB.fetchAll(sql)
            return cls._getObjectList(result)
        except Exception as e:
            print(f'Erro ao buscar os responsaveis{e}')
            raise RuntimeError
        
    @classmethod
    def getUnique(cls, id):
        try:
            DB = Database()
            sql = "SELECT * FROM responsaveis WHERE id = %s"
            params = (id,)
            result = DB.fetchOne(sql, params)
            if result: 
                return cls._getObjectList([result])[0]
            return cls()
        except Exception as e:
            print(f'Erro ao buscar os responsaveis{e}')
            raise RuntimeError

    @classmethod
    def searchLegalGuardian(cls, id):
        try:
            DB = Database()
            sql = "SELECT * FROM responsaveis WHERE id = %s AND responsavel_legal = 1"
            params = (id,)
            result = DB.fetchOne(sql, params)
            if result: 
                return cls._getObjectList([result])[0]
            return cls()
        except Exception as e:
            print(f'Erro ao buscar os responsaveis{e}')
            raise RuntimeError    

if __name__ == "__main__":
    todosResponsaveis = Parent.getAllTelephones()
    print(todosResponsaveis)
    


