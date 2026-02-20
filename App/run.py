from PyQt5.QtWidgets import QApplication
from App.view.loginUi import LoginUI
from App.view.homeUI import HomeUI
from App.controller.loginController import LoginController, isLogged

app = QApplication([])
login = LoginUI()

while not isLogged():
    res = login.exec_()
    if res:
        tela = HomeUI()
        app.exec_()
    else:
        break
print('programa encerrado')