from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.uic import loadUi
from App.view.reportCardUI import ReportCardUI
from App.controller.reportController import ReportController
 
class ReportUI(QDialog):
    def __init__(self, studentId, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/report.ui", self)
        self.studentId = studentId

        if self.scrollAreaWidgetContents.layout() is None:
            self.scrollAreaWidgetContents.setLayout(QVBoxLayout())

        self.consultarReports(self.studentId)
        self.show()
 
    def listReport(self, reports):
        self.clearStackCards(self.scrollAreaWidgetContents)
        if not reports:
            self.scrollAreaWidgetContents.layout().addWidget(
                QLabel("Nenhuma ocorrência encontrada para este aluno.", alignment=Qt.AlignCenter)
            )
            return

        for report in reports:
            card = ReportCardUI(report)
            self.addCardInStackReports(card)
 
    def addCardInStackReports(self, interface):
        self.scrollAreaWidgetContents.layout().addWidget(interface)
 
    def consultarReports(self, studentId):
        reports = ReportController.getByStudentID(studentId)
        self.listReport(reports)
       
 
    def clearStackCards(self, scrollArea):
        layout = scrollArea.layout()
        if layout is None:
            return
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
 
 
 
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = ReportUI(1)
    app.exec_()