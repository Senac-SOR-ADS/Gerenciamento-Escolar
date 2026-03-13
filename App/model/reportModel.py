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
    def create(cls, report:Report):
        try:
            DB = Database()
            sql = "INSERT INTO `relatorios`(`data`, `descricao`, `aluno_id`, `responsavel_id`) VALUES (%s,%s,%s,%s)"
            params = (report.date, report.description, report.alunoId, report.responsavelId)
            DB.insert(sql, params)
            print("Relatório criado com sucesso")
        except Exception as e:
            print(f'Erro relatorio: {e}')
            raise RuntimeError

    @classmethod
    def edit(cls, id, description):
        try:
            DB = Database()
            sql = "UPDATE relatorios SET descricao= %s WHERE id = %s"
            params = (description, id)
            update = DB.execute(sql, params)
            print(update)
            if not update: raise Exception("Erro ao editar relatorio")
            return update
        except Exception as e:
            raise e

    @classmethod
    def searchUnique(cls, id):
        try:
            DB = Database()
            sql = "SELECT `id`, `data`, `descricao`, `aluno_id`, `responsavel_id` FROM `relatorios` WHERE id = %s"
            params = (id,)
            result = DB.fetchOne(sql, params)
            if result: 
                return cls._getObjectList([result])[0]
            return cls()
        except Exception as e:
            print(f'Erro ao buscar relatorio')
            raise RuntimeError

    @classmethod
    def searchDate(cls, date):
        try:
            DB = Database()
            sql = "SELECT `id`, `data`, `descricao`, `aluno_id`, `responsavel_id` FROM `relatorios` WHERE data = %s"
            params= (date,)
            result = DB.fetchAll(sql, params)
            return cls._getObjectList(result)
        except Exception as e:
            print(f'Erro ao buscar relatorio')
            raise RuntimeError

    @classmethod
    def _getObjectList(cls, lista):
        return [cls(*item.values()) for item in lista]
    
    @classmethod
    def getAll(cls):
        DB = Database()
        sql = "SELECT * FROM relatorios"
        result = DB.fetchAll(sql)
        return cls._getObjectList(result)

if __name__ == "__main__":
    # allReports = Report.getAll()
    # print(allReports)
    # v = Report(date= "2023-10-28", description= " relatóriossss", alunoId= 3, responsavelId= 3)
    # Report.create(v)
    # a = Report.searchDate("2023-10-27")
    # print(a)
    Report.edit(11, "O pé doeu demais1")
    report = Report.searchUnique(11)
    print(report.description)
