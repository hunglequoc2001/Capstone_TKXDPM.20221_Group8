from control.BaseControl import BaseControl
from PyQt5.QtWidgets import QAbstractScrollArea,QTableWidgetItem,QHeaderView
from PyQt5.QtCore import Qt 
from entity.NhaXe import NhaXe
from view.handle import ChiTietNhaXe
class DanhSachNhaXeControl(BaseControl):
    def __init__(self, view):
        super().__init__(view)
        self.danhSachNhaXe=[]
        for x in self.connect.select('SELECT maNhaXe FROM nha_xe'):
            self.danhSachNhaXe.append(NhaXe(x[0]))
        self.loadTable(data=[x.getTableRow() for x in self.danhSachNhaXe])
        # self.view.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # self.view.tableWidget.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch)
        header = self.view.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.view.tableWidget.doubleClicked.connect(self.chiTietNhaXe)
    def loadTable(self,data):
        labels=data[0].keys()
        self.view.tableWidget.setColumnCount(len(labels))
        self.view.tableWidget.setHorizontalHeaderLabels(labels)
        self.view.tableWidget.setRowCount(len(data))
        for i,d in enumerate(data):
            for j,l in enumerate(labels):
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignHCenter)
                self.view.tableWidget.setItem(i,j,item)
                self.view.tableWidget.item(i,j).setText(str(d[l]))
        return

    def chiTietNhaXe(self):
        nhaXeDuocChon=self.danhSachNhaXe[self.view.tableWidget.selectedItems()[0].row()]
        self.chiTietQWidget=ChiTietNhaXe.ChiTietNhaXeQWidget(parent=self.view.parent,nhaXe=nhaXeDuocChon)
        self.chiTietQWidget.show()
        self.view.parent.hide()
        return