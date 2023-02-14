from control.phuongThucThueXe import BinhThuong,Goi24h

def getTinhTienThueXe(i):
    try:
        return [BinhThuong.BinhThuong,Goi24h.Goi24h][i]()
    except:
        raise Exception("Không tìm thấy phương thức tính tiền")
    

