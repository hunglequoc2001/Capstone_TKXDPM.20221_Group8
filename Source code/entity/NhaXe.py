from connect_database.ConnectMySQL import ConnectDatabase
from utils.config import DB_NAME
class NhaXe():
    def __init__(self,maNhaXe) :
        conn=ConnectDatabase(database=DB_NAME)
        self.__maNhaXe=maNhaXe
        x=conn.select(f'SELECT tenNhaXe,sucChua,diaChi,soDienThoai,mail FROM nha_xe WHERE maNhaXe={maNhaXe}')
        if x:
            self.__tenNhaXe=x[0][0]
            self.__sucChua=x[0][1]
            self.__diaChi=x[0][2]
            self.__soDienThoai=x[0][3]
            self.__mail=x[0][4]
        else:
            raise Exception(f'NhaXe có maNhaXe={maNhaXe} không tồn tại')
        
        self.__danhSachXe=[(x[0],x[1]) for x in conn.select(f'SELECT maXe,viTri FROM xe_trong_nha_xe WHERE maNhaXe={maNhaXe}')]
    def getTableRow(self):
        return {"Tên nhà xe":self.__tenNhaXe,
                "Số xe":len(self.__danhSachXe),
                "Số chỗ trống":self.__sucChua - len(self.__danhSachXe),
                "Địa chỉ":self.__diaChi
                }
    def getThongTinNhaXe(self):
        return {
            "Tên nhà xe":self.__tenNhaXe,
            "Địa chỉ":self.__diaChi,
            "Mail":self.__mail,
            "Số điện thoại":self.__soDienThoai
        }
    def getThongKeXe(self):
        conn=ConnectDatabase(database=DB_NAME)
        x=conn.select(f'SELECT xe.loaiXe,COUNT(xe.loaiXe)\
                        \nFROM xe_trong_nha_xe JOIN xe ON xe_trong_nha_xe.maXe=xe.maXe\
                        \nWHERE maNhaXe = {self.__maNhaXe}\
                        \nGROUP BY xe.loaiXe')
        return {i[0]:i[1] for i in x}

    def getDanhSachXe(self):
        return self.__danhSachXe