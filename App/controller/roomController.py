from App.model.roomModel import Room

class RoomController:

    @classmethod
    def listRooms(cls):
        room = Room.getAll()
        if room is None:
            return ("Nao foi possivel acessar essa sala!")
        return room
    
    @classmethod
    def getStatus(cls, id):
        if not id:
            return "Erro em obter id! adicione um id valido."
        activate = Room.status(id)
        statusText = "Ativa" if activate  else "Inativa"
        return statusText
    
    @classmethod
    def activatedRoom(cls, roomId):
            activate = Room.setAlwaysActive(roomId)
            if not activate:
                print ("Sala Ja esta Ativada!")
            else:
                print ("Sala Ativada!")
                return True
            
    @classmethod
    def disabledRoom(cls, room_id):
        disabled = Room.deactivateRoom(room_id)
        
        if disabled:
            print("Sala desativada com sucesso!")
            return True
        else:
            raise ValueError("Não foi possível desativar. A sala não foi encontrada!")

    @classmethod
    def getRoomById(cls, id):
        if not id:
            return "Erro: adicione um id correto!"
        room = Room.getById(id)
        if not room:
            return "Não foi encontrada essa sala!"
        return {f"Turma encontrada: {room} "}
    
    @classmethod       
    def updateRoomClass(cls, id, newRoom):
        if not newRoom:
            return "Erro: O nome da turma não pode ser vazio."
        sucesso = Room.updateRoom(newRoom, id)
        if sucesso:
            return f"Sala {id} atualizada com sucesso para as turmas: '{newRoom}'"
        raise TypeError("Erro em Atualizar!")
    
    @classmethod
    def createRoom(cls, turma, data):
        if not turma: 
            return "Erro: Não é possivel criar sem a turma!"
        sucess = Room.createRoom(turma, data)
        if sucess:
            return f"Nova turma adicionada com sucesso: '{turma}' na data de '{data}'."
        return False
    
    @classmethod
    def deleteRoom(cls, id):
        if not id:
            print ("Não foi possivel deletar sem o id!")
        delete = Room.deleteRoom(id)
        if delete == delete:
            return f"Sala deletada!"
        raise TypeError("Erro ao deletar!")
    


if __name__ == "__main__":

    #Create
    controller = RoomController
    sala = [
        "1º Ano D",
        "2026-02-15"
    ]

    # print(controller.createRoom(sala[0], sala[1]))
    # print(controller.disabledRoom(2))
    # print(controller.activatedRoom(2))



