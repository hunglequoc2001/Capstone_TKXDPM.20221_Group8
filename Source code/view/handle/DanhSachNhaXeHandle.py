from PyQt5 import QtWidgets, uic
from control.DanhSachNhaXeControl import DanhSachNhaXeControl
import sys
class DanhSachNhaXeQWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        uic.loadUi("./view/ui/danhSachNhaXe.ui", self)
        self.control=DanhSachNhaXeControl(self)
        self.parent=parent
        

# from PyQt5 import QtWidgets, uic, QtCore
# import sys
# if __name__ == "__main__":
#     MainApp = QtWidgets.QApplication(sys.argv)
#     App = DanhSachNhaXeQWidgets()
#     # print(type(App))
#     # print(App.__dict__)
#     App.show()
#     sys.exit(MainApp.exec_())
