from App.config.database import Database

class Adress:

    id = None
    city = ""
    neighborhood = ""
    street = ""
    complement = ""
    responsible_id = None

    def __init__(self, id=None, city="", neighborhood="", street="", complement="", responsible_id=None ):
        
        self.id = id
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.complement = complement
        self.responsible_id = responsible_id

    def create(self):
        # INSERIR NOVO ENDEREÇO
        pass

    def update(self):
        #ATUALIZAR ENDEREÇO
        pass

    def read(self):
        # CONSULTAR ENDEREÇO
        DB = Database()
        sql = "SELECT * FROM enderecos"
        result = DB.fetchall(sql)
        return result

    def delete(self):
        #DELETAR ENDEREÇO
        pass

    def adressforResponsible(self, responsible):
        #CONSULTAR ENDEREÇO PELO RESPONSAVEL
        pass

    def adressforStudent(self, student):
        #CONSULTAR ENDEREÇO PELO ALUNO
        pass


if __name__ == "__main__":
    address = Adress()
    listar = address.read()
    print(listar)