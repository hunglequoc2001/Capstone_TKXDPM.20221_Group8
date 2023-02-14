class HoaDon():
    def __init__(self,xe,noiDung,tien):
        self.__xe=xe
        self.__noiDung=noiDung
        if len(tien)==1:
            self.tien=tien[0]
        elif len(tien)==2:
            self.tienCoc=tien[0]
            self.tienThue=tien[1]
            self.tien=self.tienThue-self.tienCoc
        else:
            raise Exception("Tham số tien ko hợp lệ")
    def xe(self):
        return self.__xe
    def noiDung(self):
        return self.__noiDung
    def setNguoiGiaoDich(self,nguoiGiaoDich):
        self.__nguoiGiaoDich=nguoiGiaoDich
    def nguoiGiaoDich(self):
        return self.__nguoiGiaoDich
    def setThoiDiemGiaoDich(self,thoiDiemGiaoDich):
        self.__thoiDiemGiaoDich=thoiDiemGiaoDich
    def thoiDiemGiaoDich(self):
        return self.__thoiDiemGiaoDich
    def luuHoaDon(self,the,noiDung,connectDB):
        # print("OK")
        connectDB.idu(f"INSERT INTO hoa_don(nguoiGiaoDich, maThe, maXe, noiDung, maNhaXe, thoiDiemGiaoDich, soTienThanhToan, phuongThucThanhToan) VALUES ('{self.__nguoiGiaoDich}','{the.maThe()}',{self.__xe.maXe()},'{noiDung}',{self.__xe.maNhaXe()},'{self.__thoiDiemGiaoDich.strftime('%Y-%m-%d %H:%M:%S')}',{self.tien},'{the.nganHang}')")
