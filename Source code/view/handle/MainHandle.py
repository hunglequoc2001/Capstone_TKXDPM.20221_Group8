from PyQt5 import QtWidgets, uic, QtCore
import sys
from view.handle import DanhSachNhaXeHandle,HomeHandle,ThueXeHandle,TraXeHandle,DanhSachXeDangThueHandle
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("./view/ui/main.ui", self)
        self.menuButton.clicked.connect(self.side_Menu_Def)
        self.status_menu=0
        self.homeButton.clicked.connect(self.clickHomeButton)
        self.danhSachNhaXeButton.clicked.connect(self.clickDanhSachNhaXeButton)
        self.thueXeButton.clicked.connect(self.clickThueXeButton)
        self.traXeButton.clicked.connect(self.clickTraXeButton)  
        self.xeDangThueButton.clicked.connect(self.clickXeDangThueButton)
        self.mainWidget=HomeHandle.HomeQWidget(self) 
        self.scrollArea.setWidget(self.mainWidget )
        self.maXe=None
        # self.centralwidget.setLayout(QtWidgets.QVBoxLayout())

    def side_Menu_Def(self):
        if self.status_menu:
            self.menuButton.setText("")
            self.homeButton.setText("")
            self.danhSachNhaXeButton.setText("")
            self.thueXeButton.setText("")
            self.traXeButton.setText("")
            self.xeDangThueButton.setText("")
            self.status_menu=0
        else:
            self.menuButton.setText("MENU")
            self.homeButton.setText("HOME")
            self.danhSachNhaXeButton.setText("Nhà xe")
            self.thueXeButton.setText("Thuê xe")
            self.traXeButton.setText("Trả xe")
            self.xeDangThueButton.setText("Xe đang thuê")
            self.status_menu=1

    def clickHomeButton(self):
        self.mainLabel.setText("HOME")
        self.mainWidget=HomeHandle.HomeQWidget(self) 
        self.scrollArea.setWidget(self.mainWidget )
        
    def clickXeDangThueButton(self):
        self.mainLabel.setText("Danh sách các xe đang thuê")
        self.mainWidget=DanhSachXeDangThueHandle.DanhSachXeDangThueQWidget(self)
        self.scrollArea.setWidget(self.mainWidget )

    def clickDanhSachNhaXeButton(self):
        self.mainLabel.setText("Danh sách các nhà xe")
        self.mainWidget=DanhSachNhaXeHandle.DanhSachNhaXeQWidget(self)
        self.scrollArea.setWidget(self.mainWidget )

    def clickThueXeButton(self):
        self.mainLabel.setText("Thuê Xe")
        self.mainWidget=ThueXeHandle.ThueXeQWidget(self)
        self.scrollArea.setWidget(self.mainWidget )
        # self.grab().save("../Capstone_TKXDPM.20221_Group8/Thiết kế giao diện/Giao diện thuê xe.png")

    def clickTraXeButton(self):
        self.mainLabel.setText("Trả xe")
        self.mainWidget=TraXeHandle.TraXeQWidget(self)
        self.scrollArea.setWidget(self.mainWidget )    
    
    def traXe(self):
        self.mainLabel.setText("Trả xe")
        # self.mainWidget.close()
        
        # scrollArea=self.scrollArea
        # self.scrollArea=QtWidgets.QScrollArea()
        # self.frame_3.layout().replaceWidget(scrollArea,self.scrollArea)
        # # print(2)
        traXeWidget=TraXeHandle.TraXeQWidget(self,self.maXe)
        # traXeWidget.show()
        w=self.scrollArea.takeWidget()
        self.scrollArea.setWidget(traXeWidget)    
        # self.grab().save("../Capstone_TKXDPM.20221_Group8/Thiết kế giao diện/Giao diện trả xe.png")

# if __name__ == "__main__":
#     MainApp = QtWidgets.QApplication(sys.argv)
#     App = Main_UI()
#     # print(App.__dict__)
#     App.show()
#     sys.exit(MainApp.exec_())
