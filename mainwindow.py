# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 131, 16))
        self.label.setObjectName("label")
        self.qt_calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.qt_calendar.setGeometry(QtCore.QRect(220, 40, 281, 211))
        self.qt_calendar.setMouseTracking(False)
        self.qt_calendar.setTabletTracking(False)
        self.qt_calendar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.qt_calendar.setAutoFillBackground(True)
        self.qt_calendar.setSelectedDate(QtCore.QDate(2020, 2, 6))
        self.qt_calendar.setMinimumDate(QtCore.QDate(1753, 9, 14))
        self.qt_calendar.setGridVisible(True)
        self.qt_calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.qt_calendar.setNavigationBarVisible(True)
        self.qt_calendar.setDateEditEnabled(False)
        self.qt_calendar.setObjectName("qt_calendar")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 160, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qt_id = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.qt_id.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qt_id.setFont(font)
        self.qt_id.setAcceptDrops(True)
        self.qt_id.setObjectName("qt_id")
        self.verticalLayout.addWidget(self.qt_id)
        self.qt_pw = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qt_pw.setFont(font)
        self.qt_pw.setText("")
        self.qt_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.qt_pw.setObjectName("qt_pw")
        self.verticalLayout.addWidget(self.qt_pw)
        self.qt_visitor = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qt_visitor.setFont(font)
        self.qt_visitor.setObjectName("qt_visitor")
        self.verticalLayout.addWidget(self.qt_visitor)
        self.qt_building_combo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.qt_building_combo.setEditable(False)
        self.qt_building_combo.setCurrentText("")
        self.qt_building_combo.setObjectName("qt_building_combo")
        self.verticalLayout.addWidget(self.qt_building_combo)
        self.qt_phone = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qt_phone.setFont(font)
        self.qt_phone.setObjectName("qt_phone")
        self.verticalLayout.addWidget(self.qt_phone)
        self.qt_company = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qt_company.setFont(font)
        self.qt_company.setObjectName("qt_company")
        self.verticalLayout.addWidget(self.qt_company)
        self.qt_vehicle = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qt_vehicle.setFont(font)
        self.qt_vehicle.setObjectName("qt_vehicle")
        self.verticalLayout.addWidget(self.qt_vehicle)
        self.qt_reason = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.qt_reason.setFont(font)
        self.qt_reason.setObjectName("qt_reason")
        self.verticalLayout.addWidget(self.qt_reason)
        self.info_save = QtWidgets.QPushButton(self.centralwidget)
        self.info_save.setGeometry(QtCore.QRect(240, 260, 91, 23))
        self.info_save.setObjectName("info_save")
        self.register_park = QtWidgets.QPushButton(self.centralwidget)
        self.register_park.setGeometry(QtCore.QRect(350, 260, 91, 23))
        self.register_park.setObjectName("register_park")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LG 마곡 주차 자동 등록 "))
        self.qt_id.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\'; font-size:9pt;\">E-Mail</span></p></body></html>"))
        self.qt_id.setPlaceholderText(_translate("MainWindow", "E-Mail"))
        self.qt_pw.setPlaceholderText(_translate("MainWindow", "Password"))
        self.qt_visitor.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\'; font-size:9pt;\">방문자</span></p></body></html>"))
        self.qt_visitor.setPlaceholderText(_translate("MainWindow", "방문자"))
        self.qt_phone.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\'; font-size:9pt;\">연락처</span></p></body></html>"))
        self.qt_phone.setPlaceholderText(_translate("MainWindow", "xxx-xxxx-xxxx"))
        self.qt_company.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\'; font-size:9pt;\">소속기관</span></p></body></html>"))
        self.qt_company.setPlaceholderText(_translate("MainWindow", "LG전자"))
        self.qt_vehicle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\'; font-size:9pt;\">차량번호</span></p></body></html>"))
        self.qt_vehicle.setPlaceholderText(_translate("MainWindow", "xx가xxxx"))
        self.qt_reason.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\'; font-size:9pt;\">사유</span></p></body></html>"))
        self.qt_reason.setPlaceholderText(_translate("MainWindow", "개인업무"))
        self.info_save.setText(_translate("MainWindow", "주차정보저장"))
        self.register_park.setText(_translate("MainWindow", "주차 예약"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

