from control.phuongThucThueXe.TinhTienThueXe import TinhTienThueXe

class BinhThuong(TinhTienThueXe):
    def tinhTien(self, thoiDiemDau, thoiDiemCuoi, k=1):    
        count = thoiDiemCuoi - thoiDiemDau
        count = count.days*24 * 60 +  int(  count.seconds / 60  )
        if count <= 10 :
            return 0
        elif count <= 30 :
            return 10000 * k
        else :
            return (10000 + ( int((count - 30 - 1 ) / 15) + 1 )  * 3000 ) * k