from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton , QApplication
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.uic import loadUi
from App.model.parentModel import Parent
 
class ParentActionsUI(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/parentActions.ui", self)
 
        dados = Parent.getAll()
        self.setValuesOnTable(dados)
   
    def setValuesOnTable(self, values):
        self.tableWidget.setRowCount(len(values)) # definir quantidade de itens
        for i, v in enumerate(values):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(v.name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(v.legal_guardian)))
 
            btn = QPushButton("Excluir")
            btn.clicked.connect(lambda _, id=v.id: self.btn_act(id))
            self.tableWidget.setCellWidget(i, 2, btn)
 
 
    def btn_act(self, idParent):
        print(f'Excluir ID: {idParent}')


if __name__ == "__main__":
    app = QApplication([])
    window = ParentActionsUI()
    window.show()
    app.exec_()