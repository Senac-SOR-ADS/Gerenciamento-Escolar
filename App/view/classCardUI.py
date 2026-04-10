from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class ClassCardUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/classCard.ui", self)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    card = ClassCardUI()
    card.show()
    app.exec_()