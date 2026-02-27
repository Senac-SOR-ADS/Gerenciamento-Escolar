from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.loginController import validateLogin

class LoginUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/login.ui", self)
        self.show()

    @pyqtSlot()
    def on_btn_concluir_clicked(self):
        nome = self.nome.text()
        senha = self.senha.text()
        resp = validateLogin(nome , senha)
        if resp:
            self.accept()
        else:
            print("usuario ou senha incorreto")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = LoginUI()
    app.exec_()

