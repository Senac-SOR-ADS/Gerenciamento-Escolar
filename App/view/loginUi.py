from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class LoginUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/login.ui", self)
        self.show()

    @pyqtSlot()
    def on_btn_concluir_clicked(self):
        self.accept()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = LoginUI()
    app.exec_()

