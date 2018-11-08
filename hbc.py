import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import mainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint
from heroes_build_scrapper import get_heroes_list, load_builds, print_build


class Window(QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        heroes = get_heroes_list()
        self.heroComboBox.addItems(heroes)
        self.heroComboBox.currentIndexChanged.connect(self.selectionHero)


        # Custom editions on QMainWindow

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)



    def selectionHero(self):
        hero = self.heroComboBox.currentText()
        self.builds, self.titles = load_builds(hero)
        self.titles = [title.strip() for title in self.titles]
        self.talentComboBox.clear()
        self.talentComboBox.addItem('Choose build')
        self.talentComboBox.addItems(self.titles)
        self.talentComboBox.currentIndexChanged.connect(self.selectionTalent)

    def selectionTalent(self):
        if self.talentComboBox.currentIndex() > 0:
            build_title = self.talentComboBox.currentText()
            build = self.builds[self.titles.index(build_title)]
            self.label.setText(print_build(build, build_title))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
