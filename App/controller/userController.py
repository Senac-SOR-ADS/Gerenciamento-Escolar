from App.model.userModel import Usuario
from App.utils.validators import EmailValidator
from App.utils.criptografia import Criptografia
import re

class UserController:
    @classmethod 
    def normalizedEmail(cls , email):
        emailNormalized = email.strip().lower()
        return emailNormalized

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
            user.email = cls.normalizedEmail(user.email)
            if not user.name.strip() or not user.type.strip():
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
        
    @classmethod
    def login(cls , email , senha):
        try:
            sameEmail = Usuario.findByEmail(email)
            if not sameEmail:
                raise ValueError("Não encontramos seus dados de acesso")
            comparePassword = Criptografia.compararSenha(senha ,sameEmail.password)
            if not comparePassword:
                raise ValueError("Email ou senha incorretos")
            
            


        

if __name__ == "__main__":
    usuario = {
        "name" : "Nelson Mandela",
        "email" : " nelson@gmail.com ",
        "password" : "12312222R",
        "type" : "agente"
    }
    UserController.createUser(usuario)