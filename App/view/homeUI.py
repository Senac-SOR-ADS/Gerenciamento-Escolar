from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu, QPushButton, QPushButton, QWidget, QVBoxLayout, QLabel, QMainWindow, QAction, QScrollArea
from PyQt5.QtCore import Qt, pyqtSlot, QPoint
from PyQt5.uic import loadUi
from App.controller.roomController import RoomController
from App.view.classCardUI import ClassCardUI
from App.view.registerClassUI import RegisterClassUI
from App.controller.loginController import logout
from App.view.registerStudentUI import RegisterStudentUI
from App.view.registerEmployeeUI import RegisterEmployeeUI
from App.controller.studentController import StudentController
from App.view.studentCardUI import StudentCardUI

class HomeUI(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/home.ui", self)
        self.show()
        
        
        self.menuOpt = QMenu(self)
        self.createMenu()
        self.btnOptions.clicked.connect(self.showMenu)
        
        
        self.consultarTurmas()
        self.show()
    
    def createMenu(self):
        # can't click on other screens when menu is open, being necessary to click on the menu to close it before clicking on the screen
        action = [
            ("Nova turma", lambda : self.callEvent(RegisterClassUI, parent=self)),
            ("Cadatrar aluno", lambda : self.callEvent(RegisterStudentUI, parent=self)),
            ("Cadastrar funcionário", lambda : self.callEvent(RegisterEmployeeUI, parent=self)),
        ]
        
        for texto, funcao in action:
            event = QAction(texto, self)
            event.triggered.connect(funcao)
            self.menuOpt.addAction(event)
            
    def callEvent(self, event, **kwargs):
        self.evento = event(**kwargs)
        self.evento.signal_IdRoom.connect(self.consultarTurmas)
        self.evento.exec_()
            
    def showMenu(self):
        self.menuOpt.exec_(self.btnOptions.mapToGlobal(QPoint(0, self.btnOptions.height())))
        self.menuOpt.show()

        
    def consultarTurmas(self):
        self.clearStackCards(self.scrollAreaWidgetContents_2)
        todas_turmas = RoomController.getRoomByYear(2026)
        for i in todas_turmas:
            card = ClassCardUI(i)
            card.signal_idDaTurma.connect(self.consultarAlunos)
            self.addCardInStackTurmas(card)
    
    def consultarAlunos(self, idTurma):
        self.clearStackCards(self.scrollAreaWidgetContentAlunos)
        alunos = StudentController.getByRoomID(idTurma)

        try:
            for i in alunos:
                card = StudentCardUI(i)
                self.addCardInStackStudents(card)
        except Exception as e:
            self.scrollAreaWidgetContentAlunos.layout().addWidget(QLabel("Nenhum aluno encontrado nessa turma."))
                    
    def addCardInStackTurmas(self, interface):
        self.scrollAreaWidgetContents_2.layout().addWidget(interface)
    
    def addCardInStackStudents(self, interface):
        self.scrollAreaWidgetContentAlunos.layout().addWidget(interface)
    
    def clearStackCards(self, scrollArea):
        layout = scrollArea.layout()
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    home = HomeUI()
    app.exec_()