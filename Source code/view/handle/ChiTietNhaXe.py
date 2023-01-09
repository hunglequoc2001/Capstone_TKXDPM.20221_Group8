from PyQt5 import QtWidgets, uic
class ChiTietNhaXeQWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/ui/chiTietNhaXe.ui", self)