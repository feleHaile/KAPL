#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_hello2 import Ui_Hello2  # import generated interface

class Hello2Main(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface generated from Designer.
        self.ui = Ui_Hello2()  # attribute name does not have to be "ui"
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Hello2Main()
    main.show()
    sys.exit(app.exec_())


