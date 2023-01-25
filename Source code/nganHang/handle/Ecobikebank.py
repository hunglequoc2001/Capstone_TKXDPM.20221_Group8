from PyQt5 import QtWidgets, uic
class EcobikeBankFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi("./nganHang/ui/ecobikebank.ui", self)
        self.lineEdit_MaBaoMat.setEchoMode(QtWidgets.QLineEdit.Password)