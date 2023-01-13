from control.MaVachControl import MaVachControl
from view.handle import HoaDonHandle
class ThueXeControl(MaVachControl):
    def __init__(self, view):
        super().__init__(view)
    
    def timXe(self,maVach):
        super().timXe(maVach)
    
    def thueXe(self):
        self.hoaDonQWidget=HoaDonHandle.ThueXeHoaDonQWidget(self.view.parent)
        self.view.parent.hide()
        self.hoaDonQWidget.show()

        pass