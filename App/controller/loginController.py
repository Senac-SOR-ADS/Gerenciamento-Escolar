
__currentUser = {
    "id": None,
    "nome": "",
    "email": "",
    "tipo": ""
}

def isLogged():
    return __currentUser['id']

def __setCurrentUser(id):
    __currentUser['id'] = id

def validateLogin(email, senha):
    if email == "usuario" and senha == "123":
        __setCurrentUser(1)
        return True
    return False

def logout():
    __setCurrentUser(None)