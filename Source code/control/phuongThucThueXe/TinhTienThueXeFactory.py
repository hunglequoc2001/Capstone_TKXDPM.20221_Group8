from control.phuongThucThueXe import BinhThuong,Goi24h

def getTinhTienThueXe(phuongThuc):
    if phuongThuc=="Bình thường":
        return BinhThuong.BinhThuong()
    elif phuongThuc=="Gói 24h":
        return Goi24h.Goi24h()
    else:
        raise Exception("Không tìm thấy phương thức tính tiền")
    

