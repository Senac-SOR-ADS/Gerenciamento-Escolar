from PyQt5.QtWidgets import QDialog, QDateEdit
from PyQt5.QtCore import pyqtSlot, QDate , pyqtSignal
from PyQt5.uic import loadUi
from App.controller.studentController import StudentController


class RegisterStudentUI(QDialog):

    signal_alunoRegistrado = pyqtSignal(object)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/registerStudent.ui", self)
        self.show()

    def validateAll(self):
        nome = self.nome.text()
        data_nasc = self.data_nasc.date()
        data_nasc = data_nasc.toString("dd/MM/yyyy") 
        nome_social = self.nome_social.text()
        cpf = self.cpf.text()
        ra = self.ra.text()
        rm = self.rm.text()
        observacao = self.observacao.text()

        return {
            "nome": nome,
            "data_nasc": data_nasc,
            "nome_social": nome_social,
            "CPF": cpf,
            "RA": ra,
            "RM": rm,
            "observacao": observacao,
        }

    @pyqtSlot()
    def on_btn_continuar_clicked(self):
        user = self.validateAll()

        if user:
            print(user)
            try:
                student = StudentController.create(user)
                self.signal_alunoRegistrado.emit(student.id)
                self.clearText()
            except Exception as e:
                print(f"Erro: \n{e}")

    def clearText(self):
        self.nome.clear()
        self.data_nasc.setDate(QDate.currentDate())
        self.nome_social.clear()
        self.cpf.clear()
        self.ra.clear()
        self.rm.clear()
        self.observacao.clear()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = RegisterStudentUI()
    app.exec_()