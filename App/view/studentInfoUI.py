from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.studentController import StudentController
class StudentInfoUI(QDialog):
    def __init__(self,studentID, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/studentInfo.ui", self)
        self.studentID = studentID
        self.listStudent = StudentController.getById(self.studentID)
        self.getInfo()
        self.show()


    def getInfo(self):
        student = self.listStudent
        print(student)
        self.nome_4.setText(student.nome)
        self.nomeSocial.setText(student.nome_social)
        self.data_6.setDate(student.data_nasc)
        self.cpf_3.setText(student.CPF)
        self.ra.setText(student.RA)
        self.rm.setText(student.RM)
        self.obs.setText(student.obs)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    aluno = StudentController.getById(1)
    app = QApplication([])
    login = StudentInfoUI(aluno.id)
    app.exec_()