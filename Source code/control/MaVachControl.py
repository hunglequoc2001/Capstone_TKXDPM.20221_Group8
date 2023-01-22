from abc import  abstractmethod
from control.BaseControl import BaseControl
from entity.Xe import Xe
from utils.config import heSoTienCoc
class MaVachControl(BaseControl):
    def __init__(self, view):
        super().__init__(view)
    
    @abstractmethod
    def timXe(self,maVach):
        if not self.kiemTraMaVach(maVach):
            raise Exception('Mã Vạch không hợp lệ')
        self.xe=Xe(maVach)
        self.tienCoc=self.xe.giaTriXe()*heSoTienCoc

    def kiemTraMaVach(self,maVach):
        if maVach.isnumeric():
            return True
        else:
            return False