from App.config.database import Database

class Usuario:
    id = None
    name = ""
    email = ""
    password = ""
    type = ""
    active = False

    def __init__(self , id=None , name="" , email="" , password="" , type="" , active=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.type = type 
        self.active = bool(active)

    @classmethod
    def createUser(cls , name , email , password , type):
        pass

    @classmethod
    def updateUser(cls , id):
        pass
    @classmethod
    def deleteUser(cls, id):
        pass
    @classmethod
    def findByUser(cls, id):
        pass
    @classmethod
    def findAllUser(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM usuarios"
            result = DB.fetchAll(sql)
            return result
        except Exception as e:
            print(f'Erro ao buscar todos os usuarios {e}')
            raise RuntimeError
            

    @classmethod
    def findUserActive(cls):
        pass

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
    todosUsuarios = Usuario.findAllUser()
    print(todosUsuarios)