class The():
    def __init__(self,thongTinDict,nganHang='EcobikeBank'):
        self.__maThe=thongTinDict["mã thẻ"]
        self.__maBaoMat=thongTinDict["mã bảo mật"]
        self.nganHang=nganHang
        try:
            self.__chuThe=thongTinDict["chủ thẻ"]
        except:
            self.__chuThe=""
        try:
            self.__ngayHetHan=thongTinDict["ngày hết hạn"]
        except:
            self.__ngayHetHan=(1,0)
    @property
    def maThe(self):
        return self.__maThe
    @property
    def maBaoMat(self):
        return self.__maBaoMat
    @property
    def chuThe(self):
        return self.__chuThe
    @property
    def ngayHetHan(self):
        return self.__ngayHetHan