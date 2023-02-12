from view.handle import MainHandle,SplashHandle
from PyQt5 import QtWidgets, uic, QtCore
from time import sleep
import sys
if __name__ == "__main__":
    MainApp = QtWidgets.QApplication(sys.argv)
    screen_center = lambda widget: QtWidgets.QApplication.desktop().screen().rect().center()- widget.rect().center()

    splash =SplashHandle.SplashScreen()
    splash.show()
    splash.move(screen_center(splash))
    splash.progress()
    App = MainHandle.MainWindow()
    App.show()
    
    sys.exit(MainApp.exec_())
