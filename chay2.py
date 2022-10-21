from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from mau1 import Ui_MainWindow
import pandas as pd
import numpy as np

class gui(Ui_MainWindow):
    def __init__(self):
        self.setupUi(MainWindow)
        self.pushButton.clicked.connect(self.chaycode)
    def chaycode(self):
        diachi = QFileDialog.getOpenFileNames()
        print(type(diachi))
        dc2=list(diachi)
        print(type(dc2))
        print(dc2)
        dc3=str(dc2)
        print(type(dc3))
        print(dc3)
        return dc3
    def doc(self):
        docdc= gui.chaycode()
        print(docdc)
    
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui()
    MainWindow.show()
    sys.exit(app.exec_())