#!/usr/bin/python
#
# (c) 2015 John Strickler
#
# gpresinfo.py
# 
########################################
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_presinfo import Ui_PresInfo

from presidentsqlite import President

class PresInfoMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_PresInfo()
        self.ui.setupUi(self)

        # Connect up menu actions
        self.ui.actionQuit.triggered.connect(lambda:self.close())

        # Connect up the buttons.
        self.ui.btGetInfo.clicked.connect(self._get_info)

    def _get_info(self):
        term_num = int(self.ui.leTermNum.text())
        p = President(term_num)
        print(p)
        print(dir(p))
        name = '{0} {1}\n'.format(p.first_name, p.last_name)
        birth_location = '{0}, {1}\n'.format(p.birth_place, p.birth_state)
        birth = 'Born: {0}\n'.format(p.birth_date)
        death = 'Died: {0}\n'.format(p.death_date)
        served = 'Served: {0} to {1}\n'.format(p.term_start, p.term_end)
        party = '{0}\n'.format(p.party)
        self.ui.pteInfo.clear()
        for field in name, birth_location, birth, death, served, party:
            self.ui.pteInfo.insertPlainText(field)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PresInfoMain()
    main.show()
    sys.exit(app.exec_())
