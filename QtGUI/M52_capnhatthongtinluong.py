# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M52_capnhatthongtinluong.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_capnhatttluong(object):
    def setupUi(self, capnhatttluong):
        capnhatttluong.setObjectName("capnhatttluong")
        capnhatttluong.resize(978, 604)
        self.gridLayout = QtWidgets.QGridLayout(capnhatttluong)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(capnhatttluong)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 16)
        self.delallhsl = QtWidgets.QPushButton(capnhatttluong)
        self.delallhsl.setObjectName("delallhsl")
        self.gridLayout.addWidget(self.delallhsl, 6, 15, 1, 1)
        self.basepayment = QtWidgets.QDoubleSpinBox(capnhatttluong)
        self.basepayment.setMinimum(0.0)
        self.basepayment.setMaximum(1000.0)
        self.basepayment.setSingleStep(0.01)
        self.basepayment.setProperty("value", 0.0)
        self.basepayment.setObjectName("basepayment")
        self.gridLayout.addWidget(self.basepayment, 9, 6, 1, 8)
        self.httt = QtWidgets.QPushButton(capnhatttluong)
        self.httt.setObjectName("httt")
        self.gridLayout.addWidget(self.httt, 11, 0, 1, 16)
        self.capnhathsl = QtWidgets.QPushButton(capnhatttluong)
        self.capnhathsl.setObjectName("capnhathsl")
        self.gridLayout.addWidget(self.capnhathsl, 4, 15, 1, 1)
        self.label_2 = QtWidgets.QLabel(capnhatttluong)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 16)
        self.udnewbasepm = QtWidgets.QPushButton(capnhatttluong)
        self.udnewbasepm.setObjectName("udnewbasepm")
        self.gridLayout.addWidget(self.udnewbasepm, 9, 15, 1, 1)
        self.mgvblhs = QtWidgets.QComboBox(capnhatttluong)
        self.mgvblhs.setObjectName("mgvblhs")
        self.gridLayout.addWidget(self.mgvblhs, 4, 1, 1, 2)
        self.hslsua = QtWidgets.QDoubleSpinBox(capnhatttluong)
        self.hslsua.setMaximum(1.0)
        self.hslsua.setSingleStep(0.01)
        self.hslsua.setObjectName("hslsua")
        self.gridLayout.addWidget(self.hslsua, 2, 11, 1, 4)
        self.hsl = QtWidgets.QDoubleSpinBox(capnhatttluong)
        self.hsl.setMaximum(1.0)
        self.hsl.setSingleStep(0.01)
        self.hsl.setObjectName("hsl")
        self.gridLayout.addWidget(self.hsl, 4, 9, 1, 6)
        self.label = QtWidgets.QLabel(capnhatttluong)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 16)
        self.label_14 = QtWidgets.QLabel(capnhatttluong)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 10, 0, 1, 16)
        self.label_5 = QtWidgets.QLabel(capnhatttluong)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 6, 1, 1)
        self.label_15 = QtWidgets.QLabel(capnhatttluong)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.luongbac = QtWidgets.QDoubleSpinBox(capnhatttluong)
        self.luongbac.setMaximum(1000.0)
        self.luongbac.setSingleStep(1.0)
        self.luongbac.setObjectName("luongbac")
        self.gridLayout.addWidget(self.luongbac, 2, 8, 1, 1)
        self.label_6 = QtWidgets.QLabel(capnhatttluong)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.mgvcnl = QtWidgets.QComboBox(capnhatttluong)
        self.mgvcnl.setObjectName("mgvcnl")
        self.gridLayout.addWidget(self.mgvcnl, 2, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(capnhatttluong)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(capnhatttluong)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 9, 1, 2)
        self.label_18 = QtWidgets.QLabel(capnhatttluong)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 16)
        self.label_4 = QtWidgets.QLabel(capnhatttluong)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.mgvlcd = QtWidgets.QComboBox(capnhatttluong)
        self.mgvlcd.setObjectName("mgvlcd")
        self.gridLayout.addWidget(self.mgvlcd, 9, 1, 1, 4)
        self.label_9 = QtWidgets.QLabel(capnhatttluong)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(capnhatttluong)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.payment_view = QtWidgets.QTableWidget(capnhatttluong)
        self.payment_view.setMinimumSize(QtCore.QSize(700, 0))
        self.payment_view.setObjectName("payment_view")
        self.payment_view.setColumnCount(8)
        self.payment_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.payment_view.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.payment_view, 12, 0, 1, 16)
        self.label_10 = QtWidgets.QLabel(capnhatttluong)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 16)
        self.label_13 = QtWidgets.QLabel(capnhatttluong)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 14, 1, 1)
        self.updatebl = QtWidgets.QPushButton(capnhatttluong)
        self.updatebl.setObjectName("updatebl")
        self.gridLayout.addWidget(self.updatebl, 2, 15, 1, 1)
        self.bacsua = QtWidgets.QComboBox(capnhatttluong)
        self.bacsua.setObjectName("bacsua")
        self.gridLayout.addWidget(self.bacsua, 2, 4, 1, 2)
        self.hoantat = QtWidgets.QPushButton(capnhatttluong)
        self.hoantat.setObjectName("hoantat")
        self.gridLayout.addWidget(self.hoantat, 13, 0, 1, 16)
        self.label_12 = QtWidgets.QLabel(capnhatttluong)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 5, 1, 1)
        self.bacxoa = QtWidgets.QComboBox(capnhatttluong)
        self.bacxoa.setObjectName("bacxoa")
        self.gridLayout.addWidget(self.bacxoa, 6, 6, 1, 8)
        self.mgvhsl = QtWidgets.QComboBox(capnhatttluong)
        self.mgvhsl.setObjectName("mgvhsl")
        self.gridLayout.addWidget(self.mgvhsl, 6, 1, 1, 4)
        self.label_8 = QtWidgets.QLabel(capnhatttluong)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 5, 1, 1)
        self.steppayment = QtWidgets.QDoubleSpinBox(capnhatttluong)
        self.steppayment.setMinimum(1.0)
        self.steppayment.setMaximum(1000.0)
        self.steppayment.setSingleStep(1.0)
        self.steppayment.setProperty("value", 1.0)
        self.steppayment.setObjectName("steppayment")
        self.gridLayout.addWidget(self.steppayment, 4, 4, 1, 2)
        self.label_3 = QtWidgets.QLabel(capnhatttluong)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 8, 1, 1)
        self.delperhsl = QtWidgets.QPushButton(capnhatttluong)
        self.delperhsl.setObjectName("delperhsl")
        self.gridLayout.addWidget(self.delperhsl, 6, 14, 1, 1)
        self.label_19 = QtWidgets.QLabel(capnhatttluong)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 6, 1, 2)

        self.retranslateUi(capnhatttluong)
        QtCore.QMetaObject.connectSlotsByName(capnhatttluong)

    def retranslateUi(self, capnhatttluong):
        _translate = QtCore.QCoreApplication.translate
        capnhatttluong.setWindowTitle(_translate("capnhatttluong", "Form"))
        self.label_7.setText(_translate("capnhatttluong", "<html><head/><body><p align=\"center\">X??? l?? x??a h??? s??? l????ng</p></body></html>"))
        self.delallhsl.setText(_translate("capnhatttluong", "X??a to??n b??? h??? s??? l????ng c??"))
        self.httt.setText(_translate("capnhatttluong", "Hi???n th??? th??ng tin"))
        self.capnhathsl.setText(_translate("capnhatttluong", "Th??m b???c l????ng m???i"))
        self.label_2.setText(_translate("capnhatttluong", "<html><head/><body><p align=\"center\">Ch??n b???c l????ng m???i theo h??? s???</p></body></html>"))
        self.udnewbasepm.setText(_translate("capnhatttluong", "C???p nh???t m???c l????ng m???i"))
        self.label.setText(_translate("capnhatttluong", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">B???NG C???P NH???T TH??NG TIN ?????NH M???C TR??? L????NG</span></p></body></html>"))
        self.label_14.setText(_translate("capnhatttluong", "<html><head/><body><p align=\"center\">B???ng hi???n th??? t???ng th??? to??n b??? l????ng gi??o vi??n trong h??? th???ng</p></body></html>"))
        self.label_5.setText(_translate("capnhatttluong", "tri???u ?????ng"))
        self.label_15.setText(_translate("capnhatttluong", "M?? gi??o vi??n"))
        self.label_6.setText(_translate("capnhatttluong", "M?? gi??o vi??n"))
        self.label_16.setText(_translate("capnhatttluong", "B???c s???a"))
        self.label_17.setText(_translate("capnhatttluong", "H??? s??? l????ng s???a"))
        self.label_18.setText(_translate("capnhatttluong", "<html><head/><body><p align=\"center\">Thay ?????i l????ng tr??n b???c l????ng</p></body></html>"))
        self.label_4.setText(_translate("capnhatttluong", "M???c l????ng t???i thi???u b???t ?????u ??p d???ng"))
        self.label_9.setText(_translate("capnhatttluong", "M?? gi??o vi??n"))
        self.label_11.setText(_translate("capnhatttluong", "M?? gi??o vi??n"))
        item = self.payment_view.horizontalHeaderItem(0)
        item.setText(_translate("capnhatttluong", "M?? gi??o vi??n"))
        item = self.payment_view.horizontalHeaderItem(1)
        item.setText(_translate("capnhatttluong", "T??n gi??o vi??n"))
        item = self.payment_view.horizontalHeaderItem(2)
        item.setText(_translate("capnhatttluong", "H??? s??? l????ng"))
        item = self.payment_view.horizontalHeaderItem(3)
        item.setText(_translate("capnhatttluong", "Total Prfit Crtd"))
        item = self.payment_view.horizontalHeaderItem(4)
        item.setText(_translate("capnhatttluong", "L????ng Rated"))
        item = self.payment_view.horizontalHeaderItem(5)
        item.setText(_translate("capnhatttluong", "L????ng c??? ?????nh"))
        item = self.payment_view.horizontalHeaderItem(6)
        item.setText(_translate("capnhatttluong", "T???ng thu nh???p"))
        item = self.payment_view.horizontalHeaderItem(7)
        item.setText(_translate("capnhatttluong", "ProfitAft.Paid"))
        self.label_10.setText(_translate("capnhatttluong", "<html><head/><body><p align=\"center\">X??? l?? c???p nh???t m???c l????ng c??? ?????nh</p></body></html>"))
        self.label_13.setText(_translate("capnhatttluong", "tri???u ?????ng"))
        self.updatebl.setText(_translate("capnhatttluong", "C???p nh???t cho b???c l????ng"))
        self.hoantat.setText(_translate("capnhatttluong", "Ho??n t???t"))
        self.label_12.setText(_translate("capnhatttluong", "M???c l????ng c??? ?????nh m???i"))
        self.label_8.setText(_translate("capnhatttluong", "B???c x??a"))
        self.label_3.setText(_translate("capnhatttluong", "H??? s??? l????ng"))
        self.delperhsl.setText(_translate("capnhatttluong", "X??a h??? s??? l????ng b???c n??y"))
        self.label_19.setText(_translate("capnhatttluong", "L????ng t??nh b???c"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    capnhatttluong = QtWidgets.QWidget()
    ui = Ui_capnhatttluong()
    ui.setupUi(capnhatttluong)
    capnhatttluong.show()
    sys.exit(app.exec_())
