# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M14_thongkediemdanh.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tkdiemdanhhs(object):
    def setupUi(self, tkdiemdanhhs):
        tkdiemdanhhs.setObjectName("tkdiemdanhhs")
        tkdiemdanhhs.resize(780, 300)
        tkdiemdanhhs.setMinimumSize(QtCore.QSize(780, 300))
        self.gridLayout = QtWidgets.QGridLayout(tkdiemdanhhs)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(tkdiemdanhhs)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.datestart = QtWidgets.QDateEdit(tkdiemdanhhs)
        self.datestart.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.datestart.setObjectName("datestart")
        self.gridLayout.addWidget(self.datestart, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(tkdiemdanhhs)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.datefin = QtWidgets.QDateEdit(tkdiemdanhhs)
        self.datefin.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.datefin.setObjectName("datefin")
        self.gridLayout.addWidget(self.datefin, 1, 3, 1, 1)
        self.tbdiemdanh_view = QtWidgets.QTableWidget(tkdiemdanhhs)
        self.tbdiemdanh_view.setObjectName("tbdiemdanh_view")
        self.tbdiemdanh_view.setColumnCount(6)
        self.tbdiemdanh_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbdiemdanh_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbdiemdanh_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbdiemdanh_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbdiemdanh_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbdiemdanh_view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbdiemdanh_view.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tbdiemdanh_view, 3, 0, 1, 4)
        self.hoantat = QtWidgets.QPushButton(tkdiemdanhhs)
        self.hoantat.setObjectName("hoantat")
        self.gridLayout.addWidget(self.hoantat, 4, 0, 1, 4)
        self.loc = QtWidgets.QPushButton(tkdiemdanhhs)
        self.loc.setObjectName("loc")
        self.gridLayout.addWidget(self.loc, 2, 0, 1, 4)
        self.label = QtWidgets.QLabel(tkdiemdanhhs)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.retranslateUi(tkdiemdanhhs)
        QtCore.QMetaObject.connectSlotsByName(tkdiemdanhhs)

    def retranslateUi(self, tkdiemdanhhs):
        _translate = QtCore.QCoreApplication.translate
        tkdiemdanhhs.setWindowTitle(_translate("tkdiemdanhhs", "Thống kê điểm danh học sinh"))
        self.label_2.setText(_translate("tkdiemdanhhs", "Ngày bắt đầu (dd/mm/yyyy)"))
        self.datestart.setDisplayFormat(_translate("tkdiemdanhhs", "d/M/yyyy"))
        self.label_3.setText(_translate("tkdiemdanhhs", "Ngày kết thúc (dd/mm/yyyy)"))
        self.datefin.setDisplayFormat(_translate("tkdiemdanhhs", "d/M/yyyy"))
        item = self.tbdiemdanh_view.horizontalHeaderItem(0)
        item.setText(_translate("tkdiemdanhhs", "ID Điểm danh"))
        item = self.tbdiemdanh_view.horizontalHeaderItem(1)
        item.setText(_translate("tkdiemdanhhs", "Mã Học sinh"))
        item = self.tbdiemdanh_view.horizontalHeaderItem(2)
        item.setText(_translate("tkdiemdanhhs", "Tên Học sinh"))
        item = self.tbdiemdanh_view.horizontalHeaderItem(3)
        item.setText(_translate("tkdiemdanhhs", "Mã Môn học"))
        item = self.tbdiemdanh_view.horizontalHeaderItem(4)
        item.setText(_translate("tkdiemdanhhs", "Mã Nhóm"))
        item = self.tbdiemdanh_view.horizontalHeaderItem(5)
        item.setText(_translate("tkdiemdanhhs", "Ngày giờ học"))
        self.hoantat.setText(_translate("tkdiemdanhhs", "Hoàn tất"))
        self.loc.setText(_translate("tkdiemdanhhs", "Lọc"))
        self.label.setText(_translate("tkdiemdanhhs", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">THỐNG KÊ TOÀN BỘ THÔNG TIN ĐIỂM DANH</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tkdiemdanhhs = QtWidgets.QWidget()
    ui = Ui_tkdiemdanhhs()
    ui.setupUi(tkdiemdanhhs)
    tkdiemdanhhs.show()
    sys.exit(app.exec_())
