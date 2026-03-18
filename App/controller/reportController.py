from App.model.reportModel import Report

def validateDescription(value):
    description = value.strip()
    if not description: raise ValueError("Falta a descricao")
    return description

def validateId(value, nome):
    if not isinstance(value, int): raise TypeError(f"{nome} incorreto")
    if value <= 0: raise ValueError("Id invalido")
    return value

def create(description, studentID, parentID):
    try:
        description = validateDescription(description)
        studentID = validateId(studentID, "studentID")
        parentID = validateId(parentID, "parentID")
        rep = Report(description=description, studentID=studentID, parentID=parentID)
        Report.create(rep)
    except Exception as e:
        raise e

def getAll():
    lista = Report.getAll()
    for item in lista:
        print(item.id, item.description)

def edit(id, description):
    if not description:
        print("Não foi possivel editar a descrição")
    else:
        try:
            description = validateDescription(description)
            rep = Report(description=description, id=id)
            Report.edit(rep)
        except Exception as e:
            raise e


if __name__ == "__main__":
    # create(" asd", 2, 1)
    edit(8,"A criança ta doente")
    # getAll()
