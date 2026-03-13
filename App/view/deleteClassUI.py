from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class DeleteClass(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/deleteClass.ui", self)
        self.show()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = DeleteClass()
    app.exec_()