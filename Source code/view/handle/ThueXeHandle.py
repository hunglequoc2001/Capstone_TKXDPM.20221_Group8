from PyQt5 import QtWidgets, uic
from control.ThueXeControl import ThueXeControl
class ThueXeQWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        uic.loadUi("./view/ui/thueXe.ui", self)
        self.parent=parent
        self.control=ThueXeControl(self)
        radioButtonGroup=QtWidgets.QButtonGroup()
        radioButtonGroup.addButton(self.binhThuongButton)
        self.binhThuongButton.setChecked(True)
        radioButtonGroup.addButton(self.goi24hButton)
        self.pushButtonTimXe.clicked.connect(self.timXe)
        self.pushButtonThueXe.clicked.connect(self.thueXe)
        self.frameThueXe.hide()

    def timXe(self):
        self.frameThueXe.show()

    def thueXe(self):
        
        return