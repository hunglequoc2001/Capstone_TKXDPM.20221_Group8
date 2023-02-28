from entity.Xe import Xe
from connect_database.ConnectMySQL import ConnectDatabase
from utils.config import DB_NAME
class XeDien(Xe):
    def __init__(self,maXe):
        super().__init__(maXe=maXe)
        conn=ConnectDatabase(database=DB_NAME)
        x=conn.select(f"SELECT luongPin FROM xe_dien WHERE maXe={self.maXe()}")
        self.__luongPin=x[0][0]
    def luongPin(self):
        return self.__luongPin