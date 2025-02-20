import os

if not os.path.exists("archives"):
    os.mkdir("archives")

CURRENT_DIR = os.path.dirname(__file__)
ARCHIVE_DIR = os.path.join(CURRENT_DIR, "archives")
FILES_DIR = os.path.join(CURRENT_DIR, "files")
ZIP_PATH = os.path.join(ARCHIVE_DIR, "test_zip.zip")

