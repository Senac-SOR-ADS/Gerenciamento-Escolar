from App.model.parentModel import Parent 
import re

class ParentController:
    
    @classmethod
    def validCpf(cls, cpf):
        pass


    @classmethod
    def createParent(cls, parent:any):
        try:
            parent:Parent = Parent(name=parent["name"], cpf=parent["cpf"])
            if not parent.name.strip() or not parent.cpf:
                print(f'E necessario preencher todos os dados')
                return False
            parent_create = Parent.create(parent.name, parent.cpf)
            if parent_create:
                return

        except Exception as e:
            print(f'Erro ao tentar a criação de usuario {e}')
            raise RuntimeError
        
    

if __name__ == "__main__":
    usuario = {
        "name" : "cavalo",
        
    }
    Parent.createUser(usuario)