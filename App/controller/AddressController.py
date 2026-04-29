from App.model.addressModel import Address
import requests

class AddressController:

    @classmethod
    def requestCep(cls, cep):
        # CONSULTAR CEP NA API

        cep = cep.replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            res = requests.get(url, timeout=5)  
            res.raise_for_status()
            dados = res.json()

            if "erro" in dados:
                raise requests.exceptions.RequestException("CEP não existe")

            return {
                "cep": dados.get("cep", ""),
                "city": dados.get("localidade", ""),
                "neighborhood": dados.get("bairro", ""),
                "street": dados.get("logradouro", ""),
            }
        

        except requests.exceptions.RequestException as e:
            print(e)
            return {}
        
    @classmethod
    def create(cls, responsible_id, form_data):
        # RECEBE OS DADOS DO CEP E ENVIA PARA A MODEL

        if not responsible_id:
            return {"RESPONSAVEL NÃO ENCONTRADO!"}

        if not form_data:
            return {"HOUVE UM PROBLEMA NO ENVIO DE DADOS, PREENCHA MANUALMENTE"}

        # VALIDANDO OS CAMPOS OBRIGATÓRIOS (sem CEP)
        required_fields = ["city", "neighborhood", "street"]
        for field in required_fields:
            if not form_data.get(field):
                return {f"PREENCHA TODOS CAMPOS OBRIGATÓRIOS"} 

        try:
            address = Address(
                cep=form_data.get("cep"),
                city=form_data.get("city"),
                neighborhood=form_data.get("neighborhood"),
                street=form_data.get("street"),
                complement=form_data.get("complement"),
                number=form_data.get("number"),
                responsible_id=responsible_id
            )

            adressID = address.createAddress(address)
            address.id = adressID
    
            return {
                "address_id": address.id,
                "cep": address.cep,
                "city": address.city,
                "neighborhood": address.neighborhood,
                "street": address.street,
                "complement": address.complement,
                "number": address.number
            }

        except Exception as e:
            return {"ERRO AO INSERIR DADOS" : e}
        
    @classmethod
    def update(cls, form_data):
        try:
            address = Address(
                id=form_data.get("id"),
                cep=form_data.get("cep"),
                city=form_data.get("city"),
                neighborhood=form_data.get("neighborhood"),
                street=form_data.get("street"),
                complement=form_data.get("complement"),
                number=form_data.get("number"),
                responsible_id=form_data.get("responsible_id")
            )


            Address.updateAddress(address)

            return {
                "address_id": address.id,
                "cep": address.cep,
                "city": address.city,
                "neighborhood": address.neighborhood,
                "street": address.street,
                "complement": address.complement,
                "number": address.number
            }

        except Exception as e:
            print("ERRO:", e)
            return {"ERRO AO ATUALIZAR DADOS": e}
        

        
    @classmethod
    def findAddressByParentId(cls, ParentId):

        try: 

            if ParentId:
                Address.readAddress(ParentId)

            else:
                print("Nao existe Id")

        except Exception as e:
            return {"Erro ao puxar endereço": e}


if __name__ == "__main__":

    form_data = {
        "id": 1,
        "cep": "18071-360",
        "city": "Yakutski",
        "neighborhood": "bairro santa casa",
        "street": "rua dos ventos",
        "complement": "",
        "number": "123",
        "responsible_id": 1,
    }
       
    dados = AddressController.update(form_data)
    print(dados)

