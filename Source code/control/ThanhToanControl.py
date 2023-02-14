from control.BaseControl import BaseControl
from utils import config
from datetime import datetime
from interbank.Interbank import Interbank
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
        if self.checkTheDaDung(the.maThe()):
            raise Exception("Thẻ của bạn đã được dùng")
        if self.hoaDon.tien>0:
            # Thanh toán
            tien=self.hoaDon.tien
            command='pay'
            noiDung=f'Thanh toán {self.view.label_NoiDung.text()}'
            #Thêm code
        elif self.hoaDon.tien<0:
            # Hoàn tiền
            tien=-self.hoaDon.tien
            command='refund'
            noiDung=f'Hoàn tiền {self.view.label_NoiDung.text()}'
            #Thêm code
        now=datetime.now()
        bank=Interbank(config.interbank_url)
        bank.interbankPayment(the.maThe(),the.chuThe(),the.maBaoMat(),"{:02d}{:02d}".format(the.ngayHetHan()[0],the.ngayHetHan()[1]),command,noiDung,tien,self.hoaDon.thoiDiemGiaoDich().strftime("%Y-%m-%d %H:%M:%S"))
        self.hoaDon.luuHoaDon(the,noiDung,self.connect)
        return True