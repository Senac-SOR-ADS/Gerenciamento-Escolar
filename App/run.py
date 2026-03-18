from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication
from App.view.loginUI import LoginUI
from App.view.homeUI import HomeUI
<<<<<<< HEAD
from App.controller.loginController import LoginController, isLogged
=======
from App.controller.loginController import isLogged , logout

load_dotenv(override=True)
>>>>>>> b7f189892e76334c913ab91b2b8d123ad1f4f453

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