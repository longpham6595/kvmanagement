# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ip\M4_phanmonnhomtkb.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_phanmonnhomtkb(object):
    def setupUi(self, phanmonnhomtkb):
        phanmonnhomtkb.setObjectName("phanmonnhomtkb")
        phanmonnhomtkb.resize(300, 200)
        phanmonnhomtkb.setMaximumSize(QtCore.QSize(500, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(phanmonnhomtkb)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lkthemxoanhom = QtWidgets.QPushButton(phanmonnhomtkb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lkthemxoanhom.sizePolicy().hasHeightForWidth())
        self.lkthemxoanhom.setSizePolicy(sizePolicy)
        self.lkthemxoanhom.setObjectName("lkthemxoanhom")
        self.verticalLayout.addWidget(self.lkthemxoanhom)
        self.cnhstn = QtWidgets.QPushButton(phanmonnhomtkb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cnhstn.sizePolicy().hasHeightForWidth())
        self.cnhstn.setSizePolicy(sizePolicy)
        self.cnhstn.setObjectName("cnhstn")
        self.verticalLayout.addWidget(self.cnhstn)
        self.dtkbn = QtWidgets.QPushButton(phanmonnhomtkb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtkbn.sizePolicy().hasHeightForWidth())
        self.dtkbn.setSizePolicy(sizePolicy)
        self.dtkbn.setObjectName("dtkbn")
        self.verticalLayout.addWidget(self.dtkbn)
        self.quaylai = QtWidgets.QPushButton(phanmonnhomtkb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quaylai.sizePolicy().hasHeightForWidth())
        self.quaylai.setSizePolicy(sizePolicy)
        self.quaylai.setObjectName("quaylai")
        self.verticalLayout.addWidget(self.quaylai)

        self.retranslateUi(phanmonnhomtkb)
        QtCore.QMetaObject.connectSlotsByName(phanmonnhomtkb)

    def retranslateUi(self, phanmonnhomtkb):
        _translate = QtCore.QCoreApplication.translate
        phanmonnhomtkb.setWindowTitle(_translate("phanmonnhomtkb", "Form"))
        self.lkthemxoanhom.setText(_translate("phanmonnhomtkb", "Li???t k??/Th??m/X??a nh??m"))
        self.cnhstn.setText(_translate("phanmonnhomtkb", "C???p nh???t h???c sinh trong nh??m"))
        self.dtkbn.setText(_translate("phanmonnhomtkb", "Th??m/?????i th???i kh??a bi???u nh??m"))
        self.quaylai.setText(_translate("phanmonnhomtkb", "Quay l???i"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    phanmonnhomtkb = QtWidgets.QWidget()
    ui = Ui_phanmonnhomtkb()
    ui.setupUi(phanmonnhomtkb)
    phanmonnhomtkb.show()
    sys.exit(app.exec_())
