from control.MaVachControl import MaVachControl
from datetime import datetime
from view.handle import HoaDonHandle
from utils.config import PHUONGTHUCTHUEXE,K
from entity.HoaDon import HoaDon
from entity.NhaXe import NhaXe
from control.phuongThucThueXe import TinhTienThueXeFactory
from PyQt5 import QtWidgets
class TraXeControl(MaVachControl):
    def __init__(self, view):
        super().__init__(view)
    
    def timXe(self,maVach):
        super().timXe(maVach)
        if not self.xe.kiemTraXeDangDuocThue(conn=self.connect):
            raise Exception('Xe không được thuê')
        self.view.loadThongTin(
            maXe=self.xe.maXe(),
            nguoiThueXe=self.xe.nguoiThueXe(),
            bienSoXe=self.xe.bienSoXe(),
            giaCoc=self.tienCoc,
            loaiXe=self.xe.loaiXe(),
            phuongThucThueXe=PHUONGTHUCTHUEXE[self.xe.phuongThucThueXe()],
            thoiDiemThue=self.xe.thoiDiemThueXe()
        )
        self.tinhTien=TinhTienThueXeFactory.getTinhTienThueXe(self.xe.phuongThucThueXe())
        self.dateTime=datetime.now()
        self.view.dateTimeEdit.setDateTime(self.dateTime)
        self.tienThue=self.tinhTien.tinhTien(thoiDiemDau=self.xe.thoiDiemThueXe(),thoiDiemCuoi=self.dateTime,k=K[self.xe.loaiXe().lower()])
        self.view.capNhatThongTinTien(tienThue=self.tienThue,tienCoc=self.tienCoc)

    def traXe(self):
        maNhaXe=self.view.lineEdit_maNhaXe.text()
        if maNhaXe=='':
            Exception("Vui lòng nhập mã nhà xe")
        if not maNhaXe.isnumeric():
            Exception("Bạn nhập sai cú pháp mã nhà xe")
        else:
            maNhaXe=int(maNhaXe)
        nhaXe=NhaXe(maNhaXe)
        maNhaXe=self.view.lineEdit_maNhaXe.text()
        nhaXe=NhaXe(maNhaXe)
        viTri=self.view.lineEdit_viTri.text()
        if maNhaXe=='':
            Exception("Vui lòng nhập vị trí trả xe")
        self.dateTime=datetime.now()
        self.xe.setThongTinTraXe(maNhaXe,viTri,self.dateTime)
        self.tienThue=self.tinhTien.tinhTien(thoiDiemDau=self.xe.thoiDiemThueXe(),thoiDiemCuoi=self.dateTime,k=K[self.xe.loaiXe().lower()])
        self.hoaDon=HoaDon(self.xe,"trả xe",[self.tienCoc,self.tienThue])
        self.hoaDonQWidget=HoaDonHandle.TraXeHoaDonQWidget(parent=self.view.parent,hoaDon=self.hoaDon)
        self.view.parent.hide()
        self.hoaDonQWidget.show()
        

    def tinhTien(self):
        self.dateTime=self.view.dateTimeEdit.dateTime().toPyDateTime()
        self.tienThue=self.tinhTien.tinhTien(thoiDiemDau=self.xe.thoiDiemThueXe(),thoiDiemCuoi=self.dateTime,k=K[self.xe.loaiXe().lower()])
        self.view.capNhatThongTinTien(tienThue=self.tienThue,tienCoc=self.tienCoc)
        pass

    def capNhatSauKhiThanhToan(self):
        self.xe.capNhatThongTinTraXe(self.connect)