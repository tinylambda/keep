import os.path

PATHS = [
    "filename.txt",
    "filename",
    "/path/to/filename.txt",
    "/",
    "",
    "my-archive.tar.gz",
    "no-extension.",
]

if __name__ == "__main__":
    for path in PATHS:
        print("{!r:>21}: {}".format(path, os.path.splitext(path)))
