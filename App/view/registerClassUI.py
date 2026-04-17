from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QDate, pyqtSlot, pyqtSignal
from PyQt5.uic import loadUi
from App.controller.roomController import RoomController

class RegisterClassUI(QDialog):

    signal_IdRoom = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
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

        if not turma or not data:
            print("Preencha todos os campos!")
            return None

        return {
            "room": turma,
            "date": data
        }
        

    @pyqtSlot()
    def on_btn_confirmar_clicked(self):
        classe = self.validarCampos()

        if classe:
            try:
                resultado = RoomController.createRoom(*classe.values())
                self.signal_IdRoom.emit(True) 
                self.clearText()
            except Exception as e:
                print(f"Erro: \n{e}")

if __name__ == "__main__":
    app = QApplication([])
    register = RegisterClassUI()
    app.exec_()