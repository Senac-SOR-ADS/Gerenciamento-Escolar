from App.model.addressModel import Address

class AddressController:

    data = {
        "city": "São Paulo",
        "street": "Rua A",
        "neighborhood": "Eden",
        "complement": "Casa",
        "responsible_id": 1
        }


    def create(self, data):
        # PUXAR OS DADOS DO FRONT
        address = Address(
            city=data["city"],
            neighborhood=data["neighborhood"],
            street=data["street"],
            complement=data.get("complement"),
            responsible_id=data["responsible_id"] 
        )
    


result = AddressController.create(data)

print(result.city)