# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M61_quanlybaihocgiohoc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_quanlybaihocgiohoc(object):
    def setupUi(self, quanlybaihocgiohoc):
        quanlybaihocgiohoc.setObjectName("quanlybaihocgiohoc")
        quanlybaihocgiohoc.resize(274, 158)
        self.widget = QtWidgets.QWidget(quanlybaihocgiohoc)
        self.widget.setGeometry(QtCore.QRect(10, 10, 254, 135))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cnttcn = QtWidgets.QPushButton(self.widget)
        self.cnttcn.setObjectName("cnttcn")
        self.verticalLayout.addWidget(self.cnttcn)
        self.cnttn = QtWidgets.QPushButton(self.widget)
        self.cnttn.setObjectName("cnttn")
        self.verticalLayout.addWidget(self.cnttn)
        self.utthvnchs = QtWidgets.QPushButton(self.widget)
        self.utthvnchs.setObjectName("utthvnchs")
        self.verticalLayout.addWidget(self.utthvnchs)
        self.quaylai = QtWidgets.QPushButton(self.widget)
        self.quaylai.setObjectName("quaylai")
        self.verticalLayout.addWidget(self.quaylai)

        self.retranslateUi(quanlybaihocgiohoc)
        QtCore.QMetaObject.connectSlotsByName(quanlybaihocgiohoc)

    def retranslateUi(self, quanlybaihocgiohoc):
        _translate = QtCore.QCoreApplication.translate
        quanlybaihocgiohoc.setWindowTitle(_translate("quanlybaihocgiohoc", "Form"))
        self.cnttcn.setText(_translate("quanlybaihocgiohoc", "Cập nhật tiến trình cá nhân"))
        self.cnttn.setText(_translate("quanlybaihocgiohoc", "Cập nhật tiến trình nhóm"))
        self.utthvnchs.setText(_translate("quanlybaihocgiohoc", "Update tình trạng học và nghỉ của học sinh"))
        self.quaylai.setText(_translate("quanlybaihocgiohoc", "Quay lại"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quanlybaihocgiohoc = QtWidgets.QWidget()
    ui = Ui_quanlybaihocgiohoc()
    ui.setupUi(quanlybaihocgiohoc)
    quanlybaihocgiohoc.show()
    sys.exit(app.exec_())
