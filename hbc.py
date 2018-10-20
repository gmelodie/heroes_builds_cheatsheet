import sys
from PyQt5.QtWidgets import *
import mainWindow
from heroes_build_scrapper import get_heroes_list, load_builds


class Window(QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        heroes = get_heroes_list()
        self.heroComboBox.addItems(heroes)
        self.heroComboBox.currentIndexChanged.connect(self.selectionHero)

    def selectionHero(self):
        hero = self.heroComboBox.currentText()
        builds, titles = load_builds(hero)
        self.talentComboBox.addItems(titles)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
