from App.model.parentModel import Parent 
from App.controller.AddressController import AddressController
from App.controller.telephoneController import TelephoneController
import re

class ParentController:
    
    @classmethod
    def validCpf(cls, cpf):
        pass


    @classmethod
    def create(cls, parent:any):
        try:
            newParent:Parent = Parent(nome=parent["nome"], cpf=parent["cpf"])
            if not newParent.name.strip() or not newParent.cpf:
                print(f'E necessario preencher todos os dados')
                return False
            parentID = Parent.create(newParent.name, newParent.cpf)
            if parentID:
                address = parent.get('address')
                resp = AddressController.create(parentID, address)
                print(resp)

                telephone = parent.get('telephone')
                resp = TelephoneController.create(parentID, telephone)
                print(resp)
        except Exception as e:
            print(f'Erro ao tentar a criação de usuario {e}')
            raise RuntimeError
        
    @classmethod
    def update(cls, parent: any):
        try:
            updatedParent: Parent = Parent(nome=parent["nome"], cpf=parent["cpf"], id=parent["id"])
            if not updatedParent.name.strip() or not updatedParent.cpf:
                print(f'E necessario preencher todos os dados')
                return False
            updated = Parent.update(updatedParent)
            if updated is not None:
                address = parent.get('address')
                if address:
                    resp = AddressController.update(address)
                    print(resp)

                telephone = parent.get('telephone')
                if telephone:
                    resp = TelephoneController.update(telephone["id"], telephone["telephone"])
                    print(resp)
        except Exception as e:
            print(f'Erro ao tentar a atualização de usuario {e}')
            raise RuntimeError
        
    

if __name__ == "__main__":
    testParent = {
        "id": 52,
        "nome": "Gustavo Tubarão",
        "cpf": "50532394382",
        "address": {"responsible_id": 52, "city": "Cajuru", "neighborhood": "Palmeiras", "street": "João Melão", "complement": "Casa", "cep": "17704293"},
        "telephone": {"id": 52, "telephone": "20981392892"}
    }
    ParentController.update(testParent)