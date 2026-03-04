from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.controller.loginController import logout

class HomeUI(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/home.ui", self)
        self.show()


    def on_btn_pushExit_clicked(self, sair):
        try: 
            logout(sair)
            self.close()
        except Exception as e:
            print(f"Erro ao sair! {e}")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    home = HomeUI()
    app.exec_()
