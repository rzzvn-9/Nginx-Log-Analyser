# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitleduKJdmh.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget, QFileDialog)
import LogAnalysisFunctions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.LogFunctions = LogAnalysisFunctions.LogAnalyser()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Log Analyser")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 529)
        MainWindow.setFixedSize(600, 529)
        MainWindow.setWindowIcon(QIcon(u"Icon.png"))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 41))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 130, 281, 181))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_2.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_2.addWidget(self.lineEdit_6)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 60, 581, 41))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 110, 231, 16))
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(310, 130, 281, 181))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_3.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_3.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_3.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_3.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_3.addWidget(self.lineEdit_11)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 110, 231, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 320, 101, 16))
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 340, 281, 181))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_12 = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_4.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_4.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout_4.addWidget(self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.verticalLayout_4.addWidget(self.lineEdit_15)

        self.lineEdit_16 = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.verticalLayout_4.addWidget(self.lineEdit_16)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(310, 340, 281, 181))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_17 = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.verticalLayout_6.addWidget(self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.verticalLayout_6.addWidget(self.lineEdit_18)

        self.lineEdit_19 = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.verticalLayout_6.addWidget(self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_6.addWidget(self.lineEdit_20)

        self.lineEdit_21 = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_6.addWidget(self.lineEdit_21)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 320, 151, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.pushbuttonBrowse)
        self.pushButton.clicked.connect(self.analyselogs)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Log Analyser", u"Log Analyser", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Select log file", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Analyse Log", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Top 5 IP addresses with the most requests", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Top 5 most requested paths", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Top 5 user agents", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Top 5 response status codes", None))
    # retranslateUI

    def pushbuttonBrowse(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select log file","","Log files (*.log *.txt);;All files (*)")

        if file_path:
            self.lineEdit.setText(file_path)

    def analyselogs(self):
        log_dict = self.LogFunctions.create_log_dict(self.lineEdit.text())
        top5_ip = self.LogFunctions.top5_ip_addresses(log_dict)
        top5_paths = self.LogFunctions.top5_requested_paths(log_dict)
        top5_status = self.LogFunctions.top5_status_codes(log_dict)
        top5_agents = self.LogFunctions.top5_user_agent(log_dict)

        self.lineEdit_2.setText(top5_ip[0][0] + " - " + str(top5_ip[0][1]) + " occurrences")
        self.lineEdit_5.setText(top5_ip[1][0] + " - " + str(top5_ip[1][1]) + " occurrences")
        self.lineEdit_6.setText(top5_ip[2][0] + " - " + str(top5_ip[2][1]) + " occurrences")
        self.lineEdit_4.setText(top5_ip[3][0] + " - " + str(top5_ip[3][1]) + " occurrences")
        self.lineEdit_3.setText(top5_ip[4][0] + " - " + str(top5_ip[4][1]) + " occurrences")

        self.lineEdit_7.setText(top5_paths[0][0] + " - " + str(top5_ip[0][1]) + " occurrences")
        self.lineEdit_8.setText(top5_paths[1][0] + " - " + str(top5_ip[1][1]) + " occurrences")
        self.lineEdit_9.setText(top5_paths[2][0] + " - " + str(top5_ip[2][1]) + " occurrences")
        self.lineEdit_10.setText(top5_paths[3][0] + " - " + str(top5_ip[3][1]) + " occurrences")
        self.lineEdit_11.setText(top5_paths[4][0] + " - " + str(top5_ip[4][1]) + " occurrences")

        self.lineEdit_12.setText(str(top5_status[0][0]) + " - " + str(top5_ip[0][1]) + " occurrences")
        self.lineEdit_13.setText(str(top5_status[1][0]) + " - " + str(top5_ip[1][1]) + " occurrences")
        self.lineEdit_14.setText(str(top5_status[2][0]) + " - " + str(top5_ip[2][1]) + " occurrences")
        self.lineEdit_15.setText(str(top5_status[3][0]) + " - " + str(top5_ip[3][1]) + " occurrences")
        self.lineEdit_16.setText(str(top5_status[4][0]) + " - " + str(top5_ip[4][1]) + " occurrences")

        self.lineEdit_17.setText(str(top5_agents[0][0]) + " - " + str(top5_ip[0][1]) + " occurrences")
        self.lineEdit_18.setText(str(top5_agents[1][0]) + " - " + str(top5_ip[1][1]) + " occurrences")
        self.lineEdit_19.setText(str(top5_agents[2][0]) + " - " + str(top5_ip[2][1]) + " occurrences")
        self.lineEdit_20.setText(str(top5_agents[3][0]) + " - " + str(top5_ip[3][1]) + " occurrences")
        self.lineEdit_21.setText(str(top5_agents[4][0]) + " - " + str(top5_ip[4][1]) + " occurrences")

if __name__ == "__main__":
    app = QApplication([])

    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    main_window.show()

    app.exec()