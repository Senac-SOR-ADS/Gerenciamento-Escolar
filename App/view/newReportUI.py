from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.uic import loadUi
from App.controller.reportController import ReportController as rc


class NewReportUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/newReport.ui", self)
        self.show()
        
        self.dataOcorrencia.setCalendarPopup(True)
        self.dataOcorrencia.setDate(QDate.currentDate())
        self.btnSaveReport.clicked.connect(lambda: self.sendReport(self.getInfo()))
    
    def getInfo(self):
        info = []
        desc = self.descricaoOcorrencia.text()
        resp = self.responsavelCombo.currentText()
        name = self.nomeOcorrencia.text()
        date = self.dataOcorrencia.text()
        
        info = desc, resp, name, date
        print(info[0])
        
        return info
    
    def sendReport(self, info):
        try:
            rc.create(info[0], 1, 1)
        except Exception as e:
            print(f"Erro ao criar o relatório! {e}")
    
    

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = NewReportUI()
    app.exec_()