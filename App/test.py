import asyncio
from App.controller.addressController import AddressController
from App.model.addressModel import Address

async def main():
    cep_digitado = input("Digite o CEP: ")

    # Aqui usamos await, porque requestCep é async
    dados_cep = await AddressController.requestCep(cep_digitado)

    if not dados_cep:
        print("Não foi possível obter dados do CEP. Preencha manualmente.")
        dados_cep = {
            "city": input("Cidade: "),
            "neighborhood": input("Bairro: "),
            "street": input("Rua: ")
        }

    complement = input("Complemento (opcional): ") or "Casa"
    responsible_id = int(input("ID do responsável: "))

    # Montando form_data com CEP opcional
    form_data = {
        "cep": cep_digitado,  # opcional
        "city": dados_cep["city"],
        "neighborhood": dados_cep["neighborhood"],
        "street": dados_cep["street"],
        "complement": complement,
        "responsible_id": responsible_id
    }

    # Chama a função create da controller
    controller = AddressController()
    resultado = controller.create(form_data)
    print("Resultado Create:", resultado)

# Executa a função async
asyncio.run(main())