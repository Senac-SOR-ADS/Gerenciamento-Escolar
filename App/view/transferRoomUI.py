from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QApplication
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from App.controller.roomController import RoomController
from App.controller.studentController import StudentController
import sys

class transferRoomUI(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/transferRoom.ui", self)

        self.listRoom = RoomController.getRoomByYear(2026)
        self.populateComboBox()
        self.consultarAlunos(self.listRoom[0].id)
        self.btnConfir.clicked.connect(self.transfer)
        self.comboBox.currentIndexChanged.connect(self.alterarSala)
        self.show()
    
    def alterarSala(self, indice):
        self.consultarAlunos(self.listRoom[indice].id)

    
    def populateComboBox(self):
        try:
            for room in self.listRoom:
                self.comboBox.addItem(room.turmas)
                self.transferCombo.addItem(room.turmas)
        except Exception as e:
            print(f"Error populating combo boxes: {e}")

    def consultarAlunos(self, idTurma):
        try:
            self.alunos = StudentController.getByRoomID(idTurma) 
            self.setValuesOnTable(self.alunos)
        except Exception as e:
            print(f"Error fetching students: {e}")
            
    def setValuesOnTable(self, students):
        self.tableWidgetRooms.setRowCount(len(students)) 
        
        for i, student in enumerate(students):
            self.tableWidgetRooms.setItem(i, 0, QTableWidgetItem(student.nome))
            self.tableWidgetRooms.setItem(i, 1, QTableWidgetItem(str(student.RA)))
            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            checkbox_item.setCheckState(Qt.Unchecked) 
            self.tableWidgetRooms.setItem(i, 2, checkbox_item)

    def transfer(self):
        try:
            nova_sala = self.getNextRoom()
            alunos_para_transferir = self.getSelectedStudents()
            #chamar o novo metodo
            #strudentController.metodo(alunos_para_transferir, nova_sala.id)

        except Exception as e:
            print(f"Error during transfer: {e}")
    
    def getNextRoom(self):
        index = self.transferCombo.currentIndex()
        return self.listRoom[index]
    
    def getSelectedStudents(self):
        alunos_para_transferir = []
        for row in range(self.tableWidgetRooms.rowCount()):
            item = self.tableWidgetRooms.item(row, 2) 
            
            if item and item.checkState() == Qt.Checked:
                aluno = self.alunos[row]
                alunos_para_transferir.append(aluno)
        return alunos_para_transferir
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = transferRoomUI()
    sys.exit(app.exec_())