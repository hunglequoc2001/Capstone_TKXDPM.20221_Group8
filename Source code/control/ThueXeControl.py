from control.MaVachControl import MaVachControl
from view.handle import HoaDonHandle
from entity.HoaDon import HoaDon
class ThueXeControl(MaVachControl):
    def __init__(self, view):
        super().__init__(view)
    
    def timXe(self,maVach):
        super().timXe(maVach)
        if not self.xe.kiemTraXeTrongNhaXe():
            raise Exception("Xe đã được thuê.\n Vui lòng chọn xe khác")
        if self.xe.kiemTraXeDangDuocThue():
            raise Exception("Xe bạn chọn đang trong quá trình trả xe.\nVui lòng chờ người thuê xe cũ hoàn tất thủ tục hoặc chọn xe khác")
        self.view.loadThongTin(
            maXe=self.xe.maXe(),
            loaiXe=self.xe.loaiXe(),
            bienSoXe=self.xe.bienSoXe(),
            giaCoc=self.tienCoc,
            luongPin=self.xe.luongPin())

    def thueXe(self):
        self.xe.setPhuongThucThueXe(self.view.radioButtonGroup.checkedId())
        self.hoaDon=HoaDon(self.xe,"thuê xe",[self.tienCoc])
        self.hoaDonQWidget=HoaDonHandle.ThueXeHoaDonQWidget(parent=self.view.parent,hoaDon=self.hoaDon)
        self.view.parent.hide()
        self.hoaDonQWidget.show()
        pass

    def capNhatSauKhiThanhToan(self,the):
        self.connect.idu(f'DELETE FROM xe_trong_nha_xe WHERE maXe={self.xe.maXe()}')
        self.connect.idu(f"INSERT INTO xe_dang_duoc_thue(maXe,maThe,nguoiThueXe,phuongThucThueXe,thoiDiemThue,noiThueXe) VALUES ({self.xe.maXe()},'{the.maThe()}','{self.xe.nguoiThueXe()}',{self.xe.phuongThucThueXe()},'{self.xe.thoiDiemThueXe().strftime('%Y-%m-%d %H:%M:%S')}',{self.xe.maNhaXe()})")
        self.connect.idu(f"INSERT INTO hoa_don(nguoiGiaoDich, maThe, maXe, noiDung, maNhaXe, thoiDiemGiaoDich, soTienThanhToan, phuongThucThanhToan) VALUES ('{self.xe.nguoiThueXe()}','{the.maThe()}',{self.xe.maXe()},'thuê xe',{self.xe.maNhaXe()},'{self.xe.thoiDiemThueXe().strftime('%Y-%m-%d %H:%M:%S')}',{self.tienCoc},'{the.nganHang}')")