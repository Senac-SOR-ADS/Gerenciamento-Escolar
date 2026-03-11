from App.config.database import Database

class Usuario:
    id = None
    nome = ""
    email = ""
    senha = ""
    tipo = ""
    ativo = False

    def __init__(self, id=None, nome="", email="", senha="", tipo="", ativo=False):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.ativo = bool(ativo)

<<<<<<< dev

    @classmethod
    def login(cls, email):
        DB = Database()
        sql = "SELECT * FROM usuarios WHERE email = %s;"
        params = (email,)
        result = DB.fetchone(sql, params)
        if not result: return Usuario()
        user = Usuario(*result)
        return user
    
    
    def showInfo(self):
        print(f""" 
=======
    @classmethod
    def login(cls, email):
        DB = Database()
        sql = "SELECT * FROM usuarios WHERE email = %s"
        params = (email,)
        result = DB.fetchOne(sql, params)
        if not result: return Usuario()
        user = Usuario(*result.values())
        return user 
    
    def showInfo(self):
        print(f"""  
>>>>>>> dev
            ID: {self.id}
            Nome: {self.nome}
            Email: {self.email}
            Senha: {self.senha}
            Tipo: {self.tipo}
            Ativo: {self.ativo}
<<<<<<< dev
        """)
        
=======
        """) 
>>>>>>> dev
