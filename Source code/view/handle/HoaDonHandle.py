import sys
from entity import The
from datetime import datetime
from interbank.handle.Ecobikebank import EcobikeBankFrame
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDateTime,QTimer,Qt
from control.ThanhToanControl import ThanhToanControl
from utils.config import PHUONGTHUCTHANHTOAN,PHUONGTHUCTHUEXE
from view.handle.ThanhToanThanhCong import ThanhToanThanhCongDialog
# from entity.Xe import Xe
class HoaDonQWidget(QtWidgets.QWidget):
    def __init__(self,parent,hoaDon):
        super().__init__()
        # self.hoaDon=hoaDon
        self.kq=False
        self.parent=parent
        uic.loadUi("./view/ui/hoaDon.ui", self)
        for i,t in enumerate(PHUONGTHUCTHANHTOAN):
            self.comboBox_PhuongThucThanhToan.addItem(t)
        self.frameThe=EcobikeBankFrame()
        self.frame_thanhToan.layout().addWidget(self.frameThe)
        self.control=ThanhToanControl(self,hoaDon)
        self.label_MaXe.setText(str(hoaDon.xe().maXe()))
        self.label_LoaiXe.setText(hoaDon.xe().loaiXe())
        self.label_BienSoXe.setText(hoaDon.xe().bienSoXe())
        self.label_NhaXe.setText(f"{hoaDon.xe().tenNhaXe()}")
        self.label_PhuongThucThueXe.setText(PHUONGTHUCTHUEXE[hoaDon.xe().phuongThucThueXe()])
        self.showTime()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.pushButton.clicked.connect(self.thanhToan)
    def showTime(self):
        current_time=QDateTime.currentDateTime()
        label_time=current_time.toString('hh:mm dd/MM/yyyy')
        self.label_ThoiDiemGiaoDich.setText(label_time)
    def closeEvent(self, event):
        if self.kq:
            self.parent.mainWidget.control.capNhatSauKhiThanhToan()
            thanhCong=ThanhToanThanhCongDialog(self)
            thanhCong.exec()
            self.parent.clickHomeButton()
        event.accept()
        self.parent.show()
    
    def thanhToan(self):
        try:
            self.the=self.frameThe.the()
            self.control.hoaDon.setNguoiGiaoDich(self.lineEdit_NguoiGiaoDich.text())
            self.control.hoaDon.setThoiDiemGiaoDich(datetime.strptime(self.label_ThoiDiemGiaoDich.text(),'%H:%M %d/%m/%Y'))
            self.kq=self.control.thanhToan(self.the)
            self.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(str(e))
            msg.setWindowTitle('Thông báo')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
class ThongTinThemTraXeQFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/ui/thongTinThemHoaDonTraXe.ui", self)

class ThongTinThemThueXeQFrame(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/ui/thongTinThemHoaDonThueXe.ui", self)

class ThueXeHoaDonQWidget(HoaDonQWidget):
    def __init__(self ,parent,hoaDon):
        super().__init__(parent,hoaDon)
        self.label_NoiDung.setText("Thuê xe")
        self.framThongTinThem=ThongTinThemThueXeQFrame()
        self.frame_ThongTin.layout().addWidget(self.framThongTinThem)
        self.framThongTinThem.label_SoTienCoc.setText(f"{int(hoaDon.tien)} VNĐ")

    def thanhToan(self):
        self.control.hoaDon.xe().setNguoiThueXe(self.lineEdit_NguoiGiaoDich.text())
        self.control.hoaDon.xe().setThoiDiemThue(datetime.strptime(self.label_ThoiDiemGiaoDich.text(),'%H:%M %d/%m/%Y'))
        # print(datetime.strptime(self.label_ThoiDiemGiaoDich.text(),'%H:%M %d/%m/%Y'))
        # print(self.control.hoaDon.xe().thoiDiemThueXe())
        if self.control.checkTheDaDung(self.frameThe.lineEdit_MaThe.text()):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Thẻ đã được dùng để thuê xe khác")
            msg.setWindowTitle('Thông báo')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            return
        else:
            self.control.hoaDon.xe().setMaThe(self.frameThe.lineEdit_MaThe.text())
        super().thanhToan()

class TraXeHoaDonQWidget(HoaDonQWidget):
    def __init__(self,parent,hoaDon):
        super().__init__(parent,hoaDon)
        self.label_NoiDung.setText("Trả xe")
        self.framThongTinThem=ThongTinThemTraXeQFrame()
        self.frame_ThongTin.layout().addWidget(self.framThongTinThem)
        self.framThongTinThem.label_ThoiDiemThue.setText(hoaDon.xe().thoiDiemThueXe().strftime('%H:%M %d/%m/%Y'))
        self.framThongTinThem.label_ThoiDiemTraXe.setText(hoaDon.xe().thoiDiemNhanXe().strftime('%H:%M %d/%m/%Y'))
        self.framThongTinThem.label_TienCoc.setText(f"{int(hoaDon.tienCoc)} VNĐ")
        self.framThongTinThem.label_NhaXeChoThue.setText(hoaDon.xe().noiThueXe())
        self.framThongTinThem.label_SoTienThue.setText(f"{int(hoaDon.tienThue)} VNĐ")
        if hoaDon.tien>0:
            self.framThongTinThem.label_SoTienCanTra.setText(f"{int(hoaDon.tien)} VNĐ")
        else:
            self.framThongTinThem.label_SoTienHoanTra.setText(f"{int(-hoaDon.tien)} VNĐ")
        self.frameThe.lineEdit_MaThe.setText(hoaDon.xe().maThe())
        self.frameThe.lineEdit_MaThe.setReadOnly(True)
        self.lineEdit_NguoiGiaoDich.setText(hoaDon.xe().nguoiThueXe())
    def thanhToan(self):
        self.control.hoaDon.xe().setThoiDiemNhanXe(datetime.strptime(self.label_ThoiDiemGiaoDich.text(),'%H:%M %d/%m/%Y'))
        super().thanhToan()

        
# if __name__ == "__main__":
#     MainApp = QtWidgets.QApplication(sys.argv)
#     App = ThueXeHoaDonQWidget()
#     App.show()
# #     App.grab().save("../Capstone_TKXDPM.20221_Group8/Thiết kế giao diện/Hóa đơn.png")

# #     # print(App.__dict__)
#     sys.exit(MainApp.exec_())
