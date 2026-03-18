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
    
def validateStatus(id):
    if not id:
        return "Erro em obter id! adicione um id valido."
    activate = Room.status(id)
    statusText = "Ativa" if activate  else "Inativa"
    return statusText

def getAll():
    try:
        DB = Database()
        sql = "SELECT `id`, `turmas`, `ativo` FROM salas"
        result = DB.fetchAll(sql)
        return result
    except Exception as e:
        print(f"Erro ao acessar as salas {e} !")
        return None
        
def updateRoomClass(id, novaTurma):
    if not novaTurma:
        return "Erro: O nome da turma não pode ser vazio."
    sucesso = Room.updateRoom(novaTurma, id)
    if sucesso:
        return f"Sala {id} atualizada com sucesso para as turmas: '{novaTurma}'"
    return "Falha ao atualizar a sala."


if __name__ == "__main__":
    print(validateStatus(1))





