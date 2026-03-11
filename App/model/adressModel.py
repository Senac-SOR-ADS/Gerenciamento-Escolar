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

    @classmethod
    def update(cls):

        try:
            DB = Database()
            sql = """
            UPDATE enderecos
            SET cidade = %s,
                bairro = %s,
                rua = %s,
                complemento = %s
                WHERE responsavel_id = %s
            """

            params = (
                adress.city,
                adress.neighborhood,
                adress.street,
                adress.complement,
                adress.responsible_id
                )

            DB.execute(sql, params)
            print("Atualização feita!")
        
        except Exception as e:
            print("Não foi possível atualizar:", e)
            raise RuntimeError("Falha ao atualizar o endereço!") from e


    def updateAdress(self):

        DB = Database()
        sql = """
            UPDATE enderecos
            SET cidade = %s,
                bairro = %s,
                rua = %s,
                complemento = %s
            WHERE responsavel_id = %s
        """

        params = (
            self.city,
            self.neighborhood,
            self.street,
            self.complement,
            self.responsible_id
        )
        DB.execute(sql, params)
      

        

        
        
        

    def read(self):
        # CONSULTAR ENDEREÇO
        DB = Database()
        sql = "SELECT * FROM enderecos WHERE id = %s"
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
    adress = Adress(
        responsible_id=3,     
        city="Toquio",
        neighborhood="Bairro Nada",
        street="Rua Sushi",
        complement="Nada"
    )

    adress.update()