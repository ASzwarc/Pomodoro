# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StepFinishedDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StepFinishedDialog(object):
    def setupUi(self, StepFinishedDialog):
        StepFinishedDialog.setObjectName("StepFinishedDialog")
        StepFinishedDialog.resize(473, 117)
        self.buttonBox = QtWidgets.QDialogButtonBox(StepFinishedDialog)
        self.buttonBox.setGeometry(QtCore.QRect(280, 70, 181, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.notificationLabel = QtWidgets.QLabel(StepFinishedDialog)
        self.notificationLabel.setGeometry(QtCore.QRect(20, 20, 431, 41))
        self.notificationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notificationLabel.setObjectName("notificationLabel")

        self.retranslateUi(StepFinishedDialog)
        self.buttonBox.accepted.connect(StepFinishedDialog.accept)
        self.buttonBox.rejected.connect(StepFinishedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StepFinishedDialog)

    def retranslateUi(self, StepFinishedDialog):
        _translate = QtCore.QCoreApplication.translate
        StepFinishedDialog.setWindowTitle(_translate("StepFinishedDialog", "What to do next"))
        self.notificationLabel.setText(_translate("StepFinishedDialog", "TextLabel"))

