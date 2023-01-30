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
        return The({
            "mã thẻ":self.lineEdit_MaThe.text(),
            "mã bảo mật":self.lineEdit_MaBaoMat.text(),
            "chủ thẻ":self.lineEdit_ChuThe.text(),
            "ngày hết hạn":(date.month(),date.year()%100)
        })
