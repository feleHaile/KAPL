# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stretching.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Stretching(object):
    def setupUi(self, Stretching):
        Stretching.setObjectName("Stretching")
        Stretching.resize(294, 201)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Stretching.sizePolicy().hasHeightForWidth())
        Stretching.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Stretching)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_A = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_A.sizePolicy().hasHeightForWidth())
        self.button_A.setSizePolicy(sizePolicy)
        self.button_A.setObjectName("button_A")
        self.verticalLayout.addWidget(self.button_A)
        self.button_B = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_B.sizePolicy().hasHeightForWidth())
        self.button_B.setSizePolicy(sizePolicy)
        self.button_B.setObjectName("button_B")
        self.verticalLayout.addWidget(self.button_B)
        self.button_C = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_C.sizePolicy().hasHeightForWidth())
        self.button_C.setSizePolicy(sizePolicy)
        self.button_C.setObjectName("button_C")
        self.verticalLayout.addWidget(self.button_C)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Stretching.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stretching)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 25))
        self.menubar.setObjectName("menubar")
        self.menuTesting = QtWidgets.QMenu(self.menubar)
        self.menuTesting.setObjectName("menuTesting")
        Stretching.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stretching)
        self.statusbar.setObjectName("statusbar")
        Stretching.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(Stretching)
        self.actionQuit.setObjectName("actionQuit")
        self.menuTesting.addAction(self.actionQuit)
        self.menubar.addAction(self.menuTesting.menuAction())

        self.retranslateUi(Stretching)
        QtCore.QMetaObject.connectSlotsByName(Stretching)

    def retranslateUi(self, Stretching):
        _translate = QtCore.QCoreApplication.translate
        Stretching.setWindowTitle(_translate("Stretching", "Stretching"))
        self.button_A.setText(_translate("Stretching", "A"))
        self.button_B.setText(_translate("Stretching", "B"))
        self.button_C.setText(_translate("Stretching", "C"))
        self.menuTesting.setTitle(_translate("Stretching", "Testing"))
        self.actionQuit.setText(_translate("Stretching", "Quit"))

