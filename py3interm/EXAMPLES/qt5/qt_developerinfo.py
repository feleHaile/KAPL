#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import *

from ui_developerinfo import Ui_DeveloperInfo
from ui_developerinfodialog import Ui_DeveloperInfoDialog

class DeveloperInfoMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_DeveloperInfo()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda:self.close())

        self.ui.btGetInfo.clicked.connect(self._get_info)

    def _get_info(self):
        dlg = QDialog()
        ui = Ui_DeveloperInfoDialog()
        ui.setupUi(dlg)
        if dlg.exec_():
            name = ui.leName.text()
            email = ui.leEmail.text()
            if ui.rbPython.isChecked():
                lang = 'Python'
            elif ui.rbPerl.isChecked():
                lang = 'Perl'
            elif ui.rbRuby.isChecked():
                lang = 'Ruby'
            self.ui.labInfo.setText("{0}\n{1}\n{2}".format(name, email, lang))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DeveloperInfoMain()
    main.show()
    sys.exit(app.exec_())


