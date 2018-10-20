import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
#import heroes_build_scrapper

app = QApplication(sys.argv)

window = QWidget()
window.resize(350, 300)
window.move(100, 100)
window.setWindowTitle('Heroes builds cheatsheet')

window.show()

sys.exit(app.exec_())
