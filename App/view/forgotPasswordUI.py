from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class adminUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/forgotPassword.ui", self)
        self.show()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = adminUI()
    app.exec_()