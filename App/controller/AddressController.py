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
        
        


    def create(self, form_data):
        # RECEBE OS DADOS DO CEP E ENVIA PARA A MODEL
        if not form_data:
            return {"success": False, "error": "HOUVE UM PROBLEMA NO ENVIO DE DADOS, PREENCHA MANUALMENTE"}

        # VALIDANDO OS CAMPOS OBRIGATÓRIOS (sem CEP)
        required_fields = ["city", "neighborhood", "street", "responsible_id"]
        for field in required_fields:
            if not form_data.get(field):
                return {"success": False, "error": f"PREENCHA TODOS CAMPOS OBRIGATÓRIOS, FALTA: {field}"}

        # CAMPOS OPCIONAIS
        complement = form_data.get("complement")  
        cep = form_data.get("cep")  

        # MONTANDO OS DADOS
        try:
            address = Address(
                cep=cep,
                city=form_data["city"],
                neighborhood=form_data["neighborhood"],
                street=form_data["street"],
                complement=complement,
                responsible_id=form_data["responsible_id"]
            )

            # METODO DA MODEL
            address.createAddress(address)  

    
            return {
                "success": True,
                "address_id": getattr(address, "id", None),
                "cep": address.cep,
                "city": address.city,
                "neighborhood": address.neighborhood,
                "street": address.street,
                "complement": address.complement
            }

        except Exception as e:
            return {"success": False, "error": str(e)}


