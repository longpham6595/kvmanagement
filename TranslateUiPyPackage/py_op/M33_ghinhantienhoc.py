# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M33_ghinhantienhoc.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ghinhanvadshp(object):
    def setupUi(self, ghinhanvadshp):
        ghinhanvadshp.setObjectName("ghinhanvadshp")
        ghinhanvadshp.resize(1077, 707)
        self.layoutWidget = QtWidgets.QWidget(ghinhanvadshp)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 4, 1061, 691))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 74))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 74))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateinfo = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateinfo.setMinimumSize(QtCore.QSize(0, 22))
        self.dateinfo.setMaximumSize(QtCore.QSize(16777215, 22))
        self.dateinfo.setDate(QtCore.QDate(2020, 1, 1))
        self.dateinfo.setObjectName("dateinfo")
        self.horizontalLayout.addWidget(self.dateinfo)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.daysort = QtWidgets.QRadioButton(self.layoutWidget)
        self.daysort.setObjectName("daysort")
        self.verticalLayout.addWidget(self.daysort)
        self.monthsort = QtWidgets.QRadioButton(self.layoutWidget)
        self.monthsort.setMinimumSize(QtCore.QSize(0, 20))
        self.monthsort.setMaximumSize(QtCore.QSize(16777215, 20))
        self.monthsort.setObjectName("monthsort")
        self.verticalLayout.addWidget(self.monthsort)
        self.yearsort = QtWidgets.QRadioButton(self.layoutWidget)
        self.yearsort.setMinimumSize(QtCore.QSize(0, 20))
        self.yearsort.setMaximumSize(QtCore.QSize(16777215, 20))
        self.yearsort.setObjectName("yearsort")
        self.verticalLayout.addWidget(self.yearsort)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.loc = QtWidgets.QPushButton(self.layoutWidget)
        self.loc.setMinimumSize(QtCore.QSize(0, 28))
        self.loc.setMaximumSize(QtCore.QSize(16777215, 28))
        self.loc.setObjectName("loc")
        self.horizontalLayout_3.addWidget(self.loc)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 28))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.idghinhan = QtWidgets.QLineEdit(self.layoutWidget)
        self.idghinhan.setMinimumSize(QtCore.QSize(0, 22))
        self.idghinhan.setMaximumSize(QtCore.QSize(16777215, 22))
        self.idghinhan.setObjectName("idghinhan")
        self.horizontalLayout_4.addWidget(self.idghinhan)
        self.saveinfo = QtWidgets.QPushButton(self.layoutWidget)
        self.saveinfo.setMinimumSize(QtCore.QSize(0, 28))
        self.saveinfo.setMaximumSize(QtCore.QSize(16777215, 28))
        self.saveinfo.setObjectName("saveinfo")
        self.horizontalLayout_4.addWidget(self.saveinfo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 28))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.idxoa = QtWidgets.QLineEdit(self.layoutWidget)
        self.idxoa.setMinimumSize(QtCore.QSize(0, 22))
        self.idxoa.setMaximumSize(QtCore.QSize(16777215, 22))
        self.idxoa.setObjectName("idxoa")
        self.horizontalLayout_5.addWidget(self.idxoa)
        self.delid = QtWidgets.QPushButton(self.layoutWidget)
        self.delid.setMinimumSize(QtCore.QSize(0, 28))
        self.delid.setMaximumSize(QtCore.QSize(16777215, 28))
        self.delid.setObjectName("delid")
        self.horizontalLayout_5.addWidget(self.delid)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.hocphi_view = QtWidgets.QTableWidget(self.layoutWidget)
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
        self.verticalLayout_3.addWidget(self.hocphi_view)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.hoantat = QtWidgets.QPushButton(self.layoutWidget)
        self.hoantat.setObjectName("hoantat")
        self.verticalLayout_4.addWidget(self.hoantat)

        self.retranslateUi(ghinhanvadshp)
        QtCore.QMetaObject.connectSlotsByName(ghinhanvadshp)

    def retranslateUi(self, ghinhanvadshp):
        _translate = QtCore.QCoreApplication.translate
        ghinhanvadshp.setWindowTitle(_translate("ghinhanvadshp", "Ghi nhận đóng tiền học và danh sách học phí đã thu"))
        self.label.setText(_translate("ghinhanvadshp", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">DANH SÁCH HỌC PHÍ ĐÃ THU</span></p></body></html>"))
        self.label_2.setText(_translate("ghinhanvadshp", "Ngày / Tháng / Năm (DD/MM/YYYY)"))
        self.dateinfo.setDisplayFormat(_translate("ghinhanvadshp", "d/M/yyyy"))
        self.daysort.setText(_translate("ghinhanvadshp", "Lọc theo ngày + Tháng + Năm"))
        self.monthsort.setText(_translate("ghinhanvadshp", "Lọc theo tháng + năm"))
        self.yearsort.setText(_translate("ghinhanvadshp", "Lọc theo năm"))
        self.loc.setText(_translate("ghinhanvadshp", "Lọc dữ liệu"))
        self.label_3.setText(_translate("ghinhanvadshp", "Ghi nhận ID học phí đóng tiền"))
        self.saveinfo.setText(_translate("ghinhanvadshp", "Ghi nhận đóng học phí"))
        self.label_4.setText(_translate("ghinhanvadshp", "ID thu học phí để xóa"))
        self.delid.setText(_translate("ghinhanvadshp", "Xóa id ghi nhận nhầm"))
        item = self.hocphi_view.horizontalHeaderItem(0)
        item.setText(_translate("ghinhanvadshp", "ID thu học phí"))
        item = self.hocphi_view.horizontalHeaderItem(1)
        item.setText(_translate("ghinhanvadshp", "ID học phí"))
        item = self.hocphi_view.horizontalHeaderItem(2)
        item.setText(_translate("ghinhanvadshp", "Ngày thu"))
        item = self.hocphi_view.horizontalHeaderItem(3)
        item.setText(_translate("ghinhanvadshp", "Mã học sinh"))
        item = self.hocphi_view.horizontalHeaderItem(4)
        item.setText(_translate("ghinhanvadshp", "Họ tên học sinh"))
        item = self.hocphi_view.horizontalHeaderItem(5)
        item.setText(_translate("ghinhanvadshp", "Môn học"))
        item = self.hocphi_view.horizontalHeaderItem(6)
        item.setText(_translate("ghinhanvadshp", "Giáo viên"))
        self.hoantat.setText(_translate("ghinhanvadshp", "Hoàn tất"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ghinhanvadshp = QtWidgets.QWidget()
    ui = Ui_ghinhanvadshp()
    ui.setupUi(ghinhanvadshp)
    ghinhanvadshp.show()
    sys.exit(app.exec_())
