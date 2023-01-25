from control.BaseControl import BaseControl

class ThanhToanControl(BaseControl):
    def __init__(self, view,hoaDon):
        super().__init__(view)
        self.hoaDon=hoaDon
    
    def thanhToan(self,the):
        
        if self.hoaDon.tien>0:
            # Thanh toán
            maBaoMat=self.view.frameThe.lineEdit_MaBaoMat.text()
            noiDung=f'Thanh toán {self.view.label_NoiDung.text()}'
        elif self.hoaDon.tien<0:
            # Hoàn tiền
            noiDung=f'Hoàn tiền {self.view.label_NoiDung.text()}'
        

        return True