# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boeingdemo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BoeingDemo(object):
    def setupUi(self, BoeingDemo):
        BoeingDemo.setObjectName("BoeingDemo")
        BoeingDemo.resize(269, 195)
        self.centralwidget = QtWidgets.QWidget(BoeingDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_pushme = QtWidgets.QPushButton(self.centralwidget)
        self.bt_pushme.setGeometry(QtCore.QRect(70, 90, 110, 32))
        self.bt_pushme.setObjectName("bt_pushme")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 50, 71, 20))
        self.label.setObjectName("label")
        self.le_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_name.setGeometry(QtCore.QRect(110, 50, 113, 21))
        self.le_name.setObjectName("le_name")
        BoeingDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BoeingDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 269, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        BoeingDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BoeingDemo)
        self.statusbar.setObjectName("statusbar")
        BoeingDemo.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(BoeingDemo)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(BoeingDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFIle.addAction(self.actionOpen)
        self.menuFIle.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(BoeingDemo)
        self.actionQuit.triggered.connect(BoeingDemo.close)
        QtCore.QMetaObject.connectSlotsByName(BoeingDemo)

    def retranslateUi(self, BoeingDemo):
        _translate = QtCore.QCoreApplication.translate
        BoeingDemo.setWindowTitle(_translate("BoeingDemo", "MainWindow"))
        self.bt_pushme.setText(_translate("BoeingDemo", "Push Me"))
        self.label.setText(_translate("BoeingDemo", "Your Name"))
        self.menuFIle.setTitle(_translate("BoeingDemo", "File"))
        self.menuEdit.setTitle(_translate("BoeingDemo", "Edit"))
        self.actionOpen.setText(_translate("BoeingDemo", "Open..."))
        self.actionQuit.setText(_translate("BoeingDemo", "Quit"))

