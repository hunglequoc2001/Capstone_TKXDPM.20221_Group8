from control.BaseControl import BaseControl
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
class HomeControl(BaseControl):
    def __init__(self, view):
        super().__init__(view)
        nb=self.connect.select('SELECT COUNT(maNhaXe) FROM nha_xe')[0][0]
        self.view.label_SoNhaXe.setText(str(nb))
        self.view.label_SoNhaXe.setAlignment(Qt.AlignCenter)
        thongKeXe={x[0]:x[1] for x in self.connect.select('SELECT loaiXe,COUNT(loaiXe) FROM xe GROUP BY loaiXe')}
        thongKeXeSanSang={i:0 for i in thongKeXe}
        for x in self.connect.select('SELECT loaiXe,COUNT(loaiXe) FROM xe JOIN xe_trong_nha_xe ON xe.maXe=xe_trong_nha_xe.maXe GROUP BY loaiXe'):
            thongKeXeSanSang[x[0]]=x[1]
        for l in thongKeXe:
            label=QLabel(l)
            self.view.frame_LoaiXe.layout().addWidget(label)
            label=QLabel()
            label.setText(f'<html><head/><body><p align="center"><span style=" color:#00ff00;">{thongKeXeSanSang[l]}</span>/{thongKeXe[l]}</p></body></html>')
            # label.setTextFormat(Qt.RichText)
            self.view.frame_SoXe.layout().addWidget(label)
        # self.frame_LoaiXe