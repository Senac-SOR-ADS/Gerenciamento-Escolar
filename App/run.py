from PyQt5.QtWidgets import QApplication
from App.view.loginUI import LoginUI

app = QApplication([])
login = LoginUI()

while True:
    res = login.exec_()
    if res:
        from App.view.homeUI import HomeUI
        home = HomeUI()
        app.exec_()

    print("Exiting application")
    