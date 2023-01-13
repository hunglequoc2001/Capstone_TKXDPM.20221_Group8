from PyQt5 import QtWidgets, uic
from control.TraXeControl import TraXeControl
class TraXeQWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        uic.loadUi("./view/ui/traXe.ui", self)
        self.dateTimeEdit.setDisplayFormat('hh:mm dd/MM/yyyy')
        self.parent=parent
        self.control=TraXeControl(self)
        self.frameTraXe.hide()
        self.pushButtonTimXe.clicked.connect(self.timXe)
        self.pushButton_TraXe.clicked.connect(self.traXe)

    def timXe(self):
        self.frameTraXe.show()

    def traXe(self):
        self.control.traXe()
    