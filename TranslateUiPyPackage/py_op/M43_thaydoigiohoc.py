# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M43_thaydoigiohoc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_thaydoighlh(object):
    def setupUi(self, thaydoighlh):
        thaydoighlh.setObjectName("thaydoighlh")
        thaydoighlh.resize(785, 524)
        self.gridLayout = QtWidgets.QGridLayout(thaydoighlh)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(thaydoighlh)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(thaydoighlh)
        self.label.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(thaydoighlh)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 7)
        self.label_13 = QtWidgets.QLabel(thaydoighlh)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 8)
        self.capnhat = QtWidgets.QPushButton(thaydoighlh)
        self.capnhat.setObjectName("capnhat")
        self.gridLayout.addWidget(self.capnhat, 17, 0, 1, 9)
        self.thaydoigiohoc_view = QtWidgets.QTableWidget(thaydoighlh)
        self.thaydoigiohoc_view.setMinimumSize(QtCore.QSize(280, 200))
        self.thaydoigiohoc_view.setObjectName("thaydoigiohoc_view")
        self.thaydoigiohoc_view.setColumnCount(3)
        self.thaydoigiohoc_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.thaydoigiohoc_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.thaydoigiohoc_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.thaydoigiohoc_view.setHorizontalHeaderItem(2, item)
        self.thaydoigiohoc_view.horizontalHeader().setMinimumSectionSize(0)
        self.thaydoigiohoc_view.verticalHeader().setVisible(False)
        self.thaydoigiohoc_view.verticalHeader().setMinimumSectionSize(0)
        self.gridLayout.addWidget(self.thaydoigiohoc_view, 18, 0, 1, 9)
        self.nhom = QtWidgets.QComboBox(thaydoighlh)
        self.nhom.setMaximumSize(QtCore.QSize(16777215, 22))
        self.nhom.setObjectName("nhom")
        self.gridLayout.addWidget(self.nhom, 3, 1, 1, 8)
        self.label_6 = QtWidgets.QLabel(thaydoighlh)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 3, 1, 3)
        self.label_10 = QtWidgets.QLabel(thaydoighlh)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 6, 1, 1)
        self.option_1_giohoc = QtWidgets.QTimeEdit(thaydoighlh)
        self.option_1_giohoc.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.option_1_giohoc.setObjectName("option_1_giohoc")
        self.gridLayout.addWidget(self.option_1_giohoc, 9, 1, 1, 1)
        self.hstrongnhom_view = QtWidgets.QLineEdit(thaydoighlh)
        self.hstrongnhom_view.setMaximumSize(QtCore.QSize(16777215, 22))
        self.hstrongnhom_view.setObjectName("hstrongnhom_view")
        self.gridLayout.addWidget(self.hstrongnhom_view, 4, 1, 1, 8)
        self.label_4 = QtWidgets.QLabel(thaydoighlh)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(thaydoighlh)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(thaydoighlh)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.option_1_chonbuoihoc = QtWidgets.QComboBox(thaydoighlh)
        self.option_1_chonbuoihoc.setObjectName("option_1_chonbuoihoc")
        self.option_1_chonbuoihoc.addItem("")
        self.option_1_chonbuoihoc.addItem("")
        self.option_1_chonbuoihoc.addItem("")
        self.option_1_chonbuoihoc.addItem("")
        self.option_1_chonbuoihoc.addItem("")
        self.option_1_chonbuoihoc.addItem("")
        self.option_1_chonbuoihoc.addItem("")
        self.gridLayout.addWidget(self.option_1_chonbuoihoc, 8, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(thaydoighlh)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 10, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(thaydoighlh)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 3, 1, 1)
        self.option_2_buoihoc = QtWidgets.QComboBox(thaydoighlh)
        self.option_2_buoihoc.setObjectName("option_2_buoihoc")
        self.option_2_buoihoc.addItem("")
        self.option_2_buoihoc.addItem("")
        self.option_2_buoihoc.addItem("")
        self.option_2_buoihoc.addItem("")
        self.option_2_buoihoc.addItem("")
        self.option_2_buoihoc.addItem("")
        self.option_2_buoihoc.addItem("")
        self.gridLayout.addWidget(self.option_2_buoihoc, 8, 7, 1, 2)
        self.option_idcapnhat = QtWidgets.QComboBox(thaydoighlh)
        self.option_idcapnhat.setObjectName("option_idcapnhat")
        self.gridLayout.addWidget(self.option_idcapnhat, 9, 7, 1, 2)
        self.option_2_giohoc = QtWidgets.QTimeEdit(thaydoighlh)
        self.option_2_giohoc.setObjectName("option_2_giohoc")
        self.gridLayout.addWidget(self.option_2_giohoc, 10, 7, 1, 2)
        self.capnhatgiohoc = QtWidgets.QPushButton(thaydoighlh)
        self.capnhatgiohoc.setObjectName("capnhatgiohoc")
        self.gridLayout.addWidget(self.capnhatgiohoc, 11, 7, 1, 2)
        self.option_idxoa = QtWidgets.QComboBox(thaydoighlh)
        self.option_idxoa.setObjectName("option_idxoa")
        self.gridLayout.addWidget(self.option_idxoa, 8, 4, 1, 2)
        self.xoagiohoc = QtWidgets.QPushButton(thaydoighlh)
        self.xoagiohoc.setMaximumSize(QtCore.QSize(500, 28))
        self.xoagiohoc.setObjectName("xoagiohoc")
        self.gridLayout.addWidget(self.xoagiohoc, 11, 4, 1, 2)
        self.themgiohoc = QtWidgets.QPushButton(thaydoighlh)
        self.themgiohoc.setMaximumSize(QtCore.QSize(195, 28))
        self.themgiohoc.setObjectName("themgiohoc")
        self.gridLayout.addWidget(self.themgiohoc, 11, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(thaydoighlh)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 6, 1, 3)
        self.label_7 = QtWidgets.QLabel(thaydoighlh)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 2)
        self.hoantat = QtWidgets.QPushButton(thaydoighlh)
        self.hoantat.setObjectName("hoantat")
        self.gridLayout.addWidget(self.hoantat, 19, 0, 1, 9)
        self.locchuatkb = QtWidgets.QPushButton(thaydoighlh)
        self.locchuatkb.setObjectName("locchuatkb")
        self.gridLayout.addWidget(self.locchuatkb, 2, 4, 1, 5)
        self.locall = QtWidgets.QPushButton(thaydoighlh)
        self.locall.setObjectName("locall")
        self.gridLayout.addWidget(self.locall, 2, 0, 1, 4)

        self.retranslateUi(thaydoighlh)
        QtCore.QMetaObject.connectSlotsByName(thaydoighlh)

    def retranslateUi(self, thaydoighlh):
        _translate = QtCore.QCoreApplication.translate
        thaydoighlh.setWindowTitle(_translate("thaydoighlh", "Form"))
        self.label_5.setText(_translate("thaydoighlh", "Nhóm này bao gồm các học sinh"))
        self.label.setText(_translate("thaydoighlh", "Chọn nhóm"))
        self.label_8.setText(_translate("thaydoighlh", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Chọn nhóm để chỉnh sửa giờ học</span></p></body></html>"))
        self.label_13.setText(_translate("thaydoighlh", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">BẢNG THÊM VÀ THAY ĐỔI GIỜ HỌC</span></p></body></html>"))
        self.capnhat.setText(_translate("thaydoighlh", "Cập nhật thời khóa biểu sau khi thực hiện thay đổi"))
        item = self.thaydoigiohoc_view.horizontalHeaderItem(0)
        item.setText(_translate("thaydoighlh", "ID giờ học"))
        item = self.thaydoigiohoc_view.horizontalHeaderItem(1)
        item.setText(_translate("thaydoighlh", "Buổi học"))
        item = self.thaydoigiohoc_view.horizontalHeaderItem(2)
        item.setText(_translate("thaydoighlh", "Giờ học"))
        self.label_6.setText(_translate("thaydoighlh", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Xóa giờ học đã có</span></p></body></html>"))
        self.label_10.setText(_translate("thaydoighlh", "Chọn id giờ học cần cập nhật"))
        self.label_4.setText(_translate("thaydoighlh", "Chọn giờ học"))
        self.label_11.setText(_translate("thaydoighlh", "Nhập buổi học mới"))
        self.label_3.setText(_translate("thaydoighlh", "Chọn buổi học cần thêm"))
        self.option_1_chonbuoihoc.setItemText(0, _translate("thaydoighlh", "Thứ hai"))
        self.option_1_chonbuoihoc.setItemText(1, _translate("thaydoighlh", "Thứ ba"))
        self.option_1_chonbuoihoc.setItemText(2, _translate("thaydoighlh", "Thứ tư"))
        self.option_1_chonbuoihoc.setItemText(3, _translate("thaydoighlh", "Thứ năm"))
        self.option_1_chonbuoihoc.setItemText(4, _translate("thaydoighlh", "Thứ sáu"))
        self.option_1_chonbuoihoc.setItemText(5, _translate("thaydoighlh", "Thứ bảy"))
        self.option_1_chonbuoihoc.setItemText(6, _translate("thaydoighlh", "Chủ nhật"))
        self.label_12.setText(_translate("thaydoighlh", "Nhập giờ học mới"))
        self.label_2.setText(_translate("thaydoighlh", "Chọn id giờ học cần xóa"))
        self.option_2_buoihoc.setItemText(0, _translate("thaydoighlh", "Thứ hai"))
        self.option_2_buoihoc.setItemText(1, _translate("thaydoighlh", "Thứ ba"))
        self.option_2_buoihoc.setItemText(2, _translate("thaydoighlh", "Thứ tư"))
        self.option_2_buoihoc.setItemText(3, _translate("thaydoighlh", "Thứ năm"))
        self.option_2_buoihoc.setItemText(4, _translate("thaydoighlh", "Thứ sáu"))
        self.option_2_buoihoc.setItemText(5, _translate("thaydoighlh", "Thứ bảy"))
        self.option_2_buoihoc.setItemText(6, _translate("thaydoighlh", "Chủ nhật"))
        self.capnhatgiohoc.setText(_translate("thaydoighlh", "Cập nhật giờ học"))
        self.xoagiohoc.setText(_translate("thaydoighlh", "Xóa giờ học"))
        self.themgiohoc.setText(_translate("thaydoighlh", "Thêm giờ học vào thời khóa biểu"))
        self.label_9.setText(_translate("thaydoighlh", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Cập nhật giờ học cũ</span></p></body></html>"))
        self.label_7.setText(_translate("thaydoighlh", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Thêm giờ học mới</span></p></body></html>"))
        self.hoantat.setText(_translate("thaydoighlh", "Hoàn tất"))
        self.locchuatkb.setText(_translate("thaydoighlh", "Hiển thị các nhóm mới chưa có thời khóa biểu"))
        self.locall.setText(_translate("thaydoighlh", "Hiển thị toàn bộ mọi nhóm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thaydoighlh = QtWidgets.QWidget()
    ui = Ui_thaydoighlh()
    ui.setupUi(thaydoighlh)
    thaydoighlh.show()
    sys.exit(app.exec_())
