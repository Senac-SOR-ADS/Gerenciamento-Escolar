from App.model.roomModel import Room
from App.config.database import Database


__currentRoom = {
    "id": None,
    "turmas": "",
    "ativo": True,
    "data": ""
}
    
def __setCurrentRoom(id):
    __currentRoom["id"] = id

def listRooms():
    room = Room.getAll()
    if room is None:
        return ("Nao foi possivel acessar essa sala!")
    return room
    
def getStatus(id):
    if not id:
        return "Erro em obter id! adicione um id valido."
    activate = Room.status(id)
    statusText = "Ativa" if activate  else "Inativa"
    return statusText

def getRoomById(id):
    if not id:
        return "Erro: adicione um id correto!"
    room = Room.getById(id)
    if not room:
        return "Não foi encontrada essa sala!"
    return {f"Turma encontrada: {room} "}
        
def updateRoomClass(id, newRoom):
    if not newRoom:
        return "Erro: O nome da turma não pode ser vazio."
    sucesso = Room.updateRoom(newRoom, id)
    if sucesso:
        return f"Sala {id} atualizada com sucesso para as turmas: '{newRoom}'"
    return "Falha ao atualizar a sala."

def createRoom(turma, data):
    if not turma: 
        return "Erro: Não é possivel criar sem a turma!"
    sucess = Room.createRoom(turma, data)
    if sucess:
        return f"Nova turma adicionada com sucesso: '{turma}' na data de '{data}'."
    return False

def deleteRoom(id):
    if not id:
        print ("Não foi possivel deletar sem o id!")
    delete = Room.deleteRoom(id)
    if delete == delete:
        return f"Sala deletada!"
    return "Não foi possivel deletar a sala!"

if __name__ == "__main__":
    print(deleteRoom())





