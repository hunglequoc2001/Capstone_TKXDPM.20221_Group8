from control.phuongThucThueXe import BinhThuong,Goi24h

def getTinhTienThueXe(i):
    
    if i==0:
        tinhTien= BinhThuong.BinhThuong()
    elif i==1:
        tinhTien= Goi24h.Goi24h()
    else:
        raise Exception("Không tìm thấy phương thức tính tiền")
    return tinhTien

