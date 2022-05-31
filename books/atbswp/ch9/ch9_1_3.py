import os

if __name__ == "__main__":
    for filename in os.listdir():
        if filename.endswith(".txt"):
            print("unlink", filename)
            os.unlink(filename)
