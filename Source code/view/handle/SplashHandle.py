import sys
import time
from PyQt5 import QtWidgets, uic
class ThueXeQWidgets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./view/ui/splash.ui", self)
        self.progressBar.setValue(0)
        self.frame.mousePressEvent=self.run
        # self.run()

    def run(self,Event):
        for i in range(100):
            time.sleep(0.05)
            self.progressBar.setValue(i+1)
        
    
if __name__ == "__main__":
    MainApp = QtWidgets.QApplication(sys.argv)
    App = ThueXeQWidgets()
    # print(App.__dict__)
    App.show()
    # App.run()
    # MainApp.exit()
    sys.exit(MainApp.exec_())