from App.config.database import Database

class Address:

    id = None
    city = ""
    neighborhood = ""
    street = ""
    complement = ""
    cep = None
    responsible_id = None
    number = None

    def __init__(self, id=None, city="", neighborhood="", street="", complement="", cep=None, responsible_id=None, number=None ):
        self.id = id
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.complement = complement
        self.cep = cep 
        self.responsible_id = responsible_id
        self.number = number

    @classmethod
    def createAddress(cls, address):
        # INSERIR NOVO ENDEREÇO EM UM ID DE RESPONSAVEL VALIDO
        try:
            DB = Database()

            sql = """
                INSERT INTO enderecos
                (cidade, bairro, rua, complemento, CEP, responsavel_id, numero)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            params = (
                address.city,
                address.neighborhood,
                address.street,
                address.complement,
                address.cep,
                address.responsible_id,
                address.number
            )

            DB.insert(sql, params)

            return address

        except Exception as e:
            print("Não foi possível inserir:", e)
            raise RuntimeError("Falha ao inserir endereço!") from e

    @classmethod
    def updateAddress(cls, address):

        try:
            DB = Database()
            sql = """
            UPDATE enderecos
            SET cidade = %s,
                bairro = %s,
                rua = %s,
                complemento = %s,
                CEP = %s
            WHERE responsavel_id = %s
            """

            params = (
                address.city,
                address.neighborhood,
                address.street,
                address.complement,
                address.cep,
                address.responsible_id
            )

            DB.execute(sql, params)

            print("Atualização feita!")

            return address
        
        except Exception as e:
            print("Não foi possível atualizar:", e)
            raise RuntimeError("Falha ao atualizar o endereço!") from e
    
    @classmethod
    def readAddress(cls, responsible_id):
        # CONSULTAR ENDEREÇO ATRAVÉS DO RESPONSAVEL
        try:
            DB = Database()
            sql = """SELECT id, cidade, bairro, rua, complemento, CEP, numero
                FROM enderecos
                WHERE responsavel_id = %s;
                """
            params = (responsible_id,)
            result = DB.fetchAll(sql, params)
            result1 = cls._getObjectList(result)
            return result1
            

        except Exception as e:
            print("Não foi possível selecionar:", e)
            print("Causa:", e.__cause__)  # <-- adiciona isso
            raise RuntimeError("Falha ao selecionar o endereço!") from e


    @classmethod
    def deleteAddress(cls, address):
        #DELETAR ENDEREÇO PELO ID DO RESPONSAVEL

        try:
            DB = Database()
            sql = """DELETE
                FROM enderecos
                WHERE responsavel_id = %s"""
            params = (address.responsible_id,)
            DB.execute(sql, params)

            print("Endereço excluido com sucesso!")
            return address

        except Exception as e:
            print("Não foi possivel deletar endereço! ", e)
            raise RuntimeError("Falha ao excluir endereço!") from e
        

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*user.values()) for user in lista]
    
    @classmethod
    def responsibleforAddress(cls, address):
        # buscar responsavel pelo endereço

        try:
            DB = Database()

            sql = """SELECT responsavel_id
                FROM enderecos
                WHERE id = %s;
                """
            params = (address.id,)
            result = DB.fetchOne(sql, params)

        except Exception as e:
            print("Não foi possivel encontrar responsável!", e)
            raise RuntimeError("Falha na procura!") from e

if __name__ == "__main__": 
    # a = Address(cep= "1832393",
    #     city= "linguiça",
    #     neighborhood= "Fora",
    #     street= "paulo guedes",
    #     complement= "dentro",
    #     number= "69",
    #     responsible_id= 4)
    

    # c = Address.createAddress(a)

    # print(c)
        
    a = Address.readAddress(1)
    print(a)
