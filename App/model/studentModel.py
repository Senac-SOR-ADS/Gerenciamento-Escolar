from App.config.database import Database

class Student:
    id = None
    nome = ""
    nome_social = None
    CPF = ""
    data_nasc = ""
    RA = ""
    RM = ""
    obs = None
    status = True
    data_registro = ""
    data_status = None


    def __init__(self, id = None, nome = "", nome_social = None, CPF = "", data_nasc = "", RA = "", RM = "", obs = None, status = True, data_registro = "", data_status = None):
        self.id = id
        self.nome = nome
        self.nome_social = nome_social
        self.CPF = CPF
        self.data_nasc = data_nasc
        self.RA = RA
        self.RM = RM
        self.obs = obs
        self.status = status
        self.data_registro = data_registro
        self.data_status = data_status


    @classmethod
    def Create(cls, student:"Student"):
        try:
            DB = Database()
        
            sql = """INSERT INTO alunos (nome, nome_social, CPF, data_nasc, RA, RM, Observacao)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                 
            params = (student.nome, student.nome_social, student.CPF, student.data_nasc, student.RA, student.RM, student.obs)

            novo_id = DB.insert(sql, params) 
        
            print(f"Aluno inserido com sucesso! ID gerado: {novo_id}")
            return novo_id
        except Exception as erro:
            print(f'nao foi possível inserir novo aluno: {erro}')

    @classmethod
    def Update(cls, student: "Student"):
        try:
            DB = Database()
            sql = """UPDATE alunos SET nome = %s, nome_social = %s, CPF = %s, 
                    data_nasc = %s, RA = %s, RM = %s, Observacao = %s, status = %s 
                    WHERE id = %s"""
        
            
            params = (student.nome, student.nome_social, student.CPF, student.data_nasc, 
                     student.RA, student.RM, student.obs, student.status, student.id)
                  
            DB.execute(sql, params)
            print(f"Aluno atualizado con sucesso, RA: {student.RA}, ID: {student.id}")
            return student.RA, student.id
        except Exception as erro:
            print(f'Não foi possível atualizar os dados do aluno: {erro}')
        raise RuntimeError
        
    @classmethod
    def delet(cls, id):
        try:
            DB = Database()
            sql = "UPDATE alunos SET status = 0 WHERE id = %s"
            params = (id , )
            result = DB.execute(sql, params)
            print('aluno desativado com sucesso!')
            return result
        except Exception as erro:
            print(f'Erro ao tentar desativar o aluno {erro}')
            raise RuntimeError
    @classmethod
    def activate(cls, id):
        try:
            DB = Database()
            sql = "UPDATE alunos SET status = 1 WHERE id = %s"
            params = (id , )
            result = DB.execute(sql, params)
            print('aluno ativado com sucesso!')
            return result
        except Exception as erro:
            print(f'Erro ao tentar desativar o aluno {erro}')
            raise RuntimeError
        
    @classmethod
    def findById(cls, id):
        try:
            DB = Database()
            sql = "SELECT * FROM alunos WHERE id = %s"
            params = (id,)
            result = DB.fetchOne(sql , params)
            if not result:
                return None
            return cls(*result.values())
        except Exception as erro:
            print(f'Erro ao encontrar aluno por id {erro}')
            raise RuntimeError

    @classmethod
    def _getObjectlist(cls, lista):
        return [cls(*user)for user in lista]

    @classmethod
    def findAll(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM alunos"
            result = DB.fetchAll(sql)
            return cls._getObjectlist(result)
        except Exception as erro:
            print(f'Erro lsitagem de alunos: {erro}')
            raise RuntimeError
    
    @classmethod
    def findActive(cls):
        try:
            DB = Database()
            sql = "SELECT * FROM alunos WHERE status = 1"
            result = DB.fetchAll(sql)
            student = [cls(*row.values()) for row in result]
            return student
        except Exception as erro:
            print(f'Erro lista de alunos ativos {erro}')
            raise RuntimeError


if __name__ == "__main__":
    Student.findById(2)
