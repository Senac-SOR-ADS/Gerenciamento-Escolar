from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.telephoneController import TelephoneController
from App.controller.parentController import ParentController
from App.controller.AddressController import AddressController



class ParentInfoUI(QDialog):
    
    def __init__(self, studentID, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/parentInfo.ui", self)
        self.studentID = studentID
        self.listParents = ParentController.findParentForStudent(self.studentID)
        
        self.populateComboBox()
        self.comboBox.currentIndexChanged.connect(self.getInfo)
        self.btnRemover.clicked.connect(self.removeParent)
        self.getInfo()
        self.show()
        
        
    def getInfo(self):
        indexResp = self.comboBox.currentIndex()
        parent = self.listParents[indexResp]

        self.nome.setText(parent.name)
        self.cpf.setText(parent.cpf)
        self.respLegal.setChecked(parent.legal_guardian)

        listTelephone = TelephoneController.findTelephoneByParentId(parent.id)
        self.telefone.setText(listTelephone[0].telephone)

        listAddress = AddressController.findAddressByParentId(parent.id)
        self.cidade.setText(listAddress[0].city)
        self.complemento.setText(listAddress[0].complement)
        self.rua.setText(listAddress[0].street)
        self.bairro.setText(listAddress[0].neighborhood)
        self.cep.setText(listAddress[0].cep)
        self.numero.setText(listAddress[0].number)
        
    
    
    def populateComboBox(self):
        try:
            for parent in self.listParents:
                self.comboBox.addItem(parent.name)
        except Exception as e:
            print(f"{e}")

    def removeParent(self):
        try:
            indexResp = self.comboBox.currentIndex()
            parent = self.listParents[indexResp]
            ParentController.deleteParent(parent.id, self.studentID)
            self.listParents.pop(indexResp)
            self.comboBox.removeItem(indexResp)
        except Exception as e:
            print(f"Erro ao remover parente: {e}")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    from App.controller.studentController import StudentController
    aluno = StudentController.getById(11)
    app = QApplication([])
    login = ParentInfoUI(aluno.id)
    app.exec_()