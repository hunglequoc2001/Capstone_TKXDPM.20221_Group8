from PyQt5 import QtWidgets, uic
from control.TraXeControl import TraXeControl
class TraXeQWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        uic.loadUi("./view/ui/traXe.ui", self)
        self.dateTimeEdit.setDisplayFormat('hh:mm dd/MM/yyyy')
        self.parent=parent
        self.control=TraXeControl(self)
        self.frameTraXe.hide()
        self.pushButtonTimXe.clicked.connect(self.timXe)
        self.pushButtonTraXe.clicked.connect(self.control.traXe)
        self.pushButtonTinhTien.clicked.connect(self.control.tinhTien)

    def loadThongTin(self,maXe,nguoiThueXe,bienSoXe,giaCoc,loaiXe,phuongThucThueXe,thoiDiemThue):
        self.label_maXe.setText(f'{maXe}')
        self.label_nguoiThueXe.setText(nguoiThueXe)
        self.label_bienSoXe.setText(bienSoXe)
        self.label_giaCoc.setText(f"{int(giaCoc)} VNĐ")
        self.label_loaiXe.setText(loaiXe)
        self.label_phuongThucThueXe.setText(phuongThucThueXe)
        self.label_thoiDiemThue.setText(thoiDiemThue.strftime('%H:%M %d/%m/%Y'))
    def capNhatThongTinTien(self,tienThue,tienCoc):
        self.label_tienThueXe.setText(f"{int(tienThue)} VNĐ")
        if tienCoc-tienThue>0:
            self.label_tienHoanTra.setText(f"{int(tienCoc-tienThue)} VNĐ")
            self.label_tienTraThem.setText("0 VNĐ")
        else:
            self.label_tienTraThem.setText(f"{int(tienThue-tienCoc)} VNĐ")
            self.label_tienHoanTra.setText("0 VNĐ")
    
    def timXe(self):
        try:
            maVach=self.lineEdit_maVach.text()
            self.control.timXe(maVach)
            self.frameTraXe.show()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(str(e))
            msg.setWindowTitle('Thông báo')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()

    # def traXe(self):
    #     self.control.traXe()
    