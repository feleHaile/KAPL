# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'developerinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeveloperInfo(object):
    def setupUi(self, DeveloperInfo):
        DeveloperInfo.setObjectName("DeveloperInfo")
        DeveloperInfo.resize(231, 190)
        self.centralwidget = QtWidgets.QWidget(DeveloperInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.btGetInfo = QtWidgets.QPushButton(self.centralwidget)
        self.btGetInfo.setGeometry(QtCore.QRect(10, 16, 169, 46))
        self.btGetInfo.setObjectName("btGetInfo")
        self.labInfo = QtWidgets.QLabel(self.centralwidget)
        self.labInfo.setGeometry(QtCore.QRect(18, 75, 182, 57))
        self.labInfo.setText("")
        self.labInfo.setObjectName("labInfo")
        DeveloperInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeveloperInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 231, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        DeveloperInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DeveloperInfo)
        self.statusbar.setObjectName("statusbar")
        DeveloperInfo.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(DeveloperInfo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(DeveloperInfo)
        QtCore.QMetaObject.connectSlotsByName(DeveloperInfo)

    def retranslateUi(self, DeveloperInfo):
        _translate = QtCore.QCoreApplication.translate
        DeveloperInfo.setWindowTitle(_translate("DeveloperInfo", "DeveloperInfo"))
        self.btGetInfo.setText(_translate("DeveloperInfo", "Get Developer Info"))
        self.menuFile.setTitle(_translate("DeveloperInfo", "Application"))
        self.actionQuit.setText(_translate("DeveloperInfo", "Quit"))

