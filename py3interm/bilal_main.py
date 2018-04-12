#!/usr/bin/env python

import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_bilal import Ui_bilal


class bilalMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_bilal()
        self.ui.setupUi(self)

        self._setupDB()

        self.ui.bt_save.clicked.connect(self._save_changes)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def _setupDB(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('DATA/presidents.db')
        if not db.open():
            raise Exception("Could not open the database")

        self.ui.model = QSqlTableModel(self, db)
        self.ui.model.setTable("presidents")
        self.ui.model.EditStrategy(QSqlTableModel.OnManualSubmit)
        self.ui.tableView.setModel(self.ui.model)
        self.ui.tableView.setSortingEnabled(True)

    def _save_changes(self):
        self.ui.model.submitAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = bilalMain()
    main.show()
    sys.exit(app.exec_())


