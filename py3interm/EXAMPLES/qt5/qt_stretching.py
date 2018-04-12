#!/usr/bin/env python
import sys


from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_stretching import Ui_Stretching

class stretchingMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Stretching()
        self.ui.setupUi(self)

        # Connect up menu actions
        self.ui.actionQuit.triggered.connect(lambda:self.close())

        # Connect up the buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = stretchingMain()
    main.show()
    sys.exit(app.exec_())


