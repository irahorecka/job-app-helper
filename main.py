import os
import sys
import qdarkstyle
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QFileDialog,
    QMainWindow,
    QSlider,
    QMessageBox,
    QPushButton,
)
from ui import UiMainWindow


class MainPage(QMainWindow, UiMainWindow):
    """Main page of the application."""

    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WIDGET = MainPage()
    APP.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    WIDGET.show()
    sys.exit(APP.exec_())