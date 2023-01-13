from PyQt5 import QtWidgets, uic
from control.ThueXeControl import ThueXeControl
from utils import config
class ThueXeQWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        uic.loadUi("./view/ui/thueXe.ui", self)
        self.parent=parent
        self.control=ThueXeControl(self)
        radioButtonGroup=QtWidgets.QButtonGroup()
        self.phuongThucThueXe=[]
        for x in config.PHUONGTHUCTHUEXE:
            radioButton=QtWidgets.QRadioButton(x)
            with open(config.TOOL_TIP_PATH+f'/{x}.txt','r',encoding="UTF-8") as f:
                radioButton.setToolTip(f.read())
            self.frame_PhuongThucThueXe.layout().addWidget(radioButton)
            self.phuongThucThueXe.append(radioButton)
            radioButtonGroup.addButton(radioButton)
        self.phuongThucThueXe[0].setChecked(True)
        # radioButtonGroup.addButton(self.binhThuongButton)
        # self.binhThuongButton.setChecked(True)
        # radioButtonGroup.addButton(self.goi24hButton)
        self.pushButtonTimXe.clicked.connect(self.timXe)
        self.pushButtonThueXe.clicked.connect(self.thueXe)
        self.frameThueXe.hide()


    def timXe(self):
        self.frameThueXe.show()

    def thueXe(self):
        self.control.thueXe()
        return