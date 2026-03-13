from App.config.database import Database

class Report:
    id = None
    date = ""
    description = ""
    alunoId = ""  
    responsavelId = ""

    def __init__(self, id=None, date="", description="", alunoId="", responsavelId=""):
        self.id = id
        self.date = date
        self.description = description
        self.alunoId = alunoId
        self.responsavelId = responsavelId 

    @classmethod
    def create(cls, date, description, alunoId, responsavelId):
        try:
            DB = Database()
            sql = "INSERT INTO `relatorios`(`data`, `descricao`, `aluno_id`, `responsavel_id`) VALUES (%s,%s,%s,%s)"
            Reporta = (date, description, alunoId, responsavelId)
            DB.insert(sql, Reporta)
            print("Relatório criado com sucesso")
        except Exception as e:
            print(f'Erro ao criar relatorio')
            raise RuntimeError

    @classmethod
    def edit(cls):
        # Atualiza o relatorio
        sql = ""
        pass

    @classmethod
    def search(cls, id):
        # busca por um id especifico
        sql = ""
        pass

    @classmethod
    def searchDate(cls, id, date):
        # Mostra as infos gerais do relatorio
        sql = ""
        pass

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*user) for user in lista]
    
    @classmethod
    def getAll(cls):
        DB = Database()
        sql = "SELECT * FROM relatorios"
        result = DB.fetchAll(sql)
        return cls._getObjectList(result)

if __name__ == "__main__":
    allReports = Report.getAll()
    print(allReports)
    Report.create("2023-10-27", " relatório", 3, 1)
