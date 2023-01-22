from control.MaVachControl import MaVachControl
from datetime import datetime
from view.handle import HoaDonHandle
from utils.config import PHUONGTHUCTHUEXE,K
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
            self.view.pushButtonTinhTien.hide()
        else:
            self.view.labelNoiTraXe.hide()
            self.view.pushButtonTraXe.hide()
            self.view.label_noiTraXe.hide()
            self.dateTime=datetime.now()
        self.view.dateTimeEdit.setDateTime(self.dateTime,)
        self.tienThue=self.tinhTien.tinhTien(thoiDiemDau=self.xe.thoiDiemThueXe(),thoiDiemCuoi=self.dateTime,k=K[self.xe.loaiXe().lower()])
        self.view.capNhatThongTinTien(tienThue=self.tienThue,tienCoc=self.tienCoc)

    def traXe(self):
        self.hoaDonQWidget=HoaDonHandle.TraXeHoaDonQWidget(self.view.parent)
        self.view.parent.hide()
        self.hoaDonQWidget.show()

    def tinhTien(self):
        pass