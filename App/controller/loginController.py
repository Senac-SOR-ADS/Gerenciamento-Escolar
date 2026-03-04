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
    __currentUser['id'] = id
    pass

def validateLogin(email, password):
    user = Usuario.login(email)
    # user.showInfo()
    resultSenha = Criptografia.compararSenha(password, user.senha)
    if user.id and user.email == email and resultSenha:
        __setCurrentUser(user.id)
        return True
    
    return False