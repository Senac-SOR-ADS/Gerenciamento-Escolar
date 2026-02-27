from App.model.userModel import Usuario


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

    if user.id and user.email == email and user.senha == password:
        __setCurrentUser(user.id)
        return True
    return False

