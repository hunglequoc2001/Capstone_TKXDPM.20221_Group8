class The():
    def __init__(self,maThe,maBaoMat,chuThe='',ngayHetHan=(1,0),nganHang='EcobikeBank'):
        self.__maThe=maThe
        self.__maBaoMat=maBaoMat
        self.nganHang=nganHang
        self.__chuThe=chuThe
        self.__ngayHetHan=ngayHetHan
    
    def maThe(self):
        return self.__maThe
    def maBaoMat(self):
        return self.__maBaoMat
    def chuThe(self):
        return self.__chuThe
    def ngayHetHan(self):
        return self.__ngayHetHan