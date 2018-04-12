# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'developerinfodialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeveloperInfoDialog(object):
    def setupUi(self, DeveloperInfoDialog):
        DeveloperInfoDialog.setObjectName("DeveloperInfoDialog")
        DeveloperInfoDialog.resize(477, 174)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeveloperInfoDialog)
        self.buttonBox.setGeometry(QtCore.QRect(87, 127, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(DeveloperInfoDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 15, 455, 96))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labName.setObjectName("labName")
        self.horizontalLayout_3.addWidget(self.labName)
        self.leName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leName.setObjectName("leName")
        self.horizontalLayout_3.addWidget(self.leName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labEmail = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labEmail.setObjectName("labEmail")
        self.horizontalLayout_4.addWidget(self.labEmail)
        self.leEmail = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leEmail.setObjectName("leEmail")
        self.horizontalLayout_4.addWidget(self.leEmail)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rbPython = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbPython.setChecked(True)
        self.rbPython.setObjectName("rbPython")
        self.horizontalLayout_5.addWidget(self.rbPython)
        self.rbPerl = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbPerl.setObjectName("rbPerl")
        self.horizontalLayout_5.addWidget(self.rbPerl)
        self.rbRuby = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbRuby.setObjectName("rbRuby")
        self.horizontalLayout_5.addWidget(self.rbRuby)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(DeveloperInfoDialog)
        self.buttonBox.accepted.connect(DeveloperInfoDialog.accept)
        self.buttonBox.rejected.connect(DeveloperInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeveloperInfoDialog)

    def retranslateUi(self, DeveloperInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        DeveloperInfoDialog.setWindowTitle(_translate("DeveloperInfoDialog", "DeveloperInfoDialog"))
        self.labName.setText(_translate("DeveloperInfoDialog", "Name"))
        self.labEmail.setText(_translate("DeveloperInfoDialog", "Email Address: "))
        self.rbPython.setText(_translate("DeveloperInfoDialog", "Python"))
        self.rbPerl.setText(_translate("DeveloperInfoDialog", "Perl"))
        self.rbRuby.setText(_translate("DeveloperInfoDialog", "Ruby"))

