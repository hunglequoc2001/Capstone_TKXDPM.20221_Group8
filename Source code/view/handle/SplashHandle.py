import sys
import time
from PyQt5 import QtWidgets, uic
class SplashScreen(QtWidgets.QSplashScreen):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/ui/splash.ui", self)
        self.progressBar.setValue(0)
        # self.frame.mousePressEvent=self.run
        # self.run()

    def progress(self):
        for i in range(100):
            time.sleep(0.05)
            self.progressBar.setValue(i+1)
        # time.sleep(0.1)
        # self.close()
        
    
