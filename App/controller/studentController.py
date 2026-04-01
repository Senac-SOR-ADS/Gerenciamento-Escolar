from App.config.database import Database
from App.model.studentModel import Student
 
class StudentController:

    

    CAMPOS_OBRIGATORIOS = ['nome', 'CPF', 'data_nasc', 'RA', 'RM']
    

    LIMITES_CARACTERES = {
        'nome': 100,
        'nome_social': 100,
        'CPF': 14,  # Formato: 000.000.000-00
        'RA': 20,
        'RM': 20,
        'obs': 500
    }
    
    @classmethod
    def validarCampoPreenchido(cls, valor, nome_campo):
        """Valida se um campo está preenchido."""
        if valor is None or str(valor).strip() == '':
            return False, f"O campo '{nome_campo}' é obrigatório."
        return True, None
    
    @classmethod
    def validarTamanhoMaximo(cls, valor, nome_campo, limite):
        """Valida se o campo não excede o tamanho máximo."""
        if valor and len(str(valor)) > limite:
            return False, f"O campo '{nome_campo}' deve ter no máximo {limite} caracteres."
        return True, None