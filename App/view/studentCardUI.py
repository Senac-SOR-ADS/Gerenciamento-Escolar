from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

from App.view.newReportUI import NewReportUI
from App.view.parentInfoUI import ParentInfoUI

class StudentCardUI(QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/studentCard.ui", self)
        
        self.studentName.clicked.connect(self.openScreen)
        self.newReport.clicked.connect(self.openScreen)
        self.parentInfo.clicked.connect(self.openScreen)

        
    def openScreen(self):
        sender = self.sender()
        if sender == self.studentName:
            self.studentCard = StudentCardUI()
            self.studentCard.show()
        elif sender == self.newReport:
            self.newReport = NewReportUI()
            self.newReport.show()
        elif sender == self.parentInfo:
            self.parentInfo = ParentInfoUI()
            self.parentInfo.show()
        

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = StudentCardUI()
    login.show()
    app.exec_()