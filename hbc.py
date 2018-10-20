import sys
from PyQt5.QtWidgets import *
import mainWindow
from heroes_build_scrapper import get_heroes_list, get_build_titles


class Window(QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        heroes = get_heroes_list()
        self.heroComboBox.addItems(heroes)
        self.heroComboBox.currentIndexChanged.connect(self.selectionHero)

    def selectionHero(self):
        hero = self.heroComboBox.currentText()
        titles = get_build_titles(hero)
        self.talentComboBox.addItem(titles)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
