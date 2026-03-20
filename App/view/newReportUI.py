from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class NewReportUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/newReport.ui", self)
        self.show()
        
        self.btnSaveReport.clicked.connect(self.getDescriptionText)
    
    def getDescriptionText(self):
        report = self.descricaoOcorrencia.text()
        print(report)
        
        return report
        
    
    

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = NewReportUI()
    app.exec_()