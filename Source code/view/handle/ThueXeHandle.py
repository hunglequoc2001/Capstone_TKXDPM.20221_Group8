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
        
    def loadThongTin(self,maXe,loaiXe,bienSoXe,giaCoc,luongPin):
        self.label_maXe.setText(f"{maXe}")
        self.label_bienSoXe.setText(bienSoXe)
        self.label_giaCoc.setText(f"{int(giaCoc)} VNĐ")
        self.label_loaiXe.setText(loaiXe)
        self.label_luongPin.setText(f"{luongPin}")

    def timXe(self):
        try:
            maVach=self.lineEdit_maVach.text()
            self.control.timXe(maVach)
            self.frameThueXe.show()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(str(e))
            msg.setWindowTitle('Thông báo')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
        
    def thueXe(self):
        self.control.thueXe()
        return