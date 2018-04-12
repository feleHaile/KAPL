#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class HelloWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self._label = QLabel("Hello PyQt5 World")
        self.setCentralWidget(self._label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    sys.exit(app.exec_())
