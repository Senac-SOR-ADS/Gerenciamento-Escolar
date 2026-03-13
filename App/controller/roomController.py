from App.model.roomModel import Room


__currentRoom = {
    "id": None,
    "turmas": "",
    "ativo": True,
    "data": ""
}
    
def __setCurrentRoom(id):
    __currentRoom["id"] = id

def listarSalas():
    room = Room.getAll()
    if room == None:
        return ("Nao foi possivel acessar essa sala!")
    
@staticmethod
def validateStatus(id):
    if not str (id).isdigit():
        return ("ID: Invalido")
    activate = Room.status(id)
    statusText = "Ativa" if activate  else "Inativa"
    return statusText
        



if __name__ == "__main__":
    print(listarSalas())