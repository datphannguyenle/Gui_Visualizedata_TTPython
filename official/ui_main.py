from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from rc_images import *

#########################################################################

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuicEvLFF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class Ui_MainWindow(object):
    def close(self) -> bool: ...
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 858)
        MainWindow.setMinimumSize(QSize(1000, 858))
        MainWindow.setMaximumSize(QSize(1000, 858))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 120, 451, 291))
        self.dothi_1 = QVBoxLayout(self.verticalLayoutWidget)
        self.dothi_1.setObjectName(u"dothi_1")
        self.dothi_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(30, 450, 451, 291))
        self.dothi_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.dothi_3.setObjectName(u"dothi_3")
        self.dothi_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(520, 450, 451, 291))
        self.dothi_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.dothi_4.setObjectName(u"dothi_4")
        self.dothi_4.setContentsMargins(0, 0, 0, 0)
        self.tieude = QWidget(self.centralwidget)
        self.tieude.setObjectName(u"tieude")
        self.tieude.setGeometry(QRect(0, 0, 1000, 101))
        self.tieude.setMinimumSize(QSize(1000, 0))
        self.tieude.setMaximumSize(QSize(1000, 16777215))
        self.tieude.setStyleSheet(u"border-radius: 30px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));")
        self.tendetai = QLabel(self.tieude)
        self.tendetai.setObjectName(u"tendetai")
        self.tendetai.setGeometry(QRect(10, 20, 981, 41))
        self.tendetai.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 italic 19pt \"League Spartan\";\n"
"background-color: none;\n"
"")
        self.tacgia = QLabel(self.tieude)
        self.tacgia.setObjectName(u"tacgia")
        self.tacgia.setGeometry(QRect(10, 70, 981, 20))
        self.tacgia.setStyleSheet(u"background-color: none;\n"
"")
        self.label = QLabel(self.tieude)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 71))
        self.label.setStyleSheet(u"background-color: none;\n"
"image: url(:/images/images/logos/ute_logo.png);")
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(30, 780, 89, 31))
        self.load_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(390, 780, 91, 31))
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(890, 780, 91, 31))
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
#        self.exit_button.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#        self.exit_button.clicked.connect(lambda: self.close())
        self.url_load = QTextEdit(self.centralwidget)
        self.url_load.setObjectName(u"url_load")
        self.url_load.setGeometry(QRect(130, 780, 251, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1000, 858))
        self.frame.setMinimumSize(QSize(1000, 800))
        self.frame.setMaximumSize(QSize(1000, 858))
        self.frame.setStyleSheet(u"border-radius:30px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(520, 120, 451, 291))
        self.dothi_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.dothi_2.setObjectName(u"dothi_2")
        self.dothi_2.setContentsMargins(0, 0, 0, 0)
        self.mota = QLabel(self.centralwidget)
        self.mota.setObjectName(u"mota")
        self.mota.setGeometry(QRect(30, 820, 501, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.tieude.raise_()
        self.load_button.raise_()
        self.start_button.raise_()
        self.exit_button.raise_()
        self.url_load.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.mota.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.tendetai.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tendetai.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tendetai.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-style:normal;\">Visualize Data Software</span></p></body></html>", None))
        self.tacgia.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">BY: LE PHAN NGUYEN DAT 20139037 - NGUYEN HOAI TAM 20139012</span></p></body></html>", None))
        self.label.setText("")
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.mota.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic; color:#c2c2c2;\">Nh\u1ea5n </span><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">Load</span><span style=\" font-style:italic; color:#c2c2c2;\"> \u0111\u1ec3 t\u1ea3i d\u1eef li\u1ec7u l\u00ean ph\u1ea7n m\u1ec1m v\u00e0 </span><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">Start</span><span style=\" font-style:italic; color:#c2c2c2;\"> \u0111\u1ec3 b\u1eaft \u0111\u1ea7u t\u1ea1o bi\u1ec3u \u0111\u1ed3 !</span></p></body></html>", None))
    # retranslateUi

