import os
import shutil
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
from utils import write_to_textfile

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_CV = "ira_horecka_cv_20200616.docx"
JOB_PATH = os.path.join(BASE_PATH, "job_applications")


class MainPage(QMainWindow, UiMainWindow):
    """Main page of the application."""

    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)
        self.generate_button.clicked.connect(self.make_job_app_dir)
        self.generate_button.clicked.connect(self.make_textfile)
        self.generate_button.clicked.connect(self.generate_docx)
        self.cancel_button.clicked.connect(self.close)
        self.full_source_cv_path = os.path.join(BASE_PATH, "resources", BASE_CV)

    def make_job_app_dir(self):
        """Make directory for new job application."""
        self.full_dest_cv_path = os.path.join(
            JOB_PATH,
            f"{self.get_text(self.company_box)} - {self.get_text(self.job_title_box)}",
        )
        try:
            os.makedirs(self.full_dest_cv_path)
        except FileExistsError as error:
            print(f"WHOA something exists!\n{error}")
            raise RuntimeError

    def make_textfile(self):
        """Make supplementary information text file in directory
        of new job application."""
        rows = self.skills_table.rowCount()
        skills_iter = [
            self.get_text(self.skills_table.item(row, 0))
            for row in range(rows)
            if self.skills_table.item(row, 0)
            and self.get_text(self.skills_table.item(row, 0))
        ]
        write_to_textfile(self.full_dest_cv_path, skills_iter)

    def generate_docx(self):
        """Generate a copy of the template CV with modified file name
        and in new job application directory."""
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
    """Copy template CV docx file to new job application
    directory."""
    shutil.copyfile(source_docx_path, dest_docx_path)


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WIDGET = MainPage()
    APP.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    WIDGET.show()
    sys.exit(APP.exec_())
