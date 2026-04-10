from PyQt5.QtCore import pyqtSignal, QThread

class Trabalhador(QThread):
    finalizado = pyqtSignal(object)

    def __init__(self, callback, *args, **kwargs):
        super().__init__()
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def run(self):
        resultado = self.callback(*self.args, **self.kwargs)
        self.finalizado.emit(resultado)
