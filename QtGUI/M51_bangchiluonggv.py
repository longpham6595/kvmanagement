# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M51_bangchiluonggv.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bclgiaovien(object):
    def setupUi(self, bclgiaovien):
        bclgiaovien.setObjectName("bclgiaovien")
        bclgiaovien.resize(833, 347)
        self.gridLayout = QtWidgets.QGridLayout(bclgiaovien)
        self.gridLayout.setObjectName("gridLayout")
        self.payment_view = QtWidgets.QTableWidget(bclgiaovien)
        self.payment_view.setMinimumSize(QtCore.QSize(815, 200))
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
        self.gridLayout.addWidget(self.payment_view, 6, 0, 1, 6)
        self.label_3 = QtWidgets.QLabel(bclgiaovien)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 5)
        self.label = QtWidgets.QLabel(bclgiaovien)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.thang = QtWidgets.QSpinBox(bclgiaovien)
        self.thang.setMinimum(1)
        self.thang.setMaximum(12)
        self.thang.setObjectName("thang")
        self.gridLayout.addWidget(self.thang, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(bclgiaovien)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.nam = QtWidgets.QSpinBox(bclgiaovien)
        self.nam.setMinimum(2000)
        self.nam.setMaximum(3000)
        self.nam.setProperty("value", 2020)
        self.nam.setObjectName("nam")
        self.gridLayout.addWidget(self.nam, 1, 3, 1, 1)
        self.loc = QtWidgets.QPushButton(bclgiaovien)
        self.loc.setObjectName("loc")
        self.gridLayout.addWidget(self.loc, 5, 0, 1, 6)
        self.magv = QtWidgets.QComboBox(bclgiaovien)
        self.magv.setObjectName("magv")
        self.gridLayout.addWidget(self.magv, 1, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(bclgiaovien)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.locoption = QtWidgets.QRadioButton(bclgiaovien)
        self.locoption.setObjectName("locoption")
        self.gridLayout.addWidget(self.locoption, 3, 1, 1, 1)
        self.locall = QtWidgets.QRadioButton(bclgiaovien)
        self.locall.setObjectName("locall")
        self.gridLayout.addWidget(self.locall, 3, 3, 1, 1)
        self.hoantat = QtWidgets.QPushButton(bclgiaovien)
        self.hoantat.setObjectName("hoantat")
        self.gridLayout.addWidget(self.hoantat, 7, 0, 1, 6)

        self.retranslateUi(bclgiaovien)
        QtCore.QMetaObject.connectSlotsByName(bclgiaovien)

    def retranslateUi(self, bclgiaovien):
        _translate = QtCore.QCoreApplication.translate
        bclgiaovien.setWindowTitle(_translate("bclgiaovien", "B???ng chi l????ng gi??o vi??n"))
        item = self.payment_view.horizontalHeaderItem(0)
        item.setText(_translate("bclgiaovien", "M?? gi??o vi??n"))
        item = self.payment_view.horizontalHeaderItem(1)
        item.setText(_translate("bclgiaovien", "T??n gi??o vi??n"))
        item = self.payment_view.horizontalHeaderItem(2)
        item.setText(_translate("bclgiaovien", "H??? s??? l????ng"))
        item = self.payment_view.horizontalHeaderItem(3)
        item.setText(_translate("bclgiaovien", "L????ng theo h??? s???"))
        item = self.payment_view.horizontalHeaderItem(4)
        item.setText(_translate("bclgiaovien", "L????ng c???ng"))
        item = self.payment_view.horizontalHeaderItem(5)
        item.setText(_translate("bclgiaovien", "T???ng thu nh???p"))
        item = self.payment_view.horizontalHeaderItem(6)
        item.setText(_translate("bclgiaovien", "L????ng ???? ???ng"))
        item = self.payment_view.horizontalHeaderItem(7)
        item.setText(_translate("bclgiaovien", "L????ng t??ch l??y"))
        self.label_3.setText(_translate("bclgiaovien", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">B???NG CHI L????NG GI??O VI??N</span></p></body></html>"))
        self.label.setText(_translate("bclgiaovien", "Ch???n th??ng"))
        self.label_2.setText(_translate("bclgiaovien", "Ch???n n??m"))
        self.loc.setText(_translate("bclgiaovien", "L???c"))
        self.label_4.setText(_translate("bclgiaovien", "Ch???n m?? gi??o vi??n"))
        self.locoption.setText(_translate("bclgiaovien", "L???c theo m?? gi??o vi??n d?????i ????y"))
        self.locall.setText(_translate("bclgiaovien", "Hi???n th??? t???t c??? gi??o vi??n"))
        self.hoantat.setText(_translate("bclgiaovien", "Ho??n t???t"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bclgiaovien = QtWidgets.QWidget()
    ui = Ui_bclgiaovien()
    ui.setupUi(bclgiaovien)
    bclgiaovien.show()
    sys.exit(app.exec_())
