#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_kapldemo import Ui_KaplDemo


class KaplDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_KaplDemo()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        self.ui.bt_doit.clicked.connect(self._doit)

    def _doit(self):

        if self.ui.le_firstname.text() == '':
            return
        if self.ui.le_lastname.text() == '':
            return
        mb = QMessageBox()
        mb.setStandardButtons(QMessageBox.Ok)
        mb.setText("Successfully added {} {}".format(
            self.ui.le_firstname.text(),
            self.ui.le_lastname.text(),
        ))
        mb.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = KaplDemoMain()
    main.show()
    sys.exit(app.exec_())


