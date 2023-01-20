from connect_database.ConnectMySQL import ConnectDatabase
from utils.config import DB_NAME
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
            raise Exception(f'Xe có maXe={maXe} không tồn tại')

    def getThongTinXe(self):
        return {
            'Mã xe':self.__maXe,
            'Biển số xe': self.__bienSoXe,
            'Hãng xe': self.__hangXe,
            'Loại xe':self.__loaiXe,
            'Giá trị xe':self.__giaTriXe,
            'Lượng pin': self.__luongPin
        }
    
    