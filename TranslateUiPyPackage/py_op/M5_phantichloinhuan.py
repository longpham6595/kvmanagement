# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M5_phantichloinhuan.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_phantichloinhuan(object):
    def setupUi(self, phantichloinhuan):
        phantichloinhuan.setObjectName("phantichloinhuan")
        phantichloinhuan.resize(228, 257)
        self.layoutWidget = QtWidgets.QWidget(phantichloinhuan)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 207, 240))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bclgv = QtWidgets.QPushButton(self.layoutWidget)
        self.bclgv.setObjectName("bclgv")
        self.verticalLayout.addWidget(self.bclgv)
        self.capnhatthongtin = QtWidgets.QPushButton(self.layoutWidget)
        self.capnhatthongtin.setObjectName("capnhatthongtin")
        self.verticalLayout.addWidget(self.capnhatthongtin)
        self.chiluonggv = QtWidgets.QPushButton(self.layoutWidget)
        self.chiluonggv.setObjectName("chiluonggv")
        self.verticalLayout.addWidget(self.chiluonggv)
        self.lr = QtWidgets.QPushButton(self.layoutWidget)
        self.lr.setObjectName("lr")
        self.verticalLayout.addWidget(self.lr)
        self.bctq = QtWidgets.QPushButton(self.layoutWidget)
        self.bctq.setObjectName("bctq")
        self.verticalLayout.addWidget(self.bctq)
        self.bccptt = QtWidgets.QPushButton(self.layoutWidget)
        self.bccptt.setObjectName("bccptt")
        self.verticalLayout.addWidget(self.bccptt)
        self.quaylai = QtWidgets.QPushButton(self.layoutWidget)
        self.quaylai.setObjectName("quaylai")
        self.verticalLayout.addWidget(self.quaylai)

        self.retranslateUi(phantichloinhuan)
        QtCore.QMetaObject.connectSlotsByName(phantichloinhuan)

    def retranslateUi(self, phantichloinhuan):
        _translate = QtCore.QCoreApplication.translate
        phantichloinhuan.setWindowTitle(_translate("phantichloinhuan", "Form"))
        self.bclgv.setText(_translate("phantichloinhuan", "Bảng chi lương giáo viên"))
        self.capnhatthongtin.setText(_translate("phantichloinhuan", "Cập nhật thông tin lương giáo viên"))
        self.chiluonggv.setText(_translate("phantichloinhuan", "Chi lương giáo viên"))
        self.lr.setText(_translate("phantichloinhuan", "Lãi ròng"))
        self.bctq.setText(_translate("phantichloinhuan", "Báo cáo tổng quan"))
        self.bccptt.setText(_translate("phantichloinhuan", "Báo cáo chi phí tổng thể"))
        self.quaylai.setText(_translate("phantichloinhuan", "Quay lại"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    phantichloinhuan = QtWidgets.QWidget()
    ui = Ui_phantichloinhuan()
    ui.setupUi(phantichloinhuan)
    phantichloinhuan.show()
    sys.exit(app.exec_())
