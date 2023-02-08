from PyQt5 import QtWidgets, uic
from entity.The import The
class EcobikeBankFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi("./nganHang/ui/ecobikebank.ui", self)
        self.lineEdit_MaBaoMat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dateEdit_NgayHetHan.setDisplayFormat('MM-yy')
    def the(self):
        date=self.dateEdit_NgayHetHan.date()
        return The(maThe=self.lineEdit_MaThe.text(),
            maBaoMat=self.lineEdit_MaBaoMat.text(),
            chuThe=self.lineEdit_ChuThe.text(),
            ngayHetHan=(date.month(),date.year()%100)
        )

