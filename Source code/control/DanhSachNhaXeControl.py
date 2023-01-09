from control.BaseControl import BaseControl
class DanhSachNhaXeControl(BaseControl):
    def __init__(self, view):
        super().__init__(view)

    def chiTietNhaXe(self):
        return