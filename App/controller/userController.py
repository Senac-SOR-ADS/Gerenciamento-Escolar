from App.model.userModel import Usuario
from App.utils.validators import EmailValidator
from App.utils.criptografia import Criptografia
import re

class UserController:
    # id = None
    # name = ""
    # email = ""
    # password = ""
    # type = ""
    # user = None
    # active = False

    # def __init__(self , id=None , name="" , email="" , password="" , type="" , active=False , user=None):
    #     self.id = id 
    #     self.name = name
    #     self.email = email
    #     self.password = password 
    #     self.type = type
    #     self.active = active
    #     self.user = user


    @classmethod
    def isValidEmail(cls, email):
        valid = EmailValidator.is_valid_email(email)
        return valid

    @classmethod
    def isValidPassword(cls, password):
       if len(password) < 8 or not re.search(r'[A-Z]' , password):
          print("Sua senha deve ter pelo menos 8 caracteres e pelo menos uma letra maiúscula")
          return False
       return True

    @classmethod
    def createUser(cls, user:any):
        try:
            user:Usuario = Usuario(name=user["name"] , email=user["email"] , password=user["password"] , type=user["type"])
            if not user.name or not user.type:
                print(f'E necessario preencher todos os dados')
                return False

            if not cls.isValidEmail(user.email):
                print(f'Email não foi preenchido corretamente!')
                return False
            
            if not cls.isValidPassword(user.password):
                print(f'Senha não foi preenchida corretamente!')
                return False
            user.password = Criptografia.gerarHash(user.password)
            Usuario.createUser(user)

        except Exception as e:
            print(f'Erro ao tentar a criação de usuario {e}')
            raise RuntimeError

if __name__ == "__main__":
    usuario = {
        "name" : "chico ramos",
        "email" : "chico1@gmail.com",
        "password" : "12312244Q",
        "type" : "adm"
    }
    UserController.createUser(usuario)