from App.model.addressModel import Address
import httpx
import time
import asyncio

class AddressController:

    @classmethod
    async def requestCep(cls, cep):
        # CONSULTAR CEP NA API

        cep = cep.replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                res = await client.get(url)  
                res.raise_for_status()
                dados = res.json()

            if "erro" in dados:
                print("CEP não existe")
                return None

            return {
                "city": dados.get("localidade", ""),
                "neighborhood": dados.get("bairro", ""),
                "street": dados.get("logradouro", "")
            }

        except httpx.RequestError:
            print("Erro ao conectar com a API")
            return None
        
        

    @classmethod
    def create(cls, form_data):
        # RECEBE OS DADOS DO CEP E ENVIA PARA A MODEL
        if not form_data:
            return {"HOUVE UM PROBLEMA NO ENVIO DE DADOS, PREENCHA MANUALMENTE"}

        # VALIDANDO OS CAMPOS OBRIGATÓRIOS (sem CEP)
        required_fields = ["city", "neighborhood", "street", "responsible_id"]
        for field in required_fields:
            if not form_data.get(field):
                return {f"PREENCHA TODOS CAMPOS OBRIGATÓRIOS, FALTA: {field}"} 

        try:
            address = Address(
                cep=form_data.get("cep"),
                city=form_data.get("city"),
                neighborhood=form_data.get("neighborhood"),
                street=form_data.get("street"),
                complement=form_data.get("complement"),
                responsible_id=form_data.get("responsible_id")
            )

            address.createAddress(address) 
            


    
            return {
                "address_id": "id",
                "cep": address.cep,
                "city": address.city,
                "neighborhood": address.neighborhood,
                "street": address.street,
                "complement": address.complement
            }

        except Exception as e:
            return {"ERRO AO INSERIR DADOS" : str(e)}
        






