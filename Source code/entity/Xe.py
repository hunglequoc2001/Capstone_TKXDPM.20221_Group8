from connect_database.ConnectMySQL import ConnectDatabase
from utils.config import DB_NAME
from entity.NhaXe import NhaXe
class Xe:
    def __init__(self,maXe):
        conn=ConnectDatabase(database=DB_NAME)
        self.__maXe=maXe
        x=conn.select(f'SELECT bienSoXe,loaiXe,hangXe,giaTriXe,luongPin FROM xe WHERE maXe={maXe}')
        if x:
            self.__bienSoXe=x[0][0]
            self.__loaiXe=x[0][1]
            self.__hangXe=x[0][2]
            self.__giaTriXe=x[0][3]
            self.__luongPin=x[0][4]
        else:
            raise Exception(f'Xe có mã xe={maXe} không tồn tại')

    def getThongTinXe(self):
        return {
            'Mã xe':self.__maXe,
            'Biển số xe': self.__bienSoXe,
            'Hãng xe': self.__hangXe,
            'Loại xe':self.__loaiXe,
            'Giá trị xe':self.__giaTriXe,
            'Lượng pin': self.__luongPin
        }
    
    def kiemTraXeDangDuocThue(self,conn):
        res=conn.select(f'SELECT maThe,nguoiThueXe,phuongThucThueXe,thoiDiemThue,noiThueXe FROM xe_dang_duoc_thue WHERE maXe={self.__maXe}')
        if res:
            self.__maThe=res[0][0]
            self.__nguoiThueXe=res[0][1]
            self.__phuongThucThueXe=res[0][2]
            self.__thoiDiemThue=res[0][3]
            self.__noiThueXe=res[0][4]
            return True
        else:
            return False
    def setNguoiThueXe(self,nguoiThueXe):
        self.__nguoiThueXe=nguoiThueXe
    def kiemTraXeTrongNhaXe(self,conn):
        res=conn.select(f'SELECT maNhaXe,viTri,thoiDiemNhanXe FROM xe_trong_nha_xe WHERE maXe={self.__maXe}')
        if res:
            self.__maNhaXe=res[0][0]
            self.__viTri=res[0][1]
            self.__thoiDiemNhanXe=res[0][2]
            return True
        else:
            return False   
    def setThongTinTraXe(self,maNhaXe,viTri,thoiDiemNhanXe):
        self.__maNhaXe=maNhaXe
        self.__viTri=viTri
        self.__thoiDiemNhanXe=thoiDiemNhanXe
    def viTri(self):
        return self.__viTri
    def maNhaXe(self):
        return self.__maNhaXe
    def tenNhaXe(self):
        nhaxe=NhaXe(self.__maNhaXe)
        return nhaxe.getThongTinNhaXe()['Tên nhà xe']
    def noiThueXe(self):
        nhaxe=NhaXe(self.__noiThueXe)
        return nhaxe.getThongTinNhaXe()['Tên nhà xe']
    def maXe(self):
        return self.__maXe
    def bienSoXe(self):
        return self.__bienSoXe
    def loaiXe(self):
        return self.__loaiXe
    def giaTriXe(self):
        return self.__giaTriXe 
    def luongPin(self):
        return self.__luongPin
    def nguoiThueXe(self):
        return self.__nguoiThueXe
    def phuongThucThueXe(self):
        return self.__phuongThucThueXe
    def setPhuongThucThueXe(self,phuongThucThueXe):
        self.__phuongThucThueXe=phuongThucThueXe
    def thoiDiemThueXe(self):
        return self.__thoiDiemThue
    def setThoiDiemThue(self,thoiDiemThueXe):
        self.__thoiDiemThue=thoiDiemThueXe
        # print(self.__thoiDiemThue)
    def setThoiDiemNhanXe(self,thoiDiemNhanXe):
        self.__thoiDiemNhanXe=thoiDiemNhanXe
    def thoiDiemNhanXe(self):
        return self.__thoiDiemNhanXe
    def maThe(self):
        return self.__maThe
    def setMaThe(self,maThe):
        self.__maThe=maThe


    def capNhatThongTinThueXe(self,connectDB):
        connectDB.idu(f'DELETE FROM xe_trong_nha_xe WHERE maXe={self.__maXe}')
        connectDB.idu(f"INSERT INTO xe_dang_duoc_thue(maXe,maThe,nguoiThueXe,phuongThucThueXe,thoiDiemThue,noiThueXe) VALUES ({self.__maXe},'{self.__maThe}','{self.__nguoiThueXe}',{self.__phuongThucThueXe},'{self.thoiDiemThueXe().strftime('%Y-%m-%d %H:%M:%S')}',{self.__maNhaXe})")
    def capNhatThongTinTraXe(self,connectDB):
        connectDB.idu(f"DELETE FROM xe_dang_duoc_thue WHERE maXe={self.__maXe}")
        connectDB.idu(f"INSERT INTO xe_trong_nha_xe(maXe, maNhaXe, viTri, thoiDiemNhanXe) VALUES ({self.__maXe},{self.__maNhaXe},'{self.__viTri}','{self.__thoiDiemNhanXe.strftime('%Y-%m-%d %H:%M:%S')}')")