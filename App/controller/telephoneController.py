from App.model.telephoneModel import Telephone


class TelephoneController:

    @classmethod
    def create(cls, responsible_id, form_data):

        if not form_data:
            return {"HOUVE UM PROBLEMA NO RECEBIMENTO DO TELEFONE"}
        
        if not responsible_id:
            return {"RESPONSAVEL NÃO ENCONTRADO"}
        
        try:

            insert = Telephone.create(form_data, responsible_id)
            return insert
        
        except Exception as e:
            return {"ERRO AO INSERIR DADOS" : e}
        
    @classmethod
    def update(cls, id, form_data):

        if not form_data:
            return {"TELEFONE NÃO FOI PASSADO"}
        
        if not id:
            return {"TELEFONE NÃO FOI ENCONTRADO"}
        
        try:

            update = Telephone.update(form_data, id)
            return update
        
        except Exception as e:
            return {"ERRO AO ATUALIZAR DADOS" : e}
        
    @classmethod
    def findTelephoneByParentId(cls, ParentId):

        try: 

            if ParentId:
                find = Telephone.parentTelephone(ParentId)
                return find

            else:
                print("Nao existe Id")

        except Exception as e:
            return {"Erro ao puxar telefone": e}
        
    @classmethod
    def delete(cls, id_telephone):

        try:

            if not id_telephone:
                return {" TELEFONE NÃO FOI PASSADO "}
            
            Telephone.delete(id_telephone)

        except Exception as e:
            return {"Erro ao Excluir telefone"}
    


        
        



if __name__ == "__main__":

    TelephoneController.delete(54)




        
