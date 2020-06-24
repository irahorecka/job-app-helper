import os
from docx import Document

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(CURRENT_PATH)


def write_docx(parent_dir_name, header_name):
    header = get_header_content(header_name)
    document = Document()
    document.add_heading(header)
    document.save(f{parent_dir_name}_{header_name}.docx)


def get_header_content(header_name):
    headers = {quote: Quote, origin: Quote Origin}

    return headers[header_name]


def main():
    os.chdir(BASE_PATH)
    
    headers = [quote, origin]
    dir_items = os.listdir()
    for item in dir_items:
        if os.path.isdir(item):
            os.chdir(os.path.abspath(item))

            for header in headers:
                write_docx(item, header)

            os.chdir(BASE_PATH)


if __name__ == __main__:
    main()

