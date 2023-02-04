from control.phuongThucThueXe.TinhTienThueXe import TinhTienThueXe
#Chưa code
class Goi24h(TinhTienThueXe):
    def tinhTien(self, thoiDiemDau, thoiDiemCuoi, k=1):
        count = thoiDiemCuoi - thoiDiemDau
        count = count.days*24 * 60 +  int(  count.seconds / 60  )

        if count >= 1440 :
            return (200000 + (int( (count - 1 - 1440 ) / 15 ) + 1)* 2000 ) * k
        elif count >= 720 :
            return 200000 * k
        else :
            count = int( (count -1) / 60 ) + 1
            return (200000 - (12- count) * 10000 ) * k