from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
class ThanhToanThanhCong(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('./view/ui/thanhToanThanhCong.ui',self)