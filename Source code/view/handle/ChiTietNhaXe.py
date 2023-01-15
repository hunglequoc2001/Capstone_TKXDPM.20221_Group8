from PyQt5 import QtWidgets, uic,QtCore
from entity.Xe import Xe
class ChiTietNhaXeQWidget(QtWidgets.QWidget):
    def __init__(self,nhaXe,parent):
        super().__init__()
        self.parent=parent
        uic.loadUi("./view/ui/chiTietNhaXe.ui", self)
        thongTin=nhaXe.getThongTinNhaXe()
        self.label_TenNhaXe.setText("Nhà xe "+thongTin['Tên nhà xe'])
        self.label_DiaChi.setText(thongTin['Địa chỉ'])
        self.label_SoDienThoai.setText(thongTin['Số điện thoại'])
        self.label_Mail.setText(thongTin['Mail'])
        thongKe=nhaXe.getThongKeXe()
        for i in thongKe:
            self.frame_LoaiXe.layout().addWidget(QtWidgets.QLabel(i))
            self.frame_SoLuong.layout().addWidget(QtWidgets.QLabel(str(thongKe[i])))
        danhSach=nhaXe.getDanhSachXe()
        labels=['Biển số xe','Loại xe','Vị trí','Hãng xe','Lượng pin']
        self.tableWidget.setColumnCount(len(labels))
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.tableWidget.setRowCount(len(danhSach))
        i=0
        for maXe,vitri in danhSach:
            xe=Xe(maXe)
            thongTin=xe.getThongTinXe()
            # print(thongTin)
            thongTin['Vị trí']=vitri
            for j,l in enumerate(labels):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.tableWidget.setItem(i,j,item)
                self.tableWidget.item(i,j).setText(str(thongTin[l]))
            i+=1
    def closeEvent(self, event):
        event.accept()
        self.parent.show()