# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M42_thaydoihstrongnhom.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_thaydoitthstrongnhom(object):
    def setupUi(self, thaydoitthstrongnhom):
        thaydoitthstrongnhom.setObjectName("thaydoitthstrongnhom")
        thaydoitthstrongnhom.resize(470, 450)
        thaydoitthstrongnhom.setMinimumSize(QtCore.QSize(470, 450))
        self.gridLayout = QtWidgets.QGridLayout(thaydoitthstrongnhom)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(thaydoitthstrongnhom)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.xoahs = QtWidgets.QPushButton(thaydoitthstrongnhom)
        self.xoahs.setObjectName("xoahs")
        self.gridLayout.addWidget(self.xoahs, 7, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(thaydoitthstrongnhom)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(thaydoitthstrongnhom)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.ths = QtWidgets.QPushButton(thaydoitthstrongnhom)
        self.ths.setObjectName("ths")
        self.gridLayout.addWidget(self.ths, 6, 6, 1, 1)
        self.viewhs = QtWidgets.QPushButton(thaydoitthstrongnhom)
        self.viewhs.setObjectName("viewhs")
        self.gridLayout.addWidget(self.viewhs, 5, 6, 1, 1)
        self.dstoanbonhom = QtWidgets.QPushButton(thaydoitthstrongnhom)
        self.dstoanbonhom.setObjectName("dstoanbonhom")
        self.gridLayout.addWidget(self.dstoanbonhom, 1, 0, 1, 3)
        self.dshocsinhtheonhom_view = QtWidgets.QTableWidget(thaydoitthstrongnhom)
        self.dshocsinhtheonhom_view.setObjectName("dshocsinhtheonhom_view")
        self.dshocsinhtheonhom_view.setColumnCount(4)
        self.dshocsinhtheonhom_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dshocsinhtheonhom_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dshocsinhtheonhom_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dshocsinhtheonhom_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dshocsinhtheonhom_view.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.dshocsinhtheonhom_view, 8, 0, 1, 7)
        self.locmanhommoi = QtWidgets.QPushButton(thaydoitthstrongnhom)
        self.locmanhommoi.setObjectName("locmanhommoi")
        self.gridLayout.addWidget(self.locmanhommoi, 1, 3, 1, 4)
        self.option_manhommoi = QtWidgets.QComboBox(thaydoitthstrongnhom)
        self.option_manhommoi.setObjectName("option_manhommoi")
        self.gridLayout.addWidget(self.option_manhommoi, 5, 1, 1, 5)
        self.option_chonhsthem = QtWidgets.QComboBox(thaydoitthstrongnhom)
        self.option_chonhsthem.setObjectName("option_chonhsthem")
        self.gridLayout.addWidget(self.option_chonhsthem, 6, 1, 1, 5)
        self.option_chonhsxoa = QtWidgets.QComboBox(thaydoitthstrongnhom)
        self.option_chonhsxoa.setObjectName("option_chonhsxoa")
        self.gridLayout.addWidget(self.option_chonhsxoa, 7, 1, 1, 5)
        self.label_4 = QtWidgets.QLabel(thaydoitthstrongnhom)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 7)
        self.hoantat = QtWidgets.QPushButton(thaydoitthstrongnhom)
        self.hoantat.setObjectName("hoantat")
        self.gridLayout.addWidget(self.hoantat, 9, 0, 1, 7)

        self.retranslateUi(thaydoitthstrongnhom)
        QtCore.QMetaObject.connectSlotsByName(thaydoitthstrongnhom)

    def retranslateUi(self, thaydoitthstrongnhom):
        _translate = QtCore.QCoreApplication.translate
        thaydoitthstrongnhom.setWindowTitle(_translate("thaydoitthstrongnhom", "Thay đổi thông tin học sinh trong nhóm"))
        self.label.setText(_translate("thaydoitthstrongnhom", "Mã nhóm"))
        self.xoahs.setText(_translate("thaydoitthstrongnhom", "Xóa học sinh khỏi nhóm"))
        self.label_2.setText(_translate("thaydoitthstrongnhom", "Chọn học sinh chưa thuộc nhóm"))
        self.label_3.setText(_translate("thaydoitthstrongnhom", "Chọn học sinh để xóa khỏi nhóm"))
        self.ths.setText(_translate("thaydoitthstrongnhom", "Thêm học sinh vào nhóm"))
        self.viewhs.setText(_translate("thaydoitthstrongnhom", "Hiển thị học sinh trong nhóm"))
        self.dstoanbonhom.setText(_translate("thaydoitthstrongnhom", "Hiển thị danh sách tất cả các nhóm"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(0)
        item.setText(_translate("thaydoitthstrongnhom", "Mã học sinh"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(1)
        item.setText(_translate("thaydoitthstrongnhom", "Tên học sinh"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(2)
        item.setText(_translate("thaydoitthstrongnhom", "Mã nhóm"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(3)
        item.setText(_translate("thaydoitthstrongnhom", "GV phụ trách"))
        self.locmanhommoi.setText(_translate("thaydoitthstrongnhom", "Lọc các mã nhóm chưa có học sinh"))
        self.label_4.setText(_translate("thaydoitthstrongnhom", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">THAY ĐỔI THÔNG TIN HỌC SINH TRONG NHÓM</span></p></body></html>"))
        self.hoantat.setText(_translate("thaydoitthstrongnhom", "Hoàn tất"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thaydoitthstrongnhom = QtWidgets.QWidget()
    ui = Ui_thaydoitthstrongnhom()
    ui.setupUi(thaydoitthstrongnhom)
    thaydoitthstrongnhom.show()
    sys.exit(app.exec_())
