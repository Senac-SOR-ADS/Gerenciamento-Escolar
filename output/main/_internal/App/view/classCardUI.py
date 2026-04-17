from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot , pyqtSignal
from PyQt5.uic import loadUi
from App.model.roomModel import Room


class ClassCardUI(QDialog):

    signal_idDaTurma = pyqtSignal(object)

    def __init__(self, turma, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/classCard.ui", self)
        self.turm = turma
        self.turma.setText(self.turm.turmas)
        self.turma.clicked.connect(self.mostrar_id)

    def mostrar_id(self):
        print(self.turm.id)
        self.signal_idDaTurma.emit(self.turm.id)

if __name__ == "__main__":
    turmas = Room.getByYear("2026")
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    card = ClassCardUI(turmas[0])
    card.show()
    app.exec_()