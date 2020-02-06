# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_park(object):
    def setupUi(self, main_park):
        main_park.setObjectName("main_park")
        main_park.resize(552, 353)
        self.centralwidget = QtWidgets.QWidget(main_park)
        self.centralwidget.setObjectName("centralwidget")
        self.qt_calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.qt_calendar.setGeometry(QtCore.QRect(230, 20, 281, 211))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 160, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qt_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
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
        self.qt_visitor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qt_visitor.setObjectName("qt_visitor")
        self.verticalLayout.addWidget(self.qt_visitor)
        self.qt_building_combo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.qt_building_combo.setEditable(False)
        self.qt_building_combo.setCurrentText("")
        self.qt_building_combo.setObjectName("qt_building_combo")
        self.verticalLayout.addWidget(self.qt_building_combo)
        self.qt_phone = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qt_phone.setObjectName("qt_phone")
        self.verticalLayout.addWidget(self.qt_phone)
        self.qt_company = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qt_company.setObjectName("qt_company")
        self.verticalLayout.addWidget(self.qt_company)
        self.qt_vehicle = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qt_vehicle.setObjectName("qt_vehicle")
        self.verticalLayout.addWidget(self.qt_vehicle)
        self.qt_reason = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qt_reason.setObjectName("qt_reason")
        self.verticalLayout.addWidget(self.qt_reason)
        self.info_save = QtWidgets.QPushButton(self.centralwidget)
        self.info_save.setGeometry(QtCore.QRect(250, 240, 91, 23))
        self.info_save.setObjectName("info_save")
        self.register_park = QtWidgets.QPushButton(self.centralwidget)
        self.register_park.setGeometry(QtCore.QRect(360, 240, 91, 23))
        self.register_park.setObjectName("register_park")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 280, 54, 12))
        self.label_2.setObjectName("label_2")
        self.qt_log = QtWidgets.QLineEdit(self.centralwidget)
        self.qt_log.setGeometry(QtCore.QRect(30, 300, 481, 20))
        self.qt_log.setObjectName("qt_log")
        main_park.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_park)
        self.statusbar.setObjectName("statusbar")
        main_park.setStatusBar(self.statusbar)

        self.retranslateUi(main_park)
        QtCore.QMetaObject.connectSlotsByName(main_park)

    def retranslateUi(self, main_park):
        _translate = QtCore.QCoreApplication.translate
        main_park.setWindowTitle(_translate("main_park", "LG 마곡 주차 자동 신청 프로그램"))
        self.qt_id.setPlaceholderText(_translate("main_park", "E-mail"))
        self.qt_pw.setPlaceholderText(_translate("main_park", "Password"))
        self.qt_visitor.setPlaceholderText(_translate("main_park", "방문자"))
        self.qt_phone.setPlaceholderText(_translate("main_park", "연락처(xxx-xxxx-xxxx)"))
        self.qt_company.setPlaceholderText(_translate("main_park", "소속기관"))
        self.qt_vehicle.setPlaceholderText(_translate("main_park", "차량번호(xx가xxxx)"))
        self.qt_reason.setPlaceholderText(_translate("main_park", "사유"))
        self.info_save.setText(_translate("main_park", "주차정보저장"))
        self.register_park.setText(_translate("main_park", "주차 예약"))
        self.label_2.setText(_translate("main_park", "Log"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     main_park = QtWidgets.QMainWindow()
#     ui = Ui_main_park()
#     ui.setupUi(main_park)
#     main_park.show()
#     sys.exit(app.exec_())

