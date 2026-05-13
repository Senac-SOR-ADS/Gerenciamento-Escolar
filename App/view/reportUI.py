from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from App.view.reportCardUI import ReportCardUI
from App.model.reportModel import Report

class ReportUI(QDialog):
    def __init__(self, studentId, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/report.ui", self)
        self.studentId = studentId
        self.show()

    def listReport(self, reports):
        self.clearStackCards(self.scrollAreaWidgetContents)
        try:
            for report in reports:
                card = ReportCardUI()
                self.addCardInStackReports(card)
        except Exception as e:
            pass

    def addCardInStackReports(self, interface):
        self.scrollAreaWidgetContents.layout().addWidget(interface)

    def consultarReports(self, StudentId):
        reports = Report.searchStudentID(StudentId)
        self.listReport(reports)
        

    def clearStackCards(self, scrollArea):
        layout = scrollArea.layout()
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()



if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = ReportUI(1)
    login.consultarReports(3)
    app.exec_()
