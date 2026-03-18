from App.model.userModel import Usuario
from App.utils.criptografia import Criptografia

__currentUser = {
    "id": None,
    "nome": "",
    "email": "",
    "tipo": ""
}
 
def isLogged():
    return __currentUser['id']

<<<<<<< HEAD
def __setCurrentUser(id):
    __currentUser['id'] = id

def validateLogin(email, senha):
    if email == "usuario" and senha == "123":
        __setCurrentUser(1)
        return True
    return False

def logout():
    __setCurrentUser(None)
=======
def logout():
    __setCurrentUser(None)

def __setCurrentUser(id):
    __currentUser["id"] = id

def validateLogin(email, password):
    user = Usuario.login(email)
    user.showInfo()

    result_senha = Criptografia.compararSenha(password, user.password)

    if user.id and email == user.email and result_senha:
        __setCurrentUser(user.id)
        return True
    
    return False
>>>>>>> b7f189892e76334c913ab91b2b8d123ad1f4f453
