from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.uic import loadUi

class NewReportUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/newReport.ui", self)
        self.show()
        
        self.dataOcorrencia.setCalendarPopup(True)
        self.dataOcorrencia.setDate(QDate.currentDate())
        self.btnSaveReport.clicked.connect(self.getText)
    
    def getText(self):
        info = []
        desc = self.descricaoOcorrencia.text()
        resp = self.responsavelCombo.currentText()
        name = self.nomeOcorrencia.text()
        date = self.dataOcorrencia.text()
        
        info = desc, resp, name, date
        print(info)
        
        return info   
    

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = NewReportUI()
    app.exec_()