import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDateTime,QTimer,Qt
from control.ThanhToanControl import ThanhToanControl
class HoaDonQWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        uic.loadUi("./view/ui/hoaDon.ui", self)
        self.lineEditMaBaoMat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.control=ThanhToanControl(self)
        self.showTime()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
    def showTime(self):
        current_time=QDateTime.currentDateTime()
        label_time=current_time.toString('hh:mm dd/MM/yyyy')
        self.label_ThoiDiemGiaoDich.setText(label_time)

class ThongTinThemTraXeQFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/ui/thongTinThemHoaDonTraXe.ui", self)

class ThongTinThemThueXeQFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/ui/thongTinThemHoaDonThueXe.ui", self)

class ThueXeHoaDonQWidget(HoaDonQWidget):
    def __init__(self ,parent):
        super().__init__(parent)
        self.label_NoiDung.setText("Thuê xe")
        self.framThongTinThem=ThongTinThemThueXeQFrame()
        self.frame_ThongTin.layout().addWidget(self.framThongTinThem)

class TraXeHoaDonQWidget(HoaDonQWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.label_NoiDung.setText("Trả xe")
        self.framThongTinThem=ThongTinThemTraXeQFrame()
        self.frame_ThongTin.layout().addWidget(self.framThongTinThem)
# if __name__ == "__main__":
#     MainApp = QtWidgets.QApplication(sys.argv)
#     App = ThueXeHoaDonQWidget()
#     App.show()
# #     App.grab().save("../Capstone_TKXDPM.20221_Group8/Thiết kế giao diện/Hóa đơn.png")

# #     # print(App.__dict__)
#     sys.exit(MainApp.exec_())
