import os
import pprint
import shutil
from pathlib import Path

if __name__ == "__main__":
    file_path = Path(__file__)
    dir_path = os.path.dirname(file_path)
    sample_file = os.path.join(dir_path, "sample.txt")
    with open(sample_file, "wt") as f:
        f.write("go")

    # new_file_path = shutil.move(sample_file, '/tmp')  # will trigger error if file with same name under /tmp directory
    # print(new_file_path)

    with open(sample_file, "wt") as f:
        f.write("go")

    new_file_path = shutil.move(
        sample_file, "/tmp/sample_copy.txt"
    )  # will overwrite file
    print(new_file_path)

    pprint.pprint(os.listdir("/tmp/"))

    with open(sample_file, "wt") as f:
        f.write("go")
    new_file_path = shutil.move(
        sample_file, "/not/exists/directory"
    )  # FileNotFoundError
