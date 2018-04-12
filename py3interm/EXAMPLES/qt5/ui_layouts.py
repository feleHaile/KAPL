# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Layouts(object):
    def setupUi(self, Layouts):
        Layouts.setObjectName("Layouts")
        Layouts.resize(411, 268)
        self.centralwidget = QtWidgets.QWidget(Layouts)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        Layouts.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Layouts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 25))
        self.menubar.setObjectName("menubar")
        Layouts.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Layouts)
        self.statusbar.setObjectName("statusbar")
        Layouts.setStatusBar(self.statusbar)

        self.retranslateUi(Layouts)
        QtCore.QMetaObject.connectSlotsByName(Layouts)

    def retranslateUi(self, Layouts):
        _translate = QtCore.QCoreApplication.translate
        Layouts.setWindowTitle(_translate("Layouts", "Layouts"))
        self.label.setText(_translate("Layouts", "VBox Row 1"))
        self.label_2.setText(_translate("Layouts", "VBox Row 2"))
        self.label_6.setText(_translate("Layouts", "<html><head/><body><p>VBox Row 3<br/>HBox Col 1</p></body></html>"))
        self.label_7.setText(_translate("Layouts", "VBox Row 3\n"
"HBox Col 2"))
        self.label_4.setText(_translate("Layouts", "VBox Row 3\n"
"HBox Col 3"))
        self.label_3.setText(_translate("Layouts", "VBox Row 4"))

