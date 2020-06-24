import os
import shutil
import sys
from pathlib import Path
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

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_CV = "ira_horecka_cv_20200616.docx"
JOB_PATH = os.path.join(BASE_PATH, "job_applications")


class MainPage(QMainWindow, UiMainWindow):
    """Main page of the application."""

    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)
        self.generate_button.clicked.connect(self.make_job_dir)
        self.generate_button.clicked.connect(self.generate_docx)
        self.cancel_button.clicked.connect(self.close)
        self.full_source_dir_path = os.path.join(BASE_PATH, "resources", BASE_CV)

    def make_job_dir(self):
        local_dest_dir_path = (
            f"{self.get_text(self.company_box)} - {self.get_text(self.job_title_box)}"
        )
        self.full_dest_dir_path = os.path.join(JOB_PATH, local_dest_dir_path)
        try:
            os.makedirs(self.full_dest_dir_path)
        except FileExistsError:
            print("WHOA something exists!")

    def generate_docx(self):
        cv_title = f"Ira Horecka CV - {self.get_text(self.company_box)}, {self.get_text(self.job_title_box)}.docx"
        print(cv_title)
        copy_template_docx(
            self.full_source_dir_path, os.path.join(self.full_dest_dir_path, cv_title)
        )
        # Path(f'{BASE_PATH}/file.txt').touch()

    @staticmethod
    def get_text(item):
        """Get text of cell value, if empty return empty str."""
        try:
            item = item.text()
            return item
        except AttributeError:
            item = ""
            return item


def copy_template_docx(source_docx_path, dest_docx_path):
    shutil.copyfile(source_docx_path, dest_docx_path)


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WIDGET = MainPage()
    APP.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    WIDGET.show()
    sys.exit(APP.exec_())
