from PyQt5.QtCore import pyqtSignal, QThread

class Trabalhador(QThread):
    finalizado = pyqtSignal(object)

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def run(self):
        resultado = self.callback()
        self.finalizado.emit(resultado) 