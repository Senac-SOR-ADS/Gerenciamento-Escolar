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

def logout():
    __setCurrentUser(None)

def __setCurrentUser(id):
    __currentUser["id"] = id

def validateLogin(email, password):
    user = Usuario.login(email)
    user.showInfo()

    result_senha = Criptografia.compararSenha(password, user.senha)

    if user.id and email == user.email and result_senha:
        __setCurrentUser(user.id)
        return True
    
    return False
