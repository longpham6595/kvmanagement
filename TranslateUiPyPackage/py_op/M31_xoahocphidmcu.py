# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M31_xoahocphidmcu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_xoahpdm(object):
    def setupUi(self, xoahpdm):
        xoahpdm.setObjectName("xoahpdm")
        xoahpdm.resize(1146, 601)
        self.layoutWidget = QtWidgets.QWidget(xoahpdm)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 1121, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QtCore.QSize(0, 22))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lop = QtWidgets.QSpinBox(self.layoutWidget)
        self.lop.setEnabled(True)
        self.lop.setMinimumSize(QtCore.QSize(0, 22))
        self.lop.setMaximumSize(QtCore.QSize(16777215, 22))
        self.lop.setMaximum(12)
        self.lop.setObjectName("lop")
        self.horizontalLayout_5.addWidget(self.lop)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.loc = QtWidgets.QPushButton(self.layoutWidget)
        self.loc.setObjectName("loc")
        self.horizontalLayout_6.addWidget(self.loc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.defhp_view = QtWidgets.QTableWidget(self.layoutWidget)
        self.defhp_view.setObjectName("defhp_view")
        self.defhp_view.setColumnCount(10)
        self.defhp_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.defhp_view.setHorizontalHeaderItem(9, item)
        self.defhp_view.verticalHeader().setVisible(False)
        self.defhp_view.verticalHeader().setHighlightSections(True)
        self.verticalLayout_3.addWidget(self.defhp_view)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.capnhat = QtWidgets.QPushButton(self.layoutWidget)
        self.capnhat.setEnabled(True)
        self.capnhat.setMinimumSize(QtCore.QSize(0, 28))
        self.capnhat.setMaximumSize(QtCore.QSize(16777215, 28))
        self.capnhat.setObjectName("capnhat")
        self.verticalLayout_2.addWidget(self.capnhat)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 44))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 44))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 41))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.delidhp = QtWidgets.QPushButton(self.layoutWidget)
        self.delidhp.setObjectName("delidhp")
        self.horizontalLayout_2.addWidget(self.delidhp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.hoantat = QtWidgets.QPushButton(self.layoutWidget)
        self.hoantat.setObjectName("hoantat")
        self.verticalLayout_3.addWidget(self.hoantat)

        self.retranslateUi(xoahpdm)
        QtCore.QMetaObject.connectSlotsByName(xoahpdm)

    def retranslateUi(self, xoahpdm):
        _translate = QtCore.QCoreApplication.translate
        xoahpdm.setWindowTitle(_translate("xoahpdm", "Xóa/sửa học phí định mức cũ và kiểm tra toàn bộ tình trạng học phí"))
        self.label.setText(_translate("xoahpdm", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">DANH MỤC HỌC PHÍ ĐỊNH MỨC</span></p></body></html>"))
        self.label_2.setText(_translate("xoahpdm", "<html><head/><body><p align=\"center\">Lớp</p></body></html>"))
        self.loc.setText(_translate("xoahpdm", "Lọc"))
        item = self.defhp_view.horizontalHeaderItem(0)
        item.setText(_translate("xoahpdm", "ID Học phí"))
        item = self.defhp_view.horizontalHeaderItem(1)
        item.setText(_translate("xoahpdm", "Mã học sinh"))
        item = self.defhp_view.horizontalHeaderItem(2)
        item.setText(_translate("xoahpdm", "Họ tên học sinh"))
        item = self.defhp_view.horizontalHeaderItem(3)
        item.setText(_translate("xoahpdm", "Mã môn học"))
        item = self.defhp_view.horizontalHeaderItem(4)
        item.setText(_translate("xoahpdm", "Học phí"))
        item = self.defhp_view.horizontalHeaderItem(5)
        item.setText(_translate("xoahpdm", "Mã giáo viên"))
        item = self.defhp_view.horizontalHeaderItem(6)
        item.setText(_translate("xoahpdm", "Số buổi/tháng"))
        item = self.defhp_view.horizontalHeaderItem(7)
        item.setText(_translate("xoahpdm", "Số lần đóng phí"))
        item = self.defhp_view.horizontalHeaderItem(8)
        item.setText(_translate("xoahpdm", "Số buổi đã học"))
        item = self.defhp_view.horizontalHeaderItem(9)
        item.setText(_translate("xoahpdm", "Tình trạng HP"))
        self.label_3.setText(_translate("xoahpdm", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">LƯU Ý: KHÔNG CẬP NHẬT DỮ LIỆU CÁC CỘT &quot;ID Học phí&quot;, &quot;Mã học sinh&quot;, &quot;Họ tên học sinh&quot;, &quot;Tình trạng HP&quot;</span></p></body></html>"))
        self.capnhat.setText(_translate("xoahpdm", "Cập nhật thủ công"))
        self.label_4.setText(_translate("xoahpdm", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">OPTION XÓA TOÀN BỘ MỘT LINE HỌC PHÍ VỚI ID HỌC PHÍ</span></p><p align=\"center\"><span style=\" font-weight:600;\">(Nhập các ID Học phí cách nhau một đấu phẩy &quot;,&quot;)</span></p></body></html>"))
        self.label_5.setText(_translate("xoahpdm", "ID Học phí cần xóa"))
        self.delidhp.setText(_translate("xoahpdm", "Xóa các ID"))
        self.hoantat.setText(_translate("xoahpdm", "Hoàn tất"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    xoahpdm = QtWidgets.QWidget()
    ui = Ui_xoahpdm()
    ui.setupUi(xoahpdm)
    xoahpdm.show()
    sys.exit(app.exec_())