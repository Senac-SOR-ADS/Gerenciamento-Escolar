from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.uic import loadUi
from App.controller.userController import UserController, logout

class LoginUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/login.ui", self)
        self.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.clearText)
        # self.label.setStyleSheet("QLabel {backgroud-color: red; color: white; }")


    def clearText(self):
        self.senha.clear()
        self.mensagem.clear()


    @pyqtSlot()
    def on_btn_concluir_clicked(self):
        nome = self.nome.text()
        senha = self.senha.text()
        resp = UserController.login(nome , senha)
        if resp:
            self.clearText()
            self.accept()
        else:
            #  self.mensagem(self)
             self.clearText()
             self.mensagem.setText("Usuário ou senha incorretos")
             self.timer.start(4000)

    def on_btn_pushExit_clicked(self, sair):
        try: 
            logout(sair)
            self.close()
        except Exception as e:
            print(f"Erro ao sair! {e}")
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = LoginUI()
    app.exec_()




