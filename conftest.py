import os
import shutil

import pytest
from zipfile import ZipFile, ZIP_DEFLATED

CURRENT_DIR = os.path.dirname(__file__)
ARCHIVE_DIR = os.path.join(CURRENT_DIR, "archives")
FILES_DIR = os.path.join(CURRENT_DIR, "files")
ZIP_PATH = os.path.join(ARCHIVE_DIR, "test_zip.zip")


@pytest.fixture(scope="session", autouse=True)
def operations_with_archive():
    if not os.path.exists("archives"):
        os.mkdir("archives")
    with ZipFile(os.path.join(ARCHIVE_DIR, "test_zip.zip"), mode='w', compression=ZIP_DEFLATED) as zip_file:
        for file in os.listdir(FILES_DIR):
            add_file = os.path.join("files", file)
            zip_file.write(add_file)
    yield
    shutil.rmtree(ARCHIVE_DIR)
