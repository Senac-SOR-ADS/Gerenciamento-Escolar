from App.config.database import Database

class Usuario:
    

    def __init__(self , id=None , name="" , email="" , password="" , type="" , active=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.type = type 
        self.active = bool(active)

    @classmethod
    def createUser(cls , name , email , password , type):
        try:
            DB = Database()
            sql = "INSERT INTO usuarios (nome_user , email , senha , tipo_user) VALUES(%s , %s , %s , %s)"
            params = (name , email , password , type)
            result = DB.execute(sql  , params)
            return result
        except Exception as e:
            print(f'Erro na criação do usuario {e}')
            raise RuntimeError

    @classmethod
    def updateUser(cls ,id , name , email , password):
        try:
            DB = Database()
            sql = "UPDATE usuarios SET nome_user = %s , email = %s , senha = %s WHERE id = %s"
            params = (name , email , password , id)
            result = DB.execute(sql , params)
            return result
        except Exception as e:
            print(f'Não foi possivel atualizar os dados do usuario {e}')
            raise RuntimeError
        
    @classmethod
    def deleteUser(cls, id):
        try:
            DB = Database()
            sql = "UPDATE usuarios SET ativo = 0 WHERE id = %s"
            params = (id , )
            result = DB.execute(sql, params)
            return result
        except Exception as e:
            print(f'Erro ao tentar desativar o usuario {e}')
            raise RuntimeError
        
    @classmethod
    def findById(cls, id):
        try:
            DB = Database()
            sql = "SELECT * FROM usuarios WHERE id = %s"
            params = (id,)
            result = DB.fetchOne(sql , params)
            if not result:
                return None
            return cls(*result)
            
        except Exception as e:
            print(f'Erro ao encontrar usuario por id {e}')
            raise RuntimeError

    @classmethod
    def findAll(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM usuarios"
            result = DB.fetchAll(sql)
            usuarios = [cls(*row) for row in result]
            return usuarios
        except Exception as e:
            print(f'Erro ao buscar todos os usuarios {e}')
            raise RuntimeError
            

    @classmethod
    def findUserActive(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM usuarios WHERE ativo = 1"
            result = DB.fetchAll(sql)
            usuarios = [cls(*row) for row in result]
            return usuarios
        except Exception as e:
            print(f'Erro ao listar usuarios ativos {e}')
            raise RuntimeError

    @classmethod
    def login(cls , email):
        DB = Database()
        sql = "SELECT * FROM usuarios WHERE email = %s AND ativo = 1"
        params = (email,)
        result = DB.fetchOne(sql, params)
        if not result: return Usuario()
        user = Usuario(*result)
        return user
    
    
    def showInfo(self):
        print(f"""
        ID : {self.id}
        Nome : {self.name}
        Email: {self.email}
        Senha: {self.password}
        Tipo: {self.type}
        Ativo: {self.active}
         """)

if __name__ == "__main__":
    todosUsuarios = Usuario.findAll()
    print(todosUsuarios)