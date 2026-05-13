from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QPushButton , QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from App.controller.userController import UserController

class adminUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("App/view/ui/adminScreen.ui", self)

        dados = UserController.findUserActive()
        self.setValuesOnTable(dados)

        self.show()

    def setValuesOnTable(self, values):
        self.tableWidget.setRowCount(len(values)) 
        for i, v in enumerate(values):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(v.name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(v.email)))
 
            btn = QPushButton("Excluir")
            # btn.clicked.connect(lambda _, id=v.id: self.btn_act(id))
            self.tableWidget.setCellWidget(i, 2, btn)

    # def btn_act(self, id):
    #     print(f'Excluir ID: {id}')

    @pyqtSlot()
    def on_salvar_clicked(self):
        name = self.name.text()
        email = self.email.text()
        password = self.senha.text()
        confirmarSenha = self.confirmarSenha.text()
        type = self.typeUser.currentText()
        resp = UserController.createUser({
                "name": name,
                "email": email,
                "password": password,
                "type": type
            })
        if confirmarSenha != password:
                self.label1.setText("As senhas não coincidem!")
                return  

        if resp:
            self.label1.setText("Usuário criado com sucesso!")

            self.name.setText("")
            self.email.setText("")
            self.senha.setText("")
            self.confirmarSenha.setText("")

            dados = UserController.findUserActive()
            self.setValuesOnTable(dados)

        else: 
            self.label1.setText("Senhas não condizem!")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    admin = adminUI()
    app.exec_()