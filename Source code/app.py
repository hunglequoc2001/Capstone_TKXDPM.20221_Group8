from view.handle import MainHandle
from PyQt5 import QtWidgets, uic, QtCore
from time import sleep
import sys
if __name__ == "__main__":
    MainApp = QtWidgets.QApplication(sys.argv)
    App = MainHandle.MainWindow()
    # print(type(App))
    App.show()
    # App.grab().save("image.png");
    sys.exit(MainApp.exec_())
