from PyQt5.QtWidgets import QDialog, QDateEdit
from PyQt5.QtCore import QDate
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.roomController import RoomController

class RegisterClassUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/registerClass.ui", self)
        self.clearText()
        self.show()

    def clearText(self):
        self.turma.clear()
        self.data.setDate(QDate.currentDate())
        
    def validarCampos(self):
        turma = self.turma.text()
        data = self.data.date() #retorna um QDate
        data = data.toString("yyyy/MM/dd") #transforma em padrão EUA

        if not turma and not data:
            print(f'Preencha os campos!')

        return {
            "room": turma,
            "date": data
        }
    
    @pyqtSlot()
    def on_btn_confirmar_clicked(self):
        classe = self.validarCampos()

        if classe:
            try:
                RoomController.createRoom(*classe.values())
                self.clearText()
            except Exception as e:
                print(f"Erro: \n{e}")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = RegisterClassUI()
    app.exec_()




