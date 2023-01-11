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
    # print(type(App))
    # App.move(screen_center(App))
    App.show()
    # splash.finish(App)
    sys.exit(MainApp.exec_())
