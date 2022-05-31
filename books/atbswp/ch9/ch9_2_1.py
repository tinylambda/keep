import os
from pathlib import Path

if __name__ == "__main__":
    file_path = Path(__file__)
    dir_path = os.path.dirname(file_path)
    parent_path = os.path.join(dir_path, os.path.pardir)

    for root, dirs, files in os.walk(parent_path):
        print("root is now", os.path.abspath(root))
        print("dirs: ")
        for dir_name in dirs:
            print("\t", os.path.abspath(os.path.join(root, dir_name)))
        print("files: ")
        for filename in files:
            print("\t", os.path.abspath(os.path.join(root, filename)))
        print("\n\n")
