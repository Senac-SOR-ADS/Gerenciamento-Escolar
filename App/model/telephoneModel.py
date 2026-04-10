from App.config.database import Database

class Telephone:

    id = None
    telephone = ""
    responsavel_id = None

    def __init__(self, id=None, telephone = "", responsavel_id = None):
        self.id = id
        self.telephone = telephone
        self.responsavel_id = responsavel_id

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*user) for user in lista]

    @classmethod
    def create(cls, telephone, responsavel_id):
        try:
            DB = Database()
            sql = "INSERT INTO telefones(telefone, responsavel_id) VALUES (%s, %s)"
            values = (telephone, responsavel_id)
            newId = DB.insert(sql, values)
            print('Telefone cadastrado com sucesso')
            return newId
        except Exception as e:
            print(f'Erro ao cadastrar telefone!{e}')
            raise RuntimeError

    
    @classmethod
    def update(cls, telephone, id):
        try:
            DB = Database()
            sql = "UPDATE telefones SET telefone = %s WHERE id = %s"
            values = (telephone, id)
            updated = DB.execute(sql, values)
            print('Telefone atualizado com sucesso!')
            return updated
        except Exception as e:
            print(f'Erro ao atualizar o telefone!{e}')
            raise RuntimeError

    @classmethod
    def delete(cls, id_telephone):
        try:
            DB = Database()
            sql = "DELETE FROM telefones WHERE id = %s"
            values = (id_telephone, )
            deleted = DB.execute(sql, values)
            print('Telefone excluído com sucesso!')
            return deleted
        except Exception as e:
            print(f'Erro ao excluir o telefone!{e}')
            raise RuntimeError
        
    @classmethod    
    def parentTelephone(cls, responsavel_id):
        try:
            DB = Database()
            sql = "SELECT telefone FROM telefones WHERE responsavel_id = %s"
            values = (responsavel_id, )
            telephone = DB.fetchAll(sql, values)
            print(telephone)
            return cls._getObjectList(telephone)
        except Exception as e:
            print(f'Erro ao buscar os telefones do responsável!{e}')
            raise RuntimeError
        
    @classmethod
    def getAllTelephones(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM telefones"
            result = DB.fetchAll(sql)
            return cls._getObjectList(result)
        except Exception as e:
                print(f'Erro ao buscar os responsaveis{e}')
                raise RuntimeError


if __name__ == "__main__":
    telefones = Telephone.getAllTelephones()
    print(telefones)
    #todosTelefones = Telephone.parentTelephone
    #print(todosTelefones)
    #Telephone.create("(90)99834-3332", 1)
    #phone = Telephone(8)
    #phone.delete()

#SELECT telefone FROM telefones WHERE responsavel_id = %s

        
