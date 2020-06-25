"""Module to write supplementary text information pertaining to your job."""
import os
from pathlib import Path


def write_to_textfile(job_dir_path, skill_iter_items):
    """Acquire job application directory path and skills to
    include in the supplementary text file. Write information to
    new text file."""
    text_header = "Desired skills and qualifications"
    skill_iter_items.insert(0, text_header)
    text_file_path = touch_textfile(job_dir_path)

    with open(text_file_path, "w") as file:
        file.write("\n".join(skill_iter_items))


def touch_textfile(file_path):
    """Create supplementary text file (empty) in the job
    application directory."""
    suppl_info_path = os.path.join(file_path, "supplementary_information.txt")
    Path(suppl_info_path).touch()
    return suppl_info_path
