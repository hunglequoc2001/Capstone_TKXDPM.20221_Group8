from interbank.Interbank import EcobikeBank
from utils import config
class InterbankInterface():
    def __init__(self,the):
        self.__the=the
        pass

    def thanhToan(self,noiDung,tien,thoiDiemGiaoDich):
        bank=EcobikeBank(config.interbank_url)
        bank.interbankPayment(self.__the.maThe(),self.__the.chuThe(),self.__the.maBaoMat(),"{:02d}{:02d}".format(self.__the.ngayHetHan()[0],self.__the.ngayHetHan()[1]),"pay",noiDung,tien,thoiDiemGiaoDich.strftime("%Y-%m-%d %H:%M:%S"))


    def hoanTien(self,noiDung,tien,thoiDiemGiaoDich):
        bank=EcobikeBank(config.interbank_url)
        bank.interbankPayment(self.__the.maThe(),self.__the.chuThe(),self.__the.maBaoMat(),"{:02d}{:02d}".format(self.__the.ngayHetHan()[0],self.__the.ngayHetHan()[1]),"refund",noiDung,tien,thoiDiemGiaoDich.strftime("%Y-%m-%d %H:%M:%S"))