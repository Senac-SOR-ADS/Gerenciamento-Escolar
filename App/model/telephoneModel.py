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


    def delete(self):
        try:
            DB = Database()
            sql = "DELETE FROM telefones WHERE id = %s"
            values = (self.id, )
            updated = DB.execute(sql, values)
            print('Telefone excluído com sucesso!')
            return updated
        except Exception as e:
            print(f'Erro ao excluir o telefone!{e}')
            raise RuntimeError

if __name__ == "__main__":
    #Telephone.create("(24)99834-3434", 1)
    phone = Telephone(8)
    phone.delete()

        
