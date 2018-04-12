# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kapldemo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KaplDemo(object):
    def setupUi(self, KaplDemo):
        KaplDemo.setObjectName("KaplDemo")
        KaplDemo.resize(489, 190)
        self.centralwidget = QtWidgets.QWidget(KaplDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.le_firstname.setText("")
        self.le_firstname.setObjectName("le_firstname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_firstname)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lastname.setObjectName("le_lastname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_lastname)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.bt_doit = QtWidgets.QPushButton(self.centralwidget)
        self.bt_doit.setObjectName("bt_doit")
        self.gridLayout.addWidget(self.bt_doit, 1, 0, 1, 1)
        KaplDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KaplDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        KaplDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KaplDemo)
        self.statusbar.setObjectName("statusbar")
        KaplDemo.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(KaplDemo)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(KaplDemo)
        self.actionPaste.setObjectName("actionPaste")
        self.actionQuit = QtWidgets.QAction(KaplDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(KaplDemo)
        self.actionQuit.triggered.connect(KaplDemo.close)
        QtCore.QMetaObject.connectSlotsByName(KaplDemo)

    def retranslateUi(self, KaplDemo):
        _translate = QtCore.QCoreApplication.translate
        KaplDemo.setWindowTitle(_translate("KaplDemo", "KAPL Demo"))
        self.label.setText(_translate("KaplDemo", "First Name"))
        self.label_2.setText(_translate("KaplDemo", "Last Name"))
        self.bt_doit.setText(_translate("KaplDemo", "Doit"))
        self.menuFile.setTitle(_translate("KaplDemo", "File"))
        self.menuEdit.setTitle(_translate("KaplDemo", "Edit"))
        self.actionCopy.setText(_translate("KaplDemo", "Copy"))
        self.actionPaste.setText(_translate("KaplDemo", "Paste"))
        self.actionQuit.setText(_translate("KaplDemo", "Quit"))

