import glob
import os


if __name__ == "__main__":
    with open("rename_start.txt", "w") as f:
        f.write("starting as rename_start.txt")

    print(f'Starting: {glob.glob("rename*.txt")}')
    os.rename("rename_start.txt", "rename_finish.txt")
    print(f'After rename: {glob.glob("rename*.txt")}')

    with open("rename_finish.txt", "r") as f:
        print(f"Contents: {repr(f.read())}")

    with open("rename_new_contents.txt", "w") as f:
        f.write("ending with contents of rename_new_contents.txt")

    os.replace("rename_new_contents.txt", "rename_finish.txt")
    with open("rename_finish.txt", "r") as f:
        print(f"After replace: {repr(f.read())}")

    for name in glob.glob("rename*.txt"):
        os.unlink(name)
