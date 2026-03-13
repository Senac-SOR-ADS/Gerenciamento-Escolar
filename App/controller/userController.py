from App.model.userModel import Usuario
from App.utils.validators import EmailValidator
import re
class UserController:
    id = None
    name = ""
    email = ""
    password = ""
    type = ""
    user = None

    active = False
    def __init__(self , id=None , name="" , email="" , password="" , type="" , active=False):
        self.id = id 
        self.name = name
        self.email = email
        self.password = password 
        self.type = type
        self.active = active


    def isValidEmail(self , email):
        valid = EmailValidator.is_valid_email(email)
        return valid

    def isValidPassword(self , password):
       if len(password) < 8 or not re.search(r'[A-Z]' , password):
          print("Sua senha deve ter pelo menos 8 caracteres e pelo menos uma letra maiúscula")
          return False
       
       return True

    @classmethod
    def createUser(cls , user:UserController):
      try:
        if not user.isValidEmail(user.email) or not user.isValidPassword(user.email):
            print(f'Email não foi preenchido corretamente!')
            return False
        
        if not user.isValidPassword(user.password):
           print(f'Senha não foi preenchida corretamente!')
           return False