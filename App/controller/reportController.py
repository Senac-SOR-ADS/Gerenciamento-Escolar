from App.model.reportModel import Report
from datetime import datetime
 
class ReportController:
    @classmethod
    def create(cls, description, studentID, parentID):
        try:
            description = ReportController.validateDescription(description)
            studentID = ReportController.validateID(studentID)
            parentID = ReportController.validateID(parentID)
            rep = Report(description=description, studentID=studentID, parentID=parentID)
            Report.create(rep)
        except Exception as e:
            raise e
 
    @classmethod
    def getAll(cls):
        lista = Report.getAll()
        return lista

    @classmethod
    def getByStudentID(cls, studentID):
        try:
            studentID = ReportController.validateID(studentID)
            lista = Report.searchStudentID(studentID)
            return lista
        except Exception as e:
            raise e

    @classmethod
    def edit(cls, id, description):
        if not description:
            print("Não foi possivel editar a descrição")
        else:
            try:
                description = ReportController.validateDescription(description)
                rep = Report(description=description, id=id)
                Report.edit(rep)
            except Exception as e:
                raise e
           
    @classmethod
    def validateIntervalDate(cls, initialDate, lastDate):
        try:
            initialDate = ReportController.validateDate(initialDate)
            lastDate = ReportController.validateDate(lastDate)
            a = Report.searchIntervalDate(initialDate, lastDate)
            if a == []:
                return False
            return a
        except Exception as e:
                raise e
   
    @classmethod
    def validateDate(cls, date):
        try:
            date = ReportController.validateDate(date)
            a = Report.searchDate(date)
            if a == []:
                return False
            return a
        except Exception as e:
                raise e
       
    @classmethod    
    def validateDescription(cls, value):
        description = value
        if not description: raise ValueError("Falta a descricao")
        return description
   
 
    @classmethod
    def validateID(cls, value):
        if not isinstance(value, int): raise TypeError(f"ID incorreto")
        if value <= 0: raise ValueError("Id invalido")
        return value
 
    @classmethod
    def validateDate(cls, date):
        try:
            validate = datetime.strptime(date, "%Y-%m-%d")
            return validate
        except ValueError:
            print("Erro: Data Inválida.")
            return
 
if __name__ == "__main__":
    # ReportController.create("Tá doendo dms", 2, 4)
    # controller = ReportController()
    # lista = controller.getByStudentID(18)
    # print(lista)
    # ReportController.create("Tá doendo dms", 18, 1)
    pass
 
