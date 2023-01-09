from PyQt5 import QtWidgets, uic
from control.HomeControl import HomeControl
import sys
class HomeQWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        uic.loadUi("./view/ui/home.ui", self)
        self.parent=parent
        self.control=HomeControl(self)