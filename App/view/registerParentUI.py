from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.utils.qthread import Trabalhador
from App.controller.AddressController import AddressController

class RegisterParentUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/registerParent.ui", self)
        self.show()

    @pyqtSlot()
    def on_btn_concluir_clicked(self):
        self.cep =Trabalhador(AddressController.requestCep)
        self.cep.finalizado.connect(self.create)
        self.cep.finished.connect(self.cep.deleteLater)
        self.cep.start()

        self.btn_concluir.setEnabled(False)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = RegisterParentUI()
    app.exec_()