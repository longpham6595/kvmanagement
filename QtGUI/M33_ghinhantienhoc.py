# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M33_ghinhantienhoc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ghinhanvadshp(object):
    def setupUi(self, ghinhanvadshp):
        ghinhanvadshp.setObjectName("ghinhanvadshp")
        ghinhanvadshp.resize(728, 434)
        self.gridLayout = QtWidgets.QGridLayout(ghinhanvadshp)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.daysort = QtWidgets.QRadioButton(ghinhanvadshp)
        self.daysort.setObjectName("daysort")
        self.verticalLayout.addWidget(self.daysort)
        self.monthsort = QtWidgets.QRadioButton(ghinhanvadshp)
        self.monthsort.setMinimumSize(QtCore.QSize(0, 20))
        self.monthsort.setMaximumSize(QtCore.QSize(16777215, 20))
        self.monthsort.setObjectName("monthsort")
        self.verticalLayout.addWidget(self.monthsort)
        self.yearsort = QtWidgets.QRadioButton(ghinhanvadshp)
        self.yearsort.setMinimumSize(QtCore.QSize(0, 20))
        self.yearsort.setMaximumSize(QtCore.QSize(16777215, 20))
        self.yearsort.setObjectName("yearsort")
        self.verticalLayout.addWidget(self.yearsort)
        self.gridLayout.addLayout(self.verticalLayout, 1, 5, 1, 2)
        self.loc = QtWidgets.QPushButton(ghinhanvadshp)
        self.loc.setMinimumSize(QtCore.QSize(0, 28))
        self.loc.setMaximumSize(QtCore.QSize(16777215, 28))
        self.loc.setObjectName("loc")
        self.gridLayout.addWidget(self.loc, 1, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(ghinhanvadshp)
        self.label_4.setMinimumSize(QtCore.QSize(0, 28))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(ghinhanvadshp)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateinfo = QtWidgets.QDateEdit(ghinhanvadshp)
        self.dateinfo.setMinimumSize(QtCore.QSize(0, 22))
        self.dateinfo.setMaximumSize(QtCore.QSize(16777215, 22))
        self.dateinfo.setDate(QtCore.QDate(2020, 1, 1))
        self.dateinfo.setObjectName("dateinfo")
        self.gridLayout.addWidget(self.dateinfo, 1, 1, 1, 4)
        self.saveinfo = QtWidgets.QPushButton(ghinhanvadshp)
        self.saveinfo.setMinimumSize(QtCore.QSize(0, 28))
        self.saveinfo.setMaximumSize(QtCore.QSize(16777215, 28))
        self.saveinfo.setObjectName("saveinfo")
        self.gridLayout.addWidget(self.saveinfo, 2, 7, 1, 1)
        self.hocphi_view = QtWidgets.QTableWidget(ghinhanvadshp)
        self.hocphi_view.setMinimumSize(QtCore.QSize(710, 220))
        self.hocphi_view.setObjectName("hocphi_view")
        self.hocphi_view.setColumnCount(7)
        self.hocphi_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hocphi_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hocphi_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hocphi_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.hocphi_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.hocphi_view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.hocphi_view.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.hocphi_view.setHorizontalHeaderItem(6, item)
        self.hocphi_view.horizontalHeader().setVisible(True)
        self.hocphi_view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.hocphi_view, 4, 0, 1, 8)
        self.delid = QtWidgets.QPushButton(ghinhanvadshp)
        self.delid.setMinimumSize(QtCore.QSize(0, 28))
        self.delid.setMaximumSize(QtCore.QSize(16777215, 28))
        self.delid.setObjectName("delid")
        self.gridLayout.addWidget(self.delid, 3, 7, 1, 1)
        self.idxoa = QtWidgets.QLineEdit(ghinhanvadshp)
        self.idxoa.setMinimumSize(QtCore.QSize(0, 22))
        self.idxoa.setMaximumSize(QtCore.QSize(16777215, 22))
        self.idxoa.setObjectName("idxoa")
        self.gridLayout.addWidget(self.idxoa, 3, 1, 1, 6)
        self.label_3 = QtWidgets.QLabel(ghinhanvadshp)
        self.label_3.setMinimumSize(QtCore.QSize(0, 28))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.idghinhan = QtWidgets.QLineEdit(ghinhanvadshp)
        self.idghinhan.setMinimumSize(QtCore.QSize(0, 22))
        self.idghinhan.setMaximumSize(QtCore.QSize(16777215, 22))
        self.idghinhan.setObjectName("idghinhan")
        self.gridLayout.addWidget(self.idghinhan, 2, 1, 1, 6)
        self.label = QtWidgets.QLabel(ghinhanvadshp)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 8)
        self.hoantat = QtWidgets.QPushButton(ghinhanvadshp)
        self.hoantat.setObjectName("hoantat")
        self.gridLayout.addWidget(self.hoantat, 5, 0, 1, 8)

        self.retranslateUi(ghinhanvadshp)
        QtCore.QMetaObject.connectSlotsByName(ghinhanvadshp)

    def retranslateUi(self, ghinhanvadshp):
        _translate = QtCore.QCoreApplication.translate
        ghinhanvadshp.setWindowTitle(_translate("ghinhanvadshp", "Ghi nh???n ????ng ti???n h???c v?? danh s??ch h???c ph?? ???? thu"))
        self.daysort.setText(_translate("ghinhanvadshp", "L???c theo ng??y + Th??ng + N??m"))
        self.monthsort.setText(_translate("ghinhanvadshp", "L???c theo th??ng + n??m"))
        self.yearsort.setText(_translate("ghinhanvadshp", "L???c theo n??m"))
        self.loc.setText(_translate("ghinhanvadshp", "L???c d??? li???u"))
        self.label_4.setText(_translate("ghinhanvadshp", "ID thu h???c ph?? ????? x??a"))
        self.label_2.setText(_translate("ghinhanvadshp", "Ng??y / Th??ng / N??m (DD/MM/YYYY)"))
        self.dateinfo.setDisplayFormat(_translate("ghinhanvadshp", "d/M/yyyy"))
        self.saveinfo.setText(_translate("ghinhanvadshp", "Ghi nh???n ????ng h???c ph??"))
        item = self.hocphi_view.horizontalHeaderItem(0)
        item.setText(_translate("ghinhanvadshp", "ID thu h???c ph??"))
        item = self.hocphi_view.horizontalHeaderItem(1)
        item.setText(_translate("ghinhanvadshp", "ID h???c ph??"))
        item = self.hocphi_view.horizontalHeaderItem(2)
        item.setText(_translate("ghinhanvadshp", "Ng??y thu"))
        item = self.hocphi_view.horizontalHeaderItem(3)
        item.setText(_translate("ghinhanvadshp", "M?? h???c sinh"))
        item = self.hocphi_view.horizontalHeaderItem(4)
        item.setText(_translate("ghinhanvadshp", "H??? t??n h???c sinh"))
        item = self.hocphi_view.horizontalHeaderItem(5)
        item.setText(_translate("ghinhanvadshp", "M??n h???c"))
        item = self.hocphi_view.horizontalHeaderItem(6)
        item.setText(_translate("ghinhanvadshp", "Gi??o vi??n"))
        self.delid.setText(_translate("ghinhanvadshp", "X??a id ghi nh???n nh???m"))
        self.label_3.setText(_translate("ghinhanvadshp", "Ghi nh???n ID h???c ph?? ????ng ti???n"))
        self.label.setText(_translate("ghinhanvadshp", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">DANH S??CH H???C PH?? ???? THU</span></p></body></html>"))
        self.hoantat.setText(_translate("ghinhanvadshp", "Ho??n t???t"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ghinhanvadshp = QtWidgets.QWidget()
    ui = Ui_ghinhanvadshp()
    ui.setupUi(ghinhanvadshp)
    ghinhanvadshp.show()
    sys.exit(app.exec_())
