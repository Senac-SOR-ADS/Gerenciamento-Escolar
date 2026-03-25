from App.model.userModel import Usuario
from App.utils.validators import EmailValidator
from App.utils.criptografia import Criptografia
import re


__currentUser = {
    "id": None,
    "nome": "",
    "email": "",
    "tipo": ""
}

def isLogged():
    return __currentUser['id'] != None

def logout():
    _setCurrentUser(None)

def _setCurrentUser(id):
    __currentUser["id"] = id       
            


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
                raise ValueError(f'E necessário preencher todos os dados!')

            if not cls.isValidEmail(user.email):
                print(f'Email não foi preenchido corretamente!')
                raise ValueError('Email não preenchido corretamente')
            
            if not cls.isValidPassword(user.password):
                raise ValueError("Senha não foi preenchida corretamente!")
                
            user.password = Criptografia.gerarHash(user.password)
            Usuario.createUser(user)

        except Exception as e:
            print(f'Erro ao tentar a criação de usuario {e}')
            raise RuntimeError
        
    @classmethod
    def login(cls , email , senha):
        try:
            user = Usuario.login(email)
            if not user:
                raise TypeError("Não encontramos seus dados de acesso")
            
            comparePassword = Criptografia.compararSenha(senha ,user.password)
            if not comparePassword:
                raise ValueError("Email ou senha incorretos")
            
            _setCurrentUser(user.id)
            print(f'Login efetuado com sucesso!')
            return True
            
        except Exception as e:
            print(f'Não foi possivel fazer o login \n{e}')

    @classmethod
    def deactiveUser(cls , id):
        try:
            if type(id) != int or id <= 0:
                raise ValueError("Esse id não existe!")
            Usuario.deactiveUser(id)
        except Exception as e:
            print(f'Erro ao tentar desativar usuario \n{e}')
        
    @classmethod
    def updateUser(cls , user:any):
        try:
            usuario = Usuario.findById(user["id"])
            if not usuario:
                raise ValueError("usuario não encontrado")
           
            if not cls.isValidEmail(user["email"]) or not cls.isValidPassword(user["password"]):
                raise ValueError("Não foi possivel atualizar usuario. Por favor preencha os campos corretamente!")
            
            if not Criptografia.compararSenha(user["password"] , usuario.password):
                user["password"] = Criptografia.gerarHash(user["password"])
            usuario.email = user["email"]
            usuario.password = user["password"]
            usuario.name = user["name"]
            cls.normalizedEmail(user["email"])
                          
            Usuario.updateUser(usuario)
        except Exception as e:
            print(f'Não foi possivel atualizar o usuario \n{e}')



if __name__ == "__main__":
    # print(isLogged())
    usuario = {
        "id" : 26,
        "name" : "Nelson Junior",
        "email" : "nelson@gmail.com",
        "password" : "123",
        "type" : "agente"
    }
    #UserController.login(usuario["email"] , usuario["password"])
    #print(isLogged())
    UserController.updateUser(usuario)
