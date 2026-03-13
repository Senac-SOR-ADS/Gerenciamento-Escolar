from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication
from App.view.loginUI import LoginUI
from App.view.homeUI import HomeUI
from App.controller.loginController import isLogged , logout

load_dotenv(override=True)

app = QApplication([])
login = LoginUI()

while not isLogged():
    res = login.exec_()
    if res:
        tela = HomeUI()
        app.exec_()
        logout()
    else:
        break
print('programa encerrado')