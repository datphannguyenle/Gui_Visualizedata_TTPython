from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from rc_images import *

#########################################################################

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiWXPHRv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiwEieev.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class Ui_MainWindow(object):
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
        self.logo = QLabel(self.tieude)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 20, 81, 71))
        self.logo.setStyleSheet(u"background-color: none;\n"
"image: url(:/images/images/logos/ute_logo.png);")
        self.info_button = QPushButton(self.tieude)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(970, 80, 21, 21))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.info_button.setFont(font)
        self.info_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.info_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border-radius: 10px;\n"
"border: 3px solid;\n"
"border-color: =rgb(0, 0, 0)")
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
        self.url_load = QTextEdit(self.centralwidget)
        self.url_load.setObjectName(u"url_load")
        self.url_load.setGeometry(QRect(130, 780, 251, 31))
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1000, 858))
        self.background.setMinimumSize(QSize(1000, 800))
        self.background.setMaximumSize(QSize(1000, 858))
        self.background.setStyleSheet(u"border-radius:30px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(520, 120, 451, 291))
        self.dothi_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.dothi_2.setObjectName(u"dothi_2")
        self.dothi_2.setContentsMargins(0, 0, 0, 0)
        self.mota = QLabel(self.centralwidget)
        self.mota.setObjectName(u"mota")
        self.mota.setGeometry(QRect(30, 820, 501, 20))
        self.border_4 = QFrame(self.centralwidget)
        self.border_4.setObjectName(u"border_4")
        self.border_4.setGeometry(QRect(520, 450, 451, 291))
        self.border_4.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.border_4.setFrameShape(QFrame.StyledPanel)
        self.border_4.setFrameShadow(QFrame.Raised)
        self.border_1 = QFrame(self.centralwidget)
        self.border_1.setObjectName(u"border_1")
        self.border_1.setGeometry(QRect(30, 120, 451, 291))
        self.border_1.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.border_1.setFrameShape(QFrame.StyledPanel)
        self.border_1.setFrameShadow(QFrame.Raised)
        self.border_2 = QFrame(self.centralwidget)
        self.border_2.setObjectName(u"border_2")
        self.border_2.setGeometry(QRect(520, 120, 451, 291))
        self.border_2.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.border_2.setFrameShape(QFrame.StyledPanel)
        self.border_2.setFrameShadow(QFrame.Raised)
        self.border_3 = QFrame(self.centralwidget)
        self.border_3.setObjectName(u"border_3")
        self.border_3.setGeometry(QRect(30, 450, 451, 291))
        self.border_3.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.border_3.setFrameShape(QFrame.StyledPanel)
        self.border_3.setFrameShadow(QFrame.Raised)
        self.name_chart_2 = QLabel(self.centralwidget)
        self.name_chart_2.setObjectName(u"name_chart_2")
        self.name_chart_2.setGeometry(QRect(520, 420, 451, 20))
        self.name_chart_3 = QLabel(self.centralwidget)
        self.name_chart_3.setObjectName(u"name_chart_3")
        self.name_chart_3.setGeometry(QRect(30, 750, 451, 20))
        self.name_chart_1 = QLabel(self.centralwidget)
        self.name_chart_1.setObjectName(u"name_chart_1")
        self.name_chart_1.setGeometry(QRect(30, 420, 451, 20))
        self.name_chart_4 = QLabel(self.centralwidget)
        self.name_chart_4.setObjectName(u"name_chart_4")
        self.name_chart_4.setGeometry(QRect(520, 750, 451, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
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
        self.border_4.raise_()
        self.border_1.raise_()
        self.border_2.raise_()
        self.border_3.raise_()
        self.name_chart_2.raise_()
        self.name_chart_3.raise_()
        self.name_chart_1.raise_()
        self.name_chart_4.raise_()

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
        self.logo.setText("")
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.mota.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic; color:#c2c2c2;\">Nh\u1ea5n </span><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">Load</span><span style=\" font-style:italic; color:#c2c2c2;\"> \u0111\u1ec3 t\u1ea3i d\u1eef li\u1ec7u l\u00ean ph\u1ea7n m\u1ec1m v\u00e0 </span><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">Start</span><span style=\" font-style:italic; color:#c2c2c2;\"> \u0111\u1ec3 b\u1eaft \u0111\u1ea7u t\u1ea1o bi\u1ec3u \u0111\u1ed3 !</span></p></body></html>", None))
        self.name_chart_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean bi\u1ec3u \u0111\u1ed3 2</span></p></body></html>", None))
        self.name_chart_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean bi\u1ec3u \u0111\u1ed3 3</span></p></body></html>", None))
        self.name_chart_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean bi\u1ec3u \u0111\u1ed3 1</span></p></body></html>", None))
        self.name_chart_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">T\u00ean bi\u1ec3u \u0111\u1ed3 4</span></p></body></html>", None))
    # retranslateUi