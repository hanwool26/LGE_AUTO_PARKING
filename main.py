from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import uic

import park_info_db as PD # parking database
import webDriver as WB # chrome web driver

class MyDlg():
    info_data = None
    def __init__(self):
        self.dlg = loadUi('mainwindow.ui')
        self.dlg.info_save.clicked.connect(self.saveClick)
        self.dlg.register_park.clicked.connect(self.regClick)
        self.dlg.qt_building_combo.addItems(["ISC", "SLC"])
        self.dlg.show()

        self.info_data = None if PD.selectTable() == None else list(PD.selectTable()[0])
        if self.info_data == None:
            self.dlg.qt_log.setText("주차 정보 저장 필요")
        else :
            self.dlg.qt_log.setText("주차 정보 저장 로딩 완료")

    def save_info(self):
        self.my_id = self.dlg.qt_id.text()
        self.my_pw = self.dlg.qt_pw.text()
        self.visitor = self.dlg.qt_visitor.text()
        self.building = self.dlg.qt_building_combo.currentText()
        self.phone_num = self.dlg.qt_phone.text()
        self.company = self.dlg.qt_company.text()
        self.vehicle_num = self.dlg.qt_vehicle.text()
        self.reason = self.dlg.qt_reason.text()

    def load_info_dlg(self):
        if self.info_data != None:
            self.dlg.qt_id.setText(self.info_data[0])
            self.dlg.qt_pw.setText(self.info_data[1])
            self.dlg.qt_visitor.setText(self.info_data[2])
            self.dlg.qt_phone.setText(self.info_data[4])
            self.dlg.qt_company.setText(self.info_data[5])
            self.dlg.qt_vehicle.setText(self.info_data[6])
            self.dlg.qt_reason.setText(self.info_data[7])
            # assign actual value
            self.save_info()

    def saveClick(self):
        self.save_info()
        PD.createTable()
        PD.inputData(self.my_id, self.my_pw, self.visitor, self.building, self.phone_num, self.company, self.vehicle_num, self.reason)
        self.dlg.qt_log.setText("주차 정보 저장 완료")

    def regClick(self):
        self.dlg.qt_log.setText("주차 예약 진행")
        self.wb = WB.WebDriver()
        self.wb.login_page(self.my_id, self.my_pw)
        date = self.dlg.qt_calendar.selectedDate().toString("yyyy.M.d")
        self.wb.park_page(self.visitor, self.building, date.split('.'), self.phone_num, self.company, self.vehicle_num, self.reason)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dlg = MyDlg()
    dlg.load_info_dlg()
    app.exec()
