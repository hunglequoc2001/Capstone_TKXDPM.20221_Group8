from control.MaVachControl import MaVachControl
from datetime import datetime
from view.handle import HoaDonHandle
from utils.config import PHUONGTHUCTHUEXE,K
from entity.HoaDon import HoaDon
from control.phuongThucThueXe import TinhTienThueXeFactory
class TraXeControl(MaVachControl):
    def __init__(self, view):
        super().__init__(view)
    
    def timXe(self,maVach):
        super().timXe(maVach)
        if not self.xe.kiemTraXeDangDuocThue():
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
        if self.xe.kiemTraXeTrongNhaXe():
            self.dateTime=self.xe.thoiDiemNhanXe()
            self.view.dateTimeEdit.setReadOnly(True)
            self.view.pushButtonTinhTien.hide()
            self.view.labelNoiTraXe.show()
            self.view.pushButtonTraXe.show()
            self.view.label_noiTraXe.show()
            self.view.label_noiTraXe.setText(f"Nhà xe {self.xe.tenNhaXe()}")
        else:
            self.view.dateTimeEdit.setReadOnly(False)
            self.view.pushButtonTinhTien.show()
            self.view.labelNoiTraXe.hide()
            self.view.pushButtonTraXe.hide()
            self.view.label_noiTraXe.hide()
            self.dateTime=datetime.now()
        self.view.dateTimeEdit.setDateTime(self.dateTime)
        self.tienThue=self.tinhTien.tinhTien(thoiDiemDau=self.xe.thoiDiemThueXe(),thoiDiemCuoi=self.dateTime,k=K[self.xe.loaiXe().lower()])
        self.view.capNhatThongTinTien(tienThue=self.tienThue,tienCoc=self.tienCoc)

    def traXe(self):
        self.hoaDon=HoaDon(self.xe,"trả xe",[self.tienCoc,self.tienThue])
        self.hoaDonQWidget=HoaDonHandle.TraXeHoaDonQWidget(parent=self.view.parent,hoaDon=self.hoaDon)
        self.view.parent.hide()
        self.hoaDonQWidget.show()
        

    def tinhTien(self):
        self.dateTime=self.view.dateTimeEdit.dateTime().toPyDateTime()
        self.tienThue=self.tinhTien.tinhTien(thoiDiemDau=self.xe.thoiDiemThueXe(),thoiDiemCuoi=self.dateTime,k=K[self.xe.loaiXe().lower()])
        self.view.capNhatThongTinTien(tienThue=self.tienThue,tienCoc=self.tienCoc)
        pass

    def capNhatSauKhiThanhToan(self,the):
        self.connect.idu(f"DELETE FROM xe_dang_duoc_thue WHERE maXe={self.xe.maXe()}")
        self.connect.idu(f"INSERT INTO hoa_don(nguoiGiaoDich, maThe, maXe, noiDung, maNhaXe, thoiDiemGiaoDich, soTienThanhToan, phuongThucThanhToan) VALUES ('{self.hoaDon.nguoiGiaoDich()}','{the.maThe()}',{self.xe.maXe()},'trả xe',{self.xe.maNhaXe()},'{self.hoaDon.thoiDiemGiaoDich().strftime('%Y-%m-%d %H:%M:%S')}',{self.tienThue-self.tienCoc},'{the.nganHang}')")