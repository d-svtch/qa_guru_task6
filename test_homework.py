import os
from zipfile import ZipFile, ZIP_DEFLATED
from pypdf import PdfReader
from openpyxl import load_workbook
from conftest import ARCHIVE_DIR, FILES_DIR, ZIP_PATH
import shutil

def test_creating_archive():
    with ZipFile(os.path.join(ARCHIVE_DIR, "test_zip.zip"), mode='w', compression=ZIP_DEFLATED) as zip_file:
        for file in os.listdir(FILES_DIR):
            add_file = os.path.join("files", file)
            zip_file.write(add_file)

def test_pdf_reader():
    with ZipFile(ZIP_PATH, "r") as zip_file:
        with zip_file.open("files/test_pdf.pdf") as pdf_file:
            reader = PdfReader(pdf_file)
            assert "This is pdf file for tests" == reader.pages[0].extract_text()

def test_xlsx_reader():
    with ZipFile(ZIP_PATH, "r") as zip_file:
        with zip_file.open("files/test_xlsx.xlsx") as xlsx_file:
            reader = load_workbook(xlsx_file)
            assert "TEST" == reader.active.cell(row=3, column=2).value

def test_csv_reader():
    with ZipFile(ZIP_PATH, "r") as zip_file:
        with zip_file.open("files/test_csv.csv") as csv_file:
            reader = csv_file.read().decode("utf-8")
            assert "Jenkins" in reader

def test_deleting_archives_directory():
    shutil.rmtree(ARCHIVE_DIR)






