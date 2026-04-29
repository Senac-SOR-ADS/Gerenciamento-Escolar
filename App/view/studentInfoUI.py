from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.studentController import StudentController
class StudentInfoUI(QDialog):
    def __init__(self, student, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/studentInfo.ui", self)
        self.student = student
        self.getInfo()
        self.show()


    def getInfo(self):
        self.nome_4.setText(self.student.nome)
        self.nomeSocial.setText(self.student.nome_social)
        self.data_6.setDate(self.student.data_nasc)
        self.cpf_3.setText(self.student.CPF)
        self.ra.setText(self.student.RA)
        self.rm.setText(self.student.RM)
        self.obs.setText(self.student.obs)
        
        self.cpf_3.setReadOnly(True)
        self.ra.setReadOnly(True)
        self.rm.setReadOnly(True)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    aluno = StudentController.getById(7)
    app = QApplication([])
    login = StudentInfoUI(aluno)
    app.exec_()