# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M42_thaydoihstrongnhom.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_thaydoitthstrongnhom(object):
    def setupUi(self, thaydoitthstrongnhom):
        thaydoitthstrongnhom.setObjectName("thaydoitthstrongnhom")
        thaydoitthstrongnhom.resize(996, 572)
        self.layoutWidget = QtWidgets.QWidget(thaydoitthstrongnhom)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 981, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dstoanbonhom = QtWidgets.QPushButton(self.layoutWidget)
        self.dstoanbonhom.setObjectName("dstoanbonhom")
        self.horizontalLayout_2.addWidget(self.dstoanbonhom)
        self.locmanhommoi = QtWidgets.QPushButton(self.layoutWidget)
        self.locmanhommoi.setObjectName("locmanhommoi")
        self.horizontalLayout_2.addWidget(self.locmanhommoi)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.option_manhommoi = QtWidgets.QComboBox(self.layoutWidget)
        self.option_manhommoi.setObjectName("option_manhommoi")
        self.horizontalLayout.addWidget(self.option_manhommoi)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.viewhs = QtWidgets.QPushButton(self.layoutWidget)
        self.viewhs.setObjectName("viewhs")
        self.horizontalLayout_2.addWidget(self.viewhs)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.option_chonhsthem = QtWidgets.QComboBox(self.layoutWidget)
        self.option_chonhsthem.setObjectName("option_chonhsthem")
        self.horizontalLayout_3.addWidget(self.option_chonhsthem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.option_chonhsxoa = QtWidgets.QComboBox(self.layoutWidget)
        self.option_chonhsxoa.setObjectName("option_chonhsxoa")
        self.horizontalLayout_4.addWidget(self.option_chonhsxoa)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ths = QtWidgets.QPushButton(self.layoutWidget)
        self.ths.setObjectName("ths")
        self.verticalLayout_2.addWidget(self.ths)
        self.xoahs = QtWidgets.QPushButton(self.layoutWidget)
        self.xoahs.setObjectName("xoahs")
        self.verticalLayout_2.addWidget(self.xoahs)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.dshocsinhtheonhom_view = QtWidgets.QTableWidget(self.layoutWidget)
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
        self.verticalLayout_4.addWidget(self.dshocsinhtheonhom_view)
        self.hoantat = QtWidgets.QPushButton(self.layoutWidget)
        self.hoantat.setObjectName("hoantat")
        self.verticalLayout_4.addWidget(self.hoantat)

        self.retranslateUi(thaydoitthstrongnhom)
        QtCore.QMetaObject.connectSlotsByName(thaydoitthstrongnhom)

    def retranslateUi(self, thaydoitthstrongnhom):
        _translate = QtCore.QCoreApplication.translate
        thaydoitthstrongnhom.setWindowTitle(_translate("thaydoitthstrongnhom", "Thay đổi thông tin học sinh trong nhóm"))
        self.label_4.setText(_translate("thaydoitthstrongnhom", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">THAY ĐỔI THÔNG TIN HỌC SINH TRONG NHÓM</span></p></body></html>"))
        self.dstoanbonhom.setText(_translate("thaydoitthstrongnhom", "Hiển thị danh sách tất cả các nhóm"))
        self.locmanhommoi.setText(_translate("thaydoitthstrongnhom", "Lọc các mã nhóm chưa có học sinh"))
        self.label.setText(_translate("thaydoitthstrongnhom", "Mã nhóm"))
        self.viewhs.setText(_translate("thaydoitthstrongnhom", "Hiển thị học sinh trong nhóm"))
        self.label_2.setText(_translate("thaydoitthstrongnhom", "Chọn học sinh chưa thuộc nhóm"))
        self.label_3.setText(_translate("thaydoitthstrongnhom", "Chọn học sinh để xóa khỏi nhóm"))
        self.ths.setText(_translate("thaydoitthstrongnhom", "Thêm học sinh vào nhóm"))
        self.xoahs.setText(_translate("thaydoitthstrongnhom", "Xóa học sinh khỏi nhóm"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(0)
        item.setText(_translate("thaydoitthstrongnhom", "Mã học sinh"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(1)
        item.setText(_translate("thaydoitthstrongnhom", "Tên học sinh"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(2)
        item.setText(_translate("thaydoitthstrongnhom", "Mã nhóm"))
        item = self.dshocsinhtheonhom_view.horizontalHeaderItem(3)
        item.setText(_translate("thaydoitthstrongnhom", "GV phụ trách"))
        self.hoantat.setText(_translate("thaydoitthstrongnhom", "Hoàn tất"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thaydoitthstrongnhom = QtWidgets.QWidget()
    ui = Ui_thaydoitthstrongnhom()
    ui.setupUi(thaydoitthstrongnhom)
    thaydoitthstrongnhom.show()
    sys.exit(app.exec_())