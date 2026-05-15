from PyQt5.QtWidgets import QDialog, QComboBox
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.uic import loadUi
from App.controller.roomController import RoomController
from App.view.classCardUI import ClassCardUI



class transferRoomUI(QDialog):
    def __init__(self, roomID,**kwargs):
        super().__init__(**kwargs)
        loadUi("App/view/ui/transferRoom.ui", self)

        self.roomID = roomID
        self.listRoom = RoomController.getRoomByYear(2026)
        self.populateComboBox()
        self.show()
    
    def populateComboBox(self):
        try:
            for room in self.listRoom:
                self.comboBox.addItem(room.turmas)
                self.transferCombo.addItem(room.turmas)
        except Exception as e:
            print(f"{e}")
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    login = transferRoomUI(roomID=6)
    app.exec_()
