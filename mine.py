import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Heroes Builds Cheatsheet'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def setHeroesMenu(self):
        # get heroes list
        # sort heroes list
        # show heroes list on combobox
        # (?) trigger event when clicked
        pass

    def setBuildsMenu(self, hero):
        # get builds list
        # (?) trigger event when clicked
        pass

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 #       self.setHeroesMenu()
 #       self.setBuildsMenu()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
