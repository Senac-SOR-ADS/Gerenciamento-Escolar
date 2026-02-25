
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
     if email == "usuario" and password == "123":
        __setCurrentUser(1)
        return True
     return False