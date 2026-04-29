from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot , pyqtSignal
from PyQt5.uic import loadUi
from App.model.roomModel import Room


class ClassCardUI(QDialog):

    signal_idDaTurma = pyqtSignal(object)

    def __init__(self, turmas, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/classCard.ui", self)
        self.parent = kwargs.get("parent", None)

        if self.parent:
            self.parent.signal_desmarcarTurma.connect(self.desmarcar)

        self.turm = turmas
        self.turma.setText(self.turm.turmas)
        self.turma.clicked.connect(self.idAtual)

    def idAtual(self):
        self.signal_idDaTurma.emit(self.turm.id)

    def desmarcar(self, idTurma):
        if idTurma != self.turm.id:
            self.turma.setChecked(False)

if __name__ == "__main__":
    turmas = Room.getByYear("2026")
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    card = ClassCardUI(turmas[0])
    card.show()
    app.exec_()