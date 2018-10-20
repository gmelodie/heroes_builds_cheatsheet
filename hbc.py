import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def _heroes_menu(self, grid):
        select_hero = QComboBox()
        grid.addWidget(select_hero, 0, 0)
        heroes = ['diablo', 'valla', 'sonya'] # get heroes list, ORDERED!
        select_hero.addItems(heroes)
        return grid


    def _builds_menu(self, grid):
        select_hero = QComboBox()
        grid.addWidget(select_hero, 0, 10)
        heroes = ['diablo', 'valla', 'sonya'] # get heroes list, ORDERED!
        select_hero.addItems(heroes)
        return grid

    def initUI(self):
        grid = QGridLayout()
        grid = self._heroes_menu(grid)
        grid = self._builds_menu(grid)

        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())







class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('index.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(QApplication.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

