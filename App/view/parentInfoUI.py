from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.telephoneController import TelephoneController
from App.controller.parentController import ParentController



class ParentInfoUI(QDialog):
    
    def __init__(self, studentID,  **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/parentInfo.ui", self)
        self.studentID = studentID
        self.listParents = ParentController.findParentForStudent(self.studentID)
        self.listTelephone = TelephoneController.findTelephoneByParentId()
        self.populateComboBox()
        self.comboBox.currentIndexChanged.connect(self.getInfo)
        self.getInfo()
        self.show()
        
        
    def getInfo(self):
        indexResp = self.comboBox.currentIndex()
        parent = self.listParents[indexResp]
        self.nome.setText(parent.name)
        self.telefone.setText()
        self.cpf.setText(parent.cpf)
    
        
        
    
    def populateComboBox(self):
        try:
            for parent in self.listParents:
                self.comboBox.addItem(parent.name)
        except Exception as e:
            print(f"{e}")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    from App.controller.studentController import StudentController
    aluno = StudentController.getById(19)
    app = QApplication([])
    login = ParentInfoUI(aluno.id)
    app.exec_()