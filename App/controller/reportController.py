from App.model.reportModel import Report
from datetime import datetime

class ReportController:

    def create(self, description, studentID, parentID):
        try:
            description = self.validateDescription(description)
            studentID = self.validateID(studentID, "studentID")
            parentID = self.validateID(parentID, "parentID")
            rep = Report(description=description, studentID=studentID, parentID=parentID)
            Report.create(rep)
        except Exception as e:
            raise e

    def getAll(self, ):
        lista = Report.getAll()
        for item in lista:
            print(item.id, item.description)

    def edit(self, id, description):
        if not description:
            print("Não foi possivel editar a descrição")
        else:
            try:
                description = self.validateDescription(description)
                rep = Report(description=description, id=id)
                Report.edit(rep)
            except Exception as e:
                raise e
            
    def checkIntervalDate(self, initialDate, lastDate):
        try:
            initialDate = self.validateDate(initialDate)
            lastDate = self.validateDate(lastDate)
            a = Report.searchIntervalDate(initialDate, lastDate)
            if a == []:
                return False
            return a
        except Exception as e:
                raise e
        
    def checkDate(self, date):
        try:
            date = self.validateDate(date)
            a = Report.searchDate(date)
            if a == []:
                return False
            return a
        except Exception as e:
                raise e
             
    def validateDescription(self, value):
        description = value.strip()
        if not description: raise ValueError("Falta a descricao")
        return description

    def validateID(self, value):
        if not isinstance(value, int): raise TypeError(f"ID incorreto")
        if value <= 0: raise ValueError("Id invalido")
        return value

    def validateDate(self, date):
        try:
            validate = datetime.strptime(date, "%Y-%m-%d")
            return validate
        except ValueError:
            print("Erro: Data Inválida.")
            return

if __name__ == "__main__":
    pass
