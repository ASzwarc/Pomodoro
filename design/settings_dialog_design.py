# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(396, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(SettingsWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 20, 151, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(SettingsWindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 20, 101, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.workTimeEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.workTimeEdit.setObjectName("workTimeEdit")
        self.verticalLayout_2.addWidget(self.workTimeEdit)
        self.shortBreakTimeEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.shortBreakTimeEdit.setObjectName("shortBreakTimeEdit")
        self.verticalLayout_2.addWidget(self.shortBreakTimeEdit)
        self.longBreakTimeEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.longBreakTimeEdit.setObjectName("longBreakTimeEdit")
        self.verticalLayout_2.addWidget(self.longBreakTimeEdit)
        self.noOfUnitsEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.noOfUnitsEdit.setObjectName("noOfUnitsEdit")
        self.verticalLayout_2.addWidget(self.noOfUnitsEdit)

        self.retranslateUi(SettingsWindow)
        self.buttonBox.accepted.connect(SettingsWindow.accept)
        self.buttonBox.rejected.connect(SettingsWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.label_2.setText(_translate("SettingsWindow", "Work time"))
        self.label_3.setText(_translate("SettingsWindow", "Short break time"))
        self.label.setText(_translate("SettingsWindow", "Long break time"))
        self.label_4.setText(_translate("SettingsWindow", "No of units"))

