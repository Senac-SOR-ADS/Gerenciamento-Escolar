from App.config.database import Database

class Address:

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

    @classmethod
    def createAddress(cls):
        # INSERIR NOVO ENDEREÇO EM UM ID DE RESPONSAVEL VALIDO
        try:
            DB = Database()

            sql = """
                INSERT INTO enderecos
                (cidade, bairro, rua, complemento, responsavel_id)
                VALUES (%s, %s, %s, %s, %s)
            """

            params = (
                address.city,
                address.neighborhood,
                address.street,
                address.complement,
                address.responsible_id
            )

            endereco_id = DB.insert(sql, params)

            print(f"Endereço inserido! ID: {endereco_id}")
            return endereco_id

        except Exception as e:
            print("Não foi possível inserir:", e)
            raise RuntimeError("Falha ao inserir endereço!") from e

    @classmethod
    def updateAddress(cls):

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
                address.city,
                address.neighborhood,
                address.street,
                address.complement,
                address.responsible_id
                )

            DB.execute(sql, params)
            print("Atualização feita!")
        
        except Exception as e:
            print("Não foi possível atualizar:", e)
            raise RuntimeError("Falha ao atualizar o endereço!") from e
      

        

        
        
        
    @classmethod
    def readAddress(cls):
        # CONSULTAR ENDEREÇO ATRAVÉS DO RESPONSAVEL

        try:
            DB = Database()
            sql = """SELECT cidade, bairro, rua, complemento
                FROM enderecos
                WHERE responsavel_id = %s;
                """
            params = (address.responsible_id,)
            result = DB.fetchOne(sql, params)
            
            print("Seleção feita!")
            print(result)

        except Exception as e:
            print("Não foi possível selecionar:", e)
            raise RuntimeError("Falha ao selecionar o endereço!") from e

            
        
    @classmethod
    def deleteAddress(cls):
        #DELETAR ENDEREÇO PELO ID DO RESPONSAVEL

        try:
            DB = Database()
            sql = """DELETE
                FROM enderecos
                WHERE responsavel_id = %s"""
            params = (address.responsible_id,)
            DB.execute(sql, params)

            print("Endereço excluido com sucesso!")

        except Exception as e:
            print("Não foi possivel deletar endereço! ", e)
            raise RuntimeError("Falha ao excluir endereço!") from e
        
    @classmethod
    def responsibleforAddress(cls):
        # buscar responsavel pelo endereço

        try:
            DB = Database()

            sql = """SELECT bairro, responsavel_id
                FROM enderecos
                WHERE id = %s;
                """
            params = (address.id,)
            result = DB.fetchOne(sql, params)

            print(result)

        except Exception as e:
            print("Não foi possivel encontrar responsável!", e)
            raise RuntimeError("Falha na procura!") from e
            
        


if __name__ == "__main__":
    address = Address(
        id=11,
        city="Sorocaba",
        neighborhood="Centro",
        street="Rua Teste",
        complement="Casa"
    )

    address.responsibleforAddress()