from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
class ThanhToanThanhCongDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('./view/ui/thanhToanThanhCong.ui',self)
        self.pushButton.clicked.connect(self.close)