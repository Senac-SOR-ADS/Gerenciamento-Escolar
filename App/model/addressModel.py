from App.config.database import Database

class Address:

    id = None
    city = ""
    neighborhood = ""
    street = ""
    complement = ""
    cep = None
    responsible_id = None

    def __init__(self, id=None, city="", neighborhood="", street="", complement="", cep=None, responsible_id=None ):
        self.id = id
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.complement = complement
        self.cep = cep 
        self.responsible_id = responsible_id

    @classmethod
    def createAddress(cls, address):
        # INSERIR NOVO ENDEREÇO EM UM ID DE RESPONSAVEL VALIDO
        try:
            DB = Database()

            sql = """
                INSERT INTO enderecos
                (cidade, bairro, rua, complemento, CEP, responsavel_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            params = (
                address.city,
                address.neighborhood,
                address.street,
                address.complement,
                address.cep,
                address.responsible_id
            )

            endereco_id = DB.insert(sql, params)

            print(f"Endereço inserido! ID: {endereco_id}")
            return endereco_id

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
        
        except Exception as e:
            print("Não foi possível atualizar:", e)
            raise RuntimeError("Falha ao atualizar o endereço!") from e
    
    @classmethod
    def readAddress(cls, responsible_id):
        # CONSULTAR ENDEREÇO ATRAVÉS DO RESPONSAVEL

        try:
            DB = Database()
            sql = """SELECT id, cidade, bairro, rua, complemento, CEP
                FROM enderecos
                WHERE responsavel_id = %s;
                """
            params = (responsible_id,)
            result = DB.fetchAll(sql, params)
            
            print("Seleção feita!")
            print(result)

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

        except Exception as e:
            print("Não foi possivel deletar endereço! ", e)
            raise RuntimeError("Falha ao excluir endereço!") from e
    
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

            print(result)

        except Exception as e:
            print("Não foi possivel encontrar responsável!", e)
            raise RuntimeError("Falha na procura!") from e

        
