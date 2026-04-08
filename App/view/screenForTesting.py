# File created specifically for testing all the funtionalities of view.

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.view.loginUI import LoginUI
from App.view.newReportUI import NewReportUI
from App.view.homeUI import HomeUI
from App.view.registerClassUI import RegisterClassUI
from App.view.parentEditUI import ParentEditUI
from App.view.studentEditUI import StudentEditUI
from App.view.parentInfoUI import ParentInfoUI
from App.view.studentInfoUI import StudentInfoUI
from App.view.registerEmployeeUI import RegisterEmployeeUI
from App.view.studentCardUI import StudentCardUI
from PyQt5.QtCore import QProcess

class ScreenForTesting(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/homeTest.ui", self)
        self.show()

        self.NewReport.clicked.connect(self.openScreens)
        self.StudentCard.clicked.connect(self.openScreens)
        self.RegisterEmployee.clicked.connect(self.openScreens)
        self.Login.clicked.connect(self.openScreens)
        self.Home.clicked.connect(self.openScreens)
        self.RegisterClass.clicked.connect(self.openScreens)
        self.DeleteClass.clicked.connect(self.openScreens)
        self.ParentEdit.clicked.connect(self.openScreens)
        self.StudentEdit.clicked.connect(self.openScreens)
        self.ParentInfo.clicked.connect(self.openScreens)
        self.StudentInfo.clicked.connect(self.openScreens)
        
          
    def openScreens(self):
        sender = self.sender()
        if sender == self.NewReport:
            self.newReport = NewReportUI()
            self.newReport.show()
        elif sender == self.StudentCard:
            self.studentCard = StudentCardUI()
            self.studentCard.show()
        elif sender == self.RegisterEmployee:
            self.registerEmployee = RegisterEmployeeUI()
            self.registerEmployee.show()
        elif sender == self.Login:
            self.login = LoginUI()
            self.login.show()
        elif sender == self.Home:
            self.home = HomeUI()
            self.home.show()
        elif sender == self.RegisterClass:
            self.registerClass = RegisterClassUI()
            self.registerClass.show()
        elif sender == self.ParentEdit:
            self.parentEdit = ParentEditUI()
            self.parentEdit.show()
        elif sender == self.StudentEdit:
            self.studentEdit = StudentEditUI()
            self.studentEdit.show()
        elif sender == self.ParentInfo:
            self.parentInfo = ParentInfoUI()
            self.parentInfo.show()
        elif sender == self.StudentInfo:
            self.studentInfo = StudentInfoUI()
            self.studentInfo.show()
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = ScreenForTesting()
    app.exec_()