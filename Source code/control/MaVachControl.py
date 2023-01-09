from abc import  abstractmethod
from control.BaseControl import BaseControl
class MaVachControl(BaseControl):
    def __init__(self, view):
        super().__init__(view)
    
    @abstractmethod
    def timXe(self,maVach):
        pass

    def kiemTraMaVach(maVach):
        return False