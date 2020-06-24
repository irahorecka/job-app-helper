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
        self.generate_button.clicked.connect(self.make_job_app_dir)
        self.generate_button.clicked.connect(self.touch_text_file)
        self.generate_button.clicked.connect(self.generate_docx)
        self.cancel_button.clicked.connect(self.close)
        self.full_source_cv_path = os.path.join(BASE_PATH, "resources", BASE_CV)

    def make_job_app_dir(self):
        self.full_dest_cv_path = os.path.join(
            JOB_PATH,
            f"{self.get_text(self.company_box)} - {self.get_text(self.job_title_box)}",
        )
        try:
            print(self.full_dest_cv_path)
            os.makedirs(self.full_dest_cv_path)
        except FileExistsError:
            print("WHOA something exists!")

    def touch_text_file(self):
        Path(
            os.path.join(self.full_dest_cv_path, "supplementary_information.txt")
        ).touch()

    def generate_docx(self):
        cv_title = f"Ira Horecka CV - {self.get_text(self.company_box)}, {self.get_text(self.job_title_box)}.docx"
        print(cv_title)
        copy_template_docx(
            self.full_source_cv_path, os.path.join(self.full_dest_cv_path, cv_title)
        )

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
