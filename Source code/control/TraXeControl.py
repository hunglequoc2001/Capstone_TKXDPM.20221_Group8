from control.MaVachControl import MaVachControl
from view.handle import HoaDonHandle
class TraXeControl(MaVachControl):
    def __init__(self, view):
        super().__init__(view)
    
    def timXe(maVach):
        super().timXe(maVach)
        
    def traXe(self):
        self.hoaDonQWidget=HoaDonHandle.TraXeHoaDonQWidget(self.view.parent)
        self.view.parent.hide()
        self.hoaDonQWidget.show()

    def tinhTien(self):
        pass