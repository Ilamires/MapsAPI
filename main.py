import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from log import Map
from PyQt5.QtCore import Qt


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Map')
        self.delta = 0.005
        self.map = Map()
        self.map.toponim("Москва")
        name = self.map.maping(self.delta)
        pixmap = QPixmap(name)
        self.image.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.delta > 0.005:
                self.delta -= 0.005
        if event.key() == Qt.Key_PageDown:
            if self.delta < 5:
                self.delta += 0.005
        self.rendering()

    def rendering(self):
        name = self.map.maping(self.delta)
        pixmap = QPixmap(name)
        self.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
