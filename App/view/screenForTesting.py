# File created specifically for testing all the funtionalities of view.

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.view.loginUi import LoginUI
from App.view.newReportUI import NewReportUI
from App.view.homeUI import HomeUI
from App.view.deleteClassUI import DeleteClassUI
from App.view.parentEditUI import ParentEditUI
from App.view.studentEditUI import StudentEditUI
from App.view.parentInfoUI import ParentInfoUI
from App.view.studentInfoUI import StudentInfoUI
from App.view.registerEmployeeUI import RegisterEmployeeUI
from App.view.deleteClassUI import DeleteClassUI


class ScreenForTesting(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/homeTest.ui", self)
        self.show()
    
    

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = ScreenForTesting()
    app.exec_()