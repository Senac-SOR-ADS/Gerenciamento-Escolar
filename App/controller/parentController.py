from App.model.parentModel import Parent 
from App.controller.AddressController import AddressController
import re

class ParentController:
    
    @classmethod
    def validCpf(cls, cpf):
        pass


    @classmethod
    def create(cls, parent:any):
        try:
            newParent:Parent = Parent(name=parent["name"], cpf=parent["cpf"])
            if not newParent.name.strip() or not newParent.cpf:
                print(f'E necessario preencher todos os dados')
                return False
            parentID = Parent.create(newParent.name, newParent.cpf)
            if parentID:
                address = parent.get('address')
                address['responsible_id'] = parentID
                resp = AddressController.create(address)
                print(resp)
        except Exception as e:
            print(f'Erro ao tentar a criação de usuario {e}')
            raise RuntimeError
        
    @classmethod
    def update(cls, parent: any):
        try:
            updatedParent: Parent = Parent(name=parent["name"], cpf=parent["cpf"], id=parent["id"])
            if not updatedParent.name.strip() or not updatedParent.cpf:
                print(f'E necessario preencher todos os dados')
                return False
            updated = Parent.update(updatedParent)
            if updated:
                address = parent.get('address')
                if address:
                    resp = AddressController.update(address)
                    print(resp)
        except Exception as e:
            print(f'Erro ao tentar a atualização de usuario {e}')
            raise RuntimeError
        
    

if __name__ == "__main__":
    testParent = {
        "name" : "cavalo",
        "cpf" : "1234567233",
        "address" : {"city" : "Sorocaba" , "neighborhood" : "Paineras" , "street" : "Vitor Gomes", "complement" : "Scrum-Master", "cep" : "1909192"}
    }
    ParentController.create(testParent)