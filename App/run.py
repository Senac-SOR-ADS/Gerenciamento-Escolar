from PyQt5.QtWidgets import QApplication
from App.view.loginUI import LoginUI

app = QApplication([])
login = LoginUI()
res = login.exec_()
if res:
    print("Login successful")

print("Exiting application")
    