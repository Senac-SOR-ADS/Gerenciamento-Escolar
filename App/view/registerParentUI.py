from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.utils.qthread import Trabalhador
from App.controller.AddressController import AddressController
from App.controller.parentController import ParentController

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

    def validateAll(self):
        nome = self.nome.text()
        telefone = self.telefone.text()
        cpf = self.cpf.text()
        resp_legal = self.resp_legal.isChecked()
        cep = self.cep.text()
        cidade = self.cidade.text()
        rua = self.rua.text()
        bairro = self.bairro.text()
        numero = self.numero.text()
        complemento = self.complemento.text()

        return {
            "name": nome,
            "telefone": telefone,
            "cpf": cpf,
            "resp_legal": resp_legal,
            "address" : {
                "city" : cidade ,
                "neighborhood" : bairro ,
                "street" : f'{rua}, {numero}',
                "complement" : complemento,
                "cep" : cep
                }
        }

    @pyqtSlot()
    def on_btn_concluir_clicked(self):
        user = self.validateAll()

        if user:
            print(user)
            try:
                ParentController.create(user)
                # self.clearText()
            except Exception as e:
                print(f"Erro: \n{e}")

    def clearText(self):
        self.nome.clear()
        self.telefone.clear()
        self.cpf.clear()
        self.resp_legal.setChecked(False)
        self.cep.clear()
        self.cidade.clear()
        self.rua.clear()
        self.bairro.clear()
        self.numero.clear()
        self.complemento.clear()


        
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = RegisterParentUI()
    app.exec_()