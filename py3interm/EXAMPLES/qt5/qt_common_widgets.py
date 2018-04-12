#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_commonwidgets import Ui_CommonWidgets

class CommonWidgetsMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_CommonWidgets()
        self.ui.setupUi(self)

        # populate the combo box
        for k,v in (('apple',1),('banana',2),('mango',3)):
            self.ui.cbFruits.insertItem(v,k,v)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CommonWidgetsMain()
    main.show()
    sys.exit(app.exec_())


