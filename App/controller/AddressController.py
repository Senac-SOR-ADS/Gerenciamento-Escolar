from App.model.addressModel import Address
import httpx
import time
import asyncio

class AddressController:

    cep = ""

    def __init__(self, cep=""):
        self.cep = cep

    data = {
        "city": "São Paulo",
        "street": "Rua A",
        "neighborhood": "Eden",
        "complement": "Casa",
        "responsible_id": 1
        }



    @classmethod
    def requestCep(cls, cep):
        try:
            cep = cep.replace("-", "").strip()

            url = f"https://viacep.com.br/ws/{cep}/json/"
            res = httpx.get(url)
            dados = res.json()

            if "erro" in dados:
                return {"error": "CEP não existe"}

            return {
                "city": dados.get("localidade"),
                "street": dados.get("logradouro"),
                "neighborhood": dados.get("bairro"),
            }

        except httpx.exceptions.RequestException:
            return {"error": "Erro ao conectar com a API"}
        
        


    def create(self, data):

        if "city" not in data or "street" not in data or "neighborhood" not in data:
            print("Faltam dados obrigatórios")
            return

        address = Address(
            cep=data.get("cep"),
            city=data["city"],
            neighborhood=data["neighborhood"],
            street=data["street"],
            complement=data.get("complement"),
            responsible_id=data["responsible_id"]
        )

        print("Endereço criado")
        print("CEP:", address.cep)
        print("Cidade:", address.city)
        print("Rua:", address.street)
        print("Bairro:", address.neighborhood)
        print("Complemento:", address.complement)
        print("Responsável ID:", address.responsible_id)

        return address


if __name__ == "__main__":

    controller = AddressController()

    cep = input("Digite o CEP: ")

    resultado = controller.requestCep(cep)

    if "error" in resultado:
        print(resultado["error"])

        data = {
            "cep": cep,
            "city": input("Digite a cidade: "),
            "street": input("Digite a rua: "),
            "neighborhood": input("Digite o bairro: "),
            "complement": input("Digite o complemento (opcional): "),
            "responsible_id": 1
        }

    else:
        print("Dados pelo CEP:")
        print(resultado)

        data = {
            "cep": cep,
            "city": resultado["city"],
            "street": resultado["street"],
            "neighborhood": resultado["neighborhood"],
            "complement": input("Digite o complemento (opcional): "),
            "responsible_id": 1
        }

    controller.create(data)