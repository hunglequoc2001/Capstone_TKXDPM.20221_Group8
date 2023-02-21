from control.BaseControl import BaseControl
import pandas
from PyQt5 import QtCore, QtGui
from utils.config import PHUONGTHUCTHUEXE
class DanhSachNhaXeControl(BaseControl):
    def __init__(self, view):
        super().__init__(view)
        data=self.connect.select('SELECT xe.maXe,xe.bienSoXe,xe.loaiXe,xddt.maThe,xddt.nguoiThueXe,xddt.phuongThucThueXe,xddt.thoiDiemThue FROM xe_dang_duoc_thue AS xddt JOIN xe ON xddt.maXe=xe.maXe;')
        listColumn=['Mã xe','Biển số xe','Loại xe','Mã thẻ','Người thuê xe','Phương thức thuê xe','Thời điểm thuê xe']
        df=pandas.DataFrame(data,columns=listColumn)
        df['Phương thức thuê xe']=df['Phương thức thuê xe'].map(lambda x: PHUONGTHUCTHUEXE[x])   
        df['Thời điểm thuê xe']=df['Thời điểm thuê xe'].map(lambda x: x.strftime("%H:%M %d/%m/%Y")) 
        for i in df:
            self.view.model.invisibleRootItem().appendColumn([
                QtGui.QStandardItem(str(x)) for x in df[i]
            ])
        self.view.model.setHorizontalHeaderLabels(listColumn)
        self.view.comboBox.addItems(listColumn)

    def traXe(self):
        index= self.view.view.currentIndex()
        row = index.row()
        maXe = self.view.view.model().data(self.view.view.model().index(row, 0))       
        self.view.parent.traXe(maXe)