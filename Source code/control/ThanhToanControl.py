from control.BaseControl import BaseControl
from datetime import datetime
from interbank.InterbankInterface import InterbankInterface
class ThanhToanControl(BaseControl):
    def __init__(self, view,hoaDon):
        super().__init__(view)
        self.hoaDon=hoaDon
    def checkTheDaDung(self,maThe):
        if self.connect.select(f"SELECT * FROM xe_dang_duoc_thue WHERE maThe='{maThe}'"):
            return True
        else:
            return False

    def thanhToan(self,the):
        interbank=InterbankInterface(the)
        if self.hoaDon.tien>0:
            # Thanh toán
            noiDung=f'Thanh toán {self.view.label_NoiDung.text()}'
            interbank.thanhToan(noiDung,self.hoaDon.tien,self.hoaDon.thoiDiemGiaoDich())
        elif self.hoaDon.tien<0:
            # Hoàn tiền
            noiDung=f'Hoàn tiền {self.view.label_NoiDung.text()}'
            interbank.hoanTien(noiDung,self.hoaDon.tien,self.hoaDon.thoiDiemGiaoDich())
        # now=datetime.now()
        self.hoaDon.luuHoaDon(the,noiDung,self.connect)
        return True