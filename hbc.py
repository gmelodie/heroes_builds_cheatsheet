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
        self.talentComboBox.clear()
        self.talentComboBox.addItem('Choose build')
        self.talentComboBox.addItems(self.titles)
        self.talentComboBox.currentIndexChanged.connect(self.selectionTalent)

    def selectionTalent(self):
        if self.talentComboBox.currentIndex() > 0:
            build_title = self.talentComboBox.currentText()
            build = self.builds[self.titles.index(build_title)]
            self.label.setText(print_build(build, build_title))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
