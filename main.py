from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

import park_info_db as PD # parking database
import webDriver as WB # chrome web driver

import mainwindow as UI

class MyDlg(UI.Ui_main_park): # Because of conversion from ui to py, It has to get inherit class from UI.py
    info_data = None
    def __init__(self):
        print("생성자")

    def draw_mainpage(self):
        self.info_save.clicked.connect(self.saveClick)
        self.register_park.clicked.connect(self.regClick)
        self.qt_building_combo.addItems(["ISC", "SLC"])

        self.info_data = None if PD.selectTable() == None else list(PD.selectTable()[0])

        if self.info_data == None:
            self.qt_log.setText("주차 정보 저장 필요")
        else :
            self.qt_log.setText("주차 정보 저장 로딩 완료")

    def save_info(self):
        self.my_id = self.qt_id.text()
        self.my_pw = self.qt_pw.text()
        self.visitor = self.qt_visitor.text()
        self.building = self.qt_building_combo.currentText()
        self.phone_num = self.qt_phone.text()
        self.company = self.qt_company.text()
        self.vehicle_num = self.qt_vehicle.text()
        self.reason = self.qt_reason.text()

    def load_info_dlg(self):
        if self.info_data != None:
            self.qt_id.setText(self.info_data[0])
            self.qt_pw.setText(self.info_data[1])
            self.qt_visitor.setText(self.info_data[2])
            self.qt_phone.setText(self.info_data[4])
            self.qt_company.setText(self.info_data[5])
            self.qt_vehicle.setText(self.info_data[6])
            self.qt_reason.setText(self.info_data[7])
            # assign actual value
            self.save_info()

    def saveClick(self):
        self.save_info()
        PD.createTable()
        PD.inputData(self.my_id, self.my_pw, self.visitor, self.building, self.phone_num, self.company, self.vehicle_num, self.reason)
        self.qt_log.setText("주차 정보 저장 완료")

    def regClick(self):
        self.qt_log.setText("주차 예약 진행")
        self.wb = WB.WebDriver()
        self.wb.login_page(self.my_id, self.my_pw)
        date = self.qt_calendar.selectedDate().toString("yyyy.M.d")
        self.wb.park_page(self.visitor, self.building, date.split('.'), self.phone_num, self.company, self.vehicle_num, self.reason)

if __name__ == "__main__":
     import sys
     app = QApplication(sys.argv)
     dlg = MyDlg()
     main_park = QtWidgets.QMainWindow()
     dlg.setupUi(main_park)
     dlg.draw_mainpage()
     dlg.load_info_dlg()
     main_park.show()
     sys.exit((app.exec_()))
