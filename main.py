import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from log import Map


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Map')
        self.image.setFocus()
        self.delta = 0.005
        self.map = Map()
        self.btn_s.clicked.connect(self.search)
        self.mapRadio.setChecked(True)
        self.view = 'map'
        self.map.toponim('Москва')
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.mapRadio)
        self.button_group.addButton(self.satRadio)
        self.button_group.addButton(self.sklRadio)
        self.button_group.buttonClicked.connect(self.ViewChange)
        name = self.map.maping(self.delta, self.view)
        pixmap = QPixmap(name)
        self.image.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.delta > 0.005:
                self.delta -= 0.005
        if event.key() == Qt.Key_PageDown:
            if self.delta < 5:
                self.delta += 0.005
        if event.key() == Qt.Key_Up:
            self.map.cord(0, 0.001)
        if event.key() == Qt.Key_Left:
            self.map.cord(-0.001, 0)
        if event.key() == Qt.Key_Right:
            self.map.cord(0.001, 0)
        if event.key() == Qt.Key_Down:
            self.map.cord(0, -0.001)
        self.rendering()

    def rendering(self):
        name = self.map.maping(self.delta, self.view)
        pixmap = QPixmap(name)
        self.image.setPixmap(pixmap)

    def ViewChange(self, button):
        if button.text() == 'Схема':
            self.view = 'map'
        elif button.text() == 'Спутник':
            self.view = 'sat'
        elif button.text() == 'Гибрид':
            self.view = 'skl'
        self.rendering()

    def search(self):
        text = self.lineEdit.text()
        if text != "":
            self.map.toponim(text)
            self.rendering()
            self.image.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
