from App.config.database import Database
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
 
def validateLogin(email , password):
    user = Usuario.login(email)
    user.showInfo()
    result_senha = Criptografia.compararSenha(password , user.senha)
    if user.id and user.email == email and result_senha:
        __setCurrentUser(user.id)
        return True
    #if not result:
    #    return False
    #if email == result[0] and password == result[1]:
    #    __setCurrentUser(1)
    #    return True
    return False
 
 
 