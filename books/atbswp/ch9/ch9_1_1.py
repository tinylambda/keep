import os
import shutil
from pathlib import Path

if __name__ == "__main__":
    file_path = Path(__file__)
    print(file_path)
    os.chdir("/tmp/")
    shutil.copy(file_path, "/tmp/")

    print(os.listdir("/tmp"))

    dir_path = os.path.dirname(file_path)
    print(dir_path)
    shutil.copytree(dir_path, "/tmp/copied_dir")
    print(os.listdir("/tmp"))
