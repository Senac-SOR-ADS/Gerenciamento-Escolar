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
                "city": dados.get("localidade", ""),
                "neighborhood": dados.get("bairro", ""),
                "street": dados.get("logradouro", "")
            }

        except requests.exceptions.RequestException as e:
            print(e)
            return {}
        
    @classmethod
    def create(cls, form_data):
        # RECEBE OS DADOS DO CEP E ENVIA PARA A MODEL
        if not form_data:
            return {"HOUVE UM PROBLEMA NO ENVIO DE DADOS, PREENCHA MANUALMENTE"}

        # VALIDANDO OS CAMPOS OBRIGATÓRIOS (sem CEP)
        required_fields = ["city", "neighborhood", "street", "responsible_id"]
        for field in required_fields:
            if not form_data.get(field):
                return {f"PREENCHA TODOS CAMPOS OBRIGATÓRIOS"} 

        try:
            address = Address(
                cep=form_data.get("cep")  ,
                city=form_data.get("city"),
                neighborhood=form_data.get("neighborhood"),
                street=form_data.get("street"),
                complement=form_data.get("complement"),
                responsible_id=form_data.get("responsible_id")
            )

            adressID = address.createAddress(address)
            address.id = adressID
    
            return {
                "address_id": address.id,
                "cep": address.cep,
                "city": address.city,
                "neighborhood": address.neighborhood,
                "street": address.street,
                "complement": address.complement
            }

        except Exception as e:
            return {"ERRO AO INSERIR DADOS" : e}
        





if __name__ == "__main__":
    endereco = {
        "cep": "18053000",
        "city": "sorocaba",
        "neighborhood": "Julio de Mesquita",
        "street": "Americo Figueiredo",
        "complement": "",
        "responsible_id": 1}
    
    cep = AddressController.requestCep("18075000")
    print(cep)
    res = AddressController.create(endereco)
    print(res)
