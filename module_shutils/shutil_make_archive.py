import logging
import shutil
import sys
import tarfile


logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger("pymotw")

print("Creating archive: ")
shutil.make_archive(
    "example", "gztar", root_dir="..", base_dir="module_shutils", logger=logger
)

print("\nArchive contents: ")
with tarfile.open("example.tar.gz", "r") as t:
    for n in t.getnames():
        print(n)
