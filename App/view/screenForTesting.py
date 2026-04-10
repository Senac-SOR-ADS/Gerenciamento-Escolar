# File created specifically for testing all the funtionalities of view.

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea
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
from App.view.classCardUI import ClassCardUI
from App.controller.roomController import RoomController
from PyQt5.QtCore import QProcess

class ScreenForTesting(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/homeTest.ui", self)
        self.stackAlunos.setCurrentWidget(self.page_7)
        self.page7Layout = QVBoxLayout(self.page_7)
        self.page7Layout.setContentsMargins(0, 0, 0, 0)

        self.cardScrollArea = QScrollArea(self.page_7)
        self.cardScrollArea.setWidgetResizable(True)
        self.cardScrollArea.setFrameShape(QScrollArea.NoFrame)

        self.cardContainer = QWidget()
        self.cardsLayout = QVBoxLayout(self.cardContainer)
        self.cardsLayout.setContentsMargins(0, 0, 0, 0)
        self.cardsLayout.setSpacing(12)
        self.cardsLayout.addStretch()
        self.cardScrollArea.setWidget(self.cardContainer)
        self.page7Layout.addWidget(self.cardScrollArea)
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
        self.btnAddCard.clicked.connect(lambda: self.addCardInStack(StudentCardUI()))
        self.btnCardClass.clicked.connect(lambda: self.addCardInStackTurmas(ClassCardUI()))

        self.consultarTurmas()
        
    def consultarTurmas(self):
        todas_turmas = RoomController.getRoomByYear(2026)
        for i in todas_turmas:
            self.addCardInStackTurmas(ClassCardUI(i))



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
    
    def addCardInStack(self, interface):
        self.cardsLayout.insertWidget(self.cardsLayout.count() - 1, interface)
        self.stackAlunos.setCurrentWidget(self.page_7)
    
    def addCardInStackTurmas(self, interface):
        self.scrollAreaWidgetContents.layout().addWidget(interface)
        
        
        
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = ScreenForTesting()
    app.exec_()