import sys
from PyQt5.QtWidgets import *
import mainWindow
from heroes_build_scrapper import get_heroes_list, load_builds, print_build


class Window(QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        heroes = get_heroes_list()
        self.heroComboBox.addItems(heroes)
        self.heroComboBox.currentIndexChanged.connect(self.selectionHero)

    def selectionHero(self):
        hero = self.heroComboBox.currentText()
        self.builds, self.titles = load_builds(hero)
        self.titles = [title.strip() for title in self.titles]
        self.talentComboBox.addItems(self.titles)
        self.talentComboBox.currentIndexChanged.connect(self.selectionTalent)

    def selectionTalent(self):
        build_index = self.talentComboBox.currentIndex() - 1
        self.label.setText(print_build(self.builds[build_index], self.titles[build_index]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
