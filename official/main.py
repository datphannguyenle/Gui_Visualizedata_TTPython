import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
#Làm ẩn thanh close, minimized, maximized 
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#Nhận biết kích hoạt button
        self.ui.load_button.clicked.connect(self.bt_load)
        self.ui.start_button.clicked.connect(self.bt_start)
        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.show()    
#Thiết lập hoạt động cho button
    def bt_load(self):
        diachi = QFileDialog.getOpenFileNames()
        chuanhoa = str(diachi)[:-20]
        chuanhoa = chuanhoa[3:] 
        print(chuanhoa)
    def bt_start(self):
        print("start ok")  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())