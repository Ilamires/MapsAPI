import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from log import maping


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Map')
        name = maping()
        pixmap = QPixmap(name)
        self.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
