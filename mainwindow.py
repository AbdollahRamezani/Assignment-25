# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 396)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 20, 541, 331))
        self.tabWidget.setStyleSheet(u"background-color: rgb(57, 91, 168);\n"
"border: 2px double ;\n"
"border-radius: 6px;\n"
"border-color: rgb(85, 85, 127);\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(180, 30, 171, 61))
        font = QFont()
        font.setPointSize(18)
        self.label_stopwatch.setFont(font)
        self.label_stopwatch.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.label_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(140, 150, 75, 24))
        self.btn_start_stopwatch.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(230, 150, 75, 24))
        self.btn_stop_stopwatch.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(320, 150, 75, 24))
        self.btn_reset_stopwatch.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineedit_hour_timer = QLineEdit(self.tab_2)
        self.lineedit_hour_timer.setObjectName(u"lineedit_hour_timer")
        self.lineedit_hour_timer.setGeometry(QRect(120, 30, 71, 61))
        self.lineedit_hour_timer.setFont(font)
        self.lineedit_hour_timer.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.lineedit_hour_timer.setAlignment(Qt.AlignCenter)
        self.lineedit_minute_timer = QLineEdit(self.tab_2)
        self.lineedit_minute_timer.setObjectName(u"lineedit_minute_timer")
        self.lineedit_minute_timer.setGeometry(QRect(210, 30, 71, 61))
        self.lineedit_minute_timer.setFont(font)
        self.lineedit_minute_timer.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.lineedit_minute_timer.setAlignment(Qt.AlignCenter)
        self.lineedit_second_timer = QLineEdit(self.tab_2)
        self.lineedit_second_timer.setObjectName(u"lineedit_second_timer")
        self.lineedit_second_timer.setGeometry(QRect(310, 30, 71, 61))
        self.lineedit_second_timer.setFont(font)
        self.lineedit_second_timer.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.lineedit_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_start_timer = QPushButton(self.tab_2)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(130, 150, 75, 24))
        self.btn_start_timer.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.btn_reset_timer = QPushButton(self.tab_2)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(310, 150, 75, 24))
        self.btn_reset_timer.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.btn_stop_timer = QPushButton(self.tab_2)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(220, 150, 75, 24))
        self.btn_stop_timer.setStyleSheet(u"background-color: rgb(110, 156, 255);\n"
"border-color: rgb(188, 203, 21);")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 572, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"WorldClock", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"StopWatch", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.lineedit_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineedit_minute_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.lineedit_second_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

