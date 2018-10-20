import sys
from PyQt5.QtWidgets import *
import mainWindow


class Test(QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
