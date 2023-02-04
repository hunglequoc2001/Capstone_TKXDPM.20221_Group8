# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import sys
from PyQt5.QtWidgets import QPushButton
from view.handle.ThanhToanThanhCong import ThanhToanThanhCongDialog

class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 100, 500, 400)

        button=QPushButton(self)
        button.clicked.connect(self.UiComponents)
        # self.layout().addWidget

        # calling method
        # self.UiComponents()
 
        # showing all the widgets
        self.show()
 
 
    # method for components
    def UiComponents(self):
        a=ThanhToanThanhCongDialog(self)
        a.exec()
 
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())