# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogWindow(object):
    def setupUi(self, dialogWindow):
        dialogWindow.setObjectName("dialogWindow")
        dialogWindow.resize(400, 177)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 131, 341, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(dialogWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(dialogWindow)
        self.buttonBox.accepted.connect(dialogWindow.accept)
        self.buttonBox.rejected.connect(dialogWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogWindow)

    def retranslateUi(self, dialogWindow):
        _translate = QtCore.QCoreApplication.translate
        dialogWindow.setWindowTitle(_translate("dialogWindow", "Dialog"))
        self.label.setText(_translate("dialogWindow", "TextLabel"))

