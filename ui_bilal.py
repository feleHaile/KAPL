# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bilal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bilal(object):
    def setupUi(self, bilal):
        bilal.setObjectName("bilal")
        bilal.resize(938, 587)
        self.centralwidget = QtWidgets.QWidget(bilal)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_save = QtWidgets.QPushButton(self.centralwidget)
        self.bt_save.setGeometry(QtCore.QRect(400, 520, 110, 32))
        self.bt_save.setObjectName("bt_save")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 10, 901, 491))
        self.tableView.setObjectName("tableView")
        bilal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(bilal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        bilal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(bilal)
        self.statusbar.setObjectName("statusbar")
        bilal.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(bilal)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(bilal)
        self.actionExit.triggered.connect(bilal.close)
        QtCore.QMetaObject.connectSlotsByName(bilal)

    def retranslateUi(self, bilal):
        _translate = QtCore.QCoreApplication.translate
        bilal.setWindowTitle(_translate("bilal", "Bilal Demo"))
        self.bt_save.setText(_translate("bilal", "Save Changes"))
        self.menuFile.setTitle(_translate("bilal", "File"))
        self.actionExit.setText(_translate("bilal", "Exit"))

