# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M11_locdiemdanhPop.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_locdiemdanh(object):
    def setupUi(self, locdiemdanh):
        locdiemdanh.setObjectName("locdiemdanh")
        locdiemdanh.resize(1161, 721)
        self.layoutWidget = QtWidgets.QWidget(locdiemdanh)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1141, 701))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lop = QtWidgets.QLabel(self.layoutWidget)
        self.lop.setMinimumSize(QtCore.QSize(55, 0))
        self.lop.setObjectName("lop")
        self.horizontalLayout_2.addWidget(self.lop)
        self.combo_lop = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_lop.setObjectName("combo_lop")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.combo_lop.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_lop)
        self.giaovien = QtWidgets.QLabel(self.layoutWidget)
        self.giaovien.setMinimumSize(QtCore.QSize(55, 0))
        self.giaovien.setObjectName("giaovien")
        self.horizontalLayout_2.addWidget(self.giaovien)
        self.combo_giaovien = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_giaovien.setObjectName("combo_giaovien")
        self.horizontalLayout_2.addWidget(self.combo_giaovien)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.nhom = QtWidgets.QLabel(self.layoutWidget)
        self.nhom.setMinimumSize(QtCore.QSize(55, 0))
        self.nhom.setObjectName("nhom")
        self.verticalLayout.addWidget(self.nhom)
        self.combo_nhom = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_nhom.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_nhom.sizePolicy().hasHeightForWidth())
        self.combo_nhom.setSizePolicy(sizePolicy)
        self.combo_nhom.setObjectName("combo_nhom")
        self.verticalLayout.addWidget(self.combo_nhom)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buoihoc = QtWidgets.QLabel(self.layoutWidget)
        self.buoihoc.setMinimumSize(QtCore.QSize(55, 0))
        self.buoihoc.setObjectName("buoihoc")
        self.horizontalLayout.addWidget(self.buoihoc)
        self.combo_buoihoc = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_buoihoc.setObjectName("combo_buoihoc")
        self.combo_buoihoc.addItem("")
        self.combo_buoihoc.addItem("")
        self.combo_buoihoc.addItem("")
        self.combo_buoihoc.addItem("")
        self.combo_buoihoc.addItem("")
        self.combo_buoihoc.addItem("")
        self.combo_buoihoc.addItem("")
        self.combo_buoihoc.addItem("")
        self.horizontalLayout.addWidget(self.combo_buoihoc)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.ngaydd = QtWidgets.QDateEdit(self.layoutWidget)
        self.ngaydd.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.ngaydd.setObjectName("ngaydd")
        self.horizontalLayout.addWidget(self.ngaydd)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.giohoc = QtWidgets.QSpinBox(self.layoutWidget)
        self.giohoc.setMaximum(24)
        self.giohoc.setObjectName("giohoc")
        self.horizontalLayout.addWidget(self.giohoc)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.phuthoc = QtWidgets.QSpinBox(self.layoutWidget)
        self.phuthoc.setMaximum(60)
        self.phuthoc.setObjectName("phuthoc")
        self.horizontalLayout.addWidget(self.phuthoc)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.cb_xoadiemdanh = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_xoadiemdanh.setObjectName("cb_xoadiemdanh")
        self.horizontalLayout_5.addWidget(self.cb_xoadiemdanh)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.ipidxoa = QtWidgets.QLineEdit(self.layoutWidget)
        self.ipidxoa.setObjectName("ipidxoa")
        self.horizontalLayout_4.addWidget(self.ipidxoa)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.loc = QtWidgets.QPushButton(self.layoutWidget)
        self.loc.setObjectName("loc")
        self.verticalLayout_2.addWidget(self.loc)
        self.diemdanh_view = QtWidgets.QTableWidget(self.layoutWidget)
        self.diemdanh_view.setObjectName("diemdanh_view")
        self.diemdanh_view.setColumnCount(10)
        self.diemdanh_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.diemdanh_view.setHorizontalHeaderItem(9, item)
        self.verticalLayout_2.addWidget(self.diemdanh_view)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.xndiemdanh = QtWidgets.QPushButton(self.layoutWidget)
        self.xndiemdanh.setObjectName("xndiemdanh")
        self.verticalLayout_2.addWidget(self.xndiemdanh)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.xoadiemdanh = QtWidgets.QPushButton(self.layoutWidget)
        self.xoadiemdanh.setObjectName("xoadiemdanh")
        self.verticalLayout_2.addWidget(self.xoadiemdanh)
        self.hoantat = QtWidgets.QPushButton(self.layoutWidget)
        self.hoantat.setObjectName("hoantat")
        self.verticalLayout_2.addWidget(self.hoantat)

        self.retranslateUi(locdiemdanh)
        QtCore.QMetaObject.connectSlotsByName(locdiemdanh)

    def retranslateUi(self, locdiemdanh):
        _translate = QtCore.QCoreApplication.translate
        locdiemdanh.setWindowTitle(_translate("locdiemdanh", "Lọc Điểm Danh"))
        self.lop.setText(_translate("locdiemdanh", "<html><head/><body><p align=\"center\">Lớp (0 hiển thị toàn bộ)</p></body></html>"))
        self.combo_lop.setCurrentText(_translate("locdiemdanh", "0"))
        self.combo_lop.setItemText(0, _translate("locdiemdanh", "0"))
        self.combo_lop.setItemText(1, _translate("locdiemdanh", "1"))
        self.combo_lop.setItemText(2, _translate("locdiemdanh", "2"))
        self.combo_lop.setItemText(3, _translate("locdiemdanh", "3"))
        self.combo_lop.setItemText(4, _translate("locdiemdanh", "4"))
        self.combo_lop.setItemText(5, _translate("locdiemdanh", "5"))
        self.combo_lop.setItemText(6, _translate("locdiemdanh", "6"))
        self.combo_lop.setItemText(7, _translate("locdiemdanh", "7"))
        self.combo_lop.setItemText(8, _translate("locdiemdanh", "8"))
        self.combo_lop.setItemText(9, _translate("locdiemdanh", "9"))
        self.combo_lop.setItemText(10, _translate("locdiemdanh", "10"))
        self.combo_lop.setItemText(11, _translate("locdiemdanh", "11"))
        self.combo_lop.setItemText(12, _translate("locdiemdanh", "12"))
        self.giaovien.setText(_translate("locdiemdanh", "<html><head/><body><p align=\"center\">Giáo Viên</p></body></html>"))
        self.nhom.setText(_translate("locdiemdanh", "<html><head/><body><p align=\"center\">Nhóm</p></body></html>"))
        self.buoihoc.setText(_translate("locdiemdanh", "<html><head/><body><p align=\"center\">Buổi học (Chọn 0 khi lọc toàn bộ)</p></body></html>"))
        self.combo_buoihoc.setItemText(0, _translate("locdiemdanh", "0"))
        self.combo_buoihoc.setItemText(1, _translate("locdiemdanh", "Thứ hai"))
        self.combo_buoihoc.setItemText(2, _translate("locdiemdanh", "Thứ ba"))
        self.combo_buoihoc.setItemText(3, _translate("locdiemdanh", "Thứ tư"))
        self.combo_buoihoc.setItemText(4, _translate("locdiemdanh", "Thứ năm"))
        self.combo_buoihoc.setItemText(5, _translate("locdiemdanh", "Thứ sáu"))
        self.combo_buoihoc.setItemText(6, _translate("locdiemdanh", "Thứ bảy"))
        self.combo_buoihoc.setItemText(7, _translate("locdiemdanh", "Chủ nhật"))
        self.label_5.setText(_translate("locdiemdanh", "Ngày điểm danh (dd/mm/yyyy)"))
        self.ngaydd.setDisplayFormat(_translate("locdiemdanh", "dd/M/yyyy"))
        self.label.setText(_translate("locdiemdanh", "<html><head/><body><p align=\"center\">Giờ học (24 giờ) (Chọn 0:0 khi lọc toàn bộ)<br/>Chọn giờ sớm hơn giờ bắt đầu nhóm để hiện nhóm</p></body></html>"))
        self.label_2.setText(_translate("locdiemdanh", "h"))
        self.label_3.setText(_translate("locdiemdanh", "phút"))
        self.label_6.setText(_translate("locdiemdanh", "<html><head/><body><p>Lọc để xóa điểm danh nhầm (lọc theo ngày điểm danh được chọn)</p><p>(Chọn để lọc xóa điểm danh ghi nhầm, không chọn để lọc điểm danh)</p></body></html>"))
        self.cb_xoadiemdanh.setText(_translate("locdiemdanh", "Lọc điểm danh nhầm"))
        self.label_7.setText(_translate("locdiemdanh", "<html><head/><body><p>Chọn các ID Điểm danh nhầm</p><p>(nhập cách nhau bởi dấu phẩy - &quot;,&quot;)</p></body></html>"))
        self.loc.setText(_translate("locdiemdanh", "Lọc"))
        item = self.diemdanh_view.horizontalHeaderItem(0)
        item.setText(_translate("locdiemdanh", "Mã HS"))
        item = self.diemdanh_view.horizontalHeaderItem(1)
        item.setText(_translate("locdiemdanh", "Họ tên"))
        item = self.diemdanh_view.horizontalHeaderItem(2)
        item.setText(_translate("locdiemdanh", "Nhóm"))
        item = self.diemdanh_view.horizontalHeaderItem(3)
        item.setText(_translate("locdiemdanh", "Buổi học TKB"))
        item = self.diemdanh_view.horizontalHeaderItem(4)
        item.setText(_translate("locdiemdanh", "Ngày điểm danh"))
        item = self.diemdanh_view.horizontalHeaderItem(5)
        item.setText(_translate("locdiemdanh", "Thứ điểm danh"))
        item = self.diemdanh_view.horizontalHeaderItem(6)
        item.setText(_translate("locdiemdanh", "Giờ bắt đầu"))
        item = self.diemdanh_view.horizontalHeaderItem(7)
        item.setText(_translate("locdiemdanh", "GV phụ trách"))
        item = self.diemdanh_view.horizontalHeaderItem(8)
        item.setText(_translate("locdiemdanh", "Điểm danh"))
        item = self.diemdanh_view.horizontalHeaderItem(9)
        item.setText(_translate("locdiemdanh", "ID Điểm danh"))
        self.label_4.setText(_translate("locdiemdanh", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Chờ lọc??</span></p></body></html>"))
        self.xndiemdanh.setText(_translate("locdiemdanh", "Xác nhận điểm danh"))
        self.label_8.setText(_translate("locdiemdanh", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Chỉ xác nhận điểm danh khi Buổi học TKB và Thứ điểm danh TRÙNG NHAU</span></p></body></html>"))
        self.xoadiemdanh.setText(_translate("locdiemdanh", "Xóa điểm danh nhầm"))
        self.hoantat.setText(_translate("locdiemdanh", "Hoàn tất"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    locdiemdanh = QtWidgets.QDialog()
    ui = Ui_locdiemdanh()
    ui.setupUi(locdiemdanh)
    locdiemdanh.show()
    sys.exit(app.exec_())