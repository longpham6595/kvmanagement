# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M51_bangchiluonggv.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bclgiaovien(object):
    def setupUi(self, bclgiaovien):
        bclgiaovien.setObjectName("bclgiaovien")
        bclgiaovien.resize(1041, 531)
        self.layoutWidget = QtWidgets.QWidget(bclgiaovien)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 1021, 511))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.thang = QtWidgets.QSpinBox(self.layoutWidget)
        self.thang.setMinimum(1)
        self.thang.setMaximum(12)
        self.thang.setObjectName("thang")
        self.horizontalLayout_2.addWidget(self.thang)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.nam = QtWidgets.QSpinBox(self.layoutWidget)
        self.nam.setMinimum(2000)
        self.nam.setMaximum(3000)
        self.nam.setProperty("value", 2020)
        self.nam.setObjectName("nam")
        self.horizontalLayout_2.addWidget(self.nam)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.locoption = QtWidgets.QRadioButton(self.layoutWidget)
        self.locoption.setObjectName("locoption")
        self.horizontalLayout.addWidget(self.locoption)
        self.locall = QtWidgets.QRadioButton(self.layoutWidget)
        self.locall.setObjectName("locall")
        self.horizontalLayout.addWidget(self.locall)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.magv = QtWidgets.QComboBox(self.layoutWidget)
        self.magv.setObjectName("magv")
        self.horizontalLayout_3.addWidget(self.magv)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.loc = QtWidgets.QPushButton(self.layoutWidget)
        self.loc.setObjectName("loc")
        self.verticalLayout.addWidget(self.loc)
        self.payment_view = QtWidgets.QTableWidget(self.layoutWidget)
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
        self.verticalLayout.addWidget(self.payment_view)
        self.hoantat = QtWidgets.QPushButton(self.layoutWidget)
        self.hoantat.setObjectName("hoantat")
        self.verticalLayout.addWidget(self.hoantat)

        self.retranslateUi(bclgiaovien)
        QtCore.QMetaObject.connectSlotsByName(bclgiaovien)

    def retranslateUi(self, bclgiaovien):
        _translate = QtCore.QCoreApplication.translate
        bclgiaovien.setWindowTitle(_translate("bclgiaovien", "Bảng chi lương giáo viên"))
        self.label_3.setText(_translate("bclgiaovien", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">BẢNG CHI LƯƠNG GIÁO VIÊN</span></p></body></html>"))
        self.label.setText(_translate("bclgiaovien", "Chọn tháng"))
        self.label_2.setText(_translate("bclgiaovien", "Chọn năm"))
        self.locoption.setText(_translate("bclgiaovien", "Lọc theo mã giáo viên dưới đây"))
        self.locall.setText(_translate("bclgiaovien", "Hiển thị tất cả giáo viên"))
        self.label_4.setText(_translate("bclgiaovien", "Chọn mã giáo viên"))
        self.loc.setText(_translate("bclgiaovien", "Lọc"))
        item = self.payment_view.horizontalHeaderItem(0)
        item.setText(_translate("bclgiaovien", "Mã giáo viên"))
        item = self.payment_view.horizontalHeaderItem(1)
        item.setText(_translate("bclgiaovien", "Tên giáo viên"))
        item = self.payment_view.horizontalHeaderItem(2)
        item.setText(_translate("bclgiaovien", "Hệ số lương"))
        item = self.payment_view.horizontalHeaderItem(3)
        item.setText(_translate("bclgiaovien", "Lương theo hệ số"))
        item = self.payment_view.horizontalHeaderItem(4)
        item.setText(_translate("bclgiaovien", "Lương cứng"))
        item = self.payment_view.horizontalHeaderItem(5)
        item.setText(_translate("bclgiaovien", "Tổng thu nhập"))
        item = self.payment_view.horizontalHeaderItem(6)
        item.setText(_translate("bclgiaovien", "Lương đã ứng"))
        item = self.payment_view.horizontalHeaderItem(7)
        item.setText(_translate("bclgiaovien", "Lương tích lũy"))
        self.hoantat.setText(_translate("bclgiaovien", "Hoàn tất"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bclgiaovien = QtWidgets.QWidget()
    ui = Ui_bclgiaovien()
    ui.setupUi(bclgiaovien)
    bclgiaovien.show()
    sys.exit(app.exec_())