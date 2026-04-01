from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.uic import loadUi
from App.utils.qthread import Trabalhador
from App.controller.AddressController import AddressController

class RegisterParentUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/registerParent.ui", self)
        self.show()
        self.cep.editingFinished.connect(self.buscarCEP)
        
    def buscarCEP(self):
        cep = self.cep.text()
        self.validarCEP =Trabalhador(AddressController.requestCep, cep=cep)
        self.validarCEP.finalizado.connect(self.popularCEP)
        self.validarCEP.finished.connect(self.validarCEP.deleteLater)
        self.validarCEP.start()

    def popularCEP(self, dadosCEP):
        self.cidade.setText(dadosCEP.get("city"))
        self.bairro.setText(dadosCEP.get("neighborhood"))
        self.rua.setText(dadosCEP.get("street"))

    def validadeAll(self):
        nome = self.nome.text()
        telefone = self.telefone.text()
        cep = self.cep.text()
        resp_legal = self.resp_legal.text()

        return {
            "name": nome,
            "phone": telefone,
            "resp_legal": resp_legal,
            "cep": cep
        }

    @pyqtSlot()
    def on_btn_concluir_clicked(self):
        resp = self.validadeAll()
        print(resp)




if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = RegisterParentUI()
    app.exec_()


    # 18053000
