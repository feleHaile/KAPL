import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_boeingdemo import Ui_BoeingDemo


class BoeingDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_BoeingDemo()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BoeingDemoMain()
    main.show()
    sys.exit(app.exec_())
