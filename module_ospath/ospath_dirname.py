import os.path

PATHS = ["/one/two/three", "/one/two/three/", "/", ""]

if __name__ == "__main__":
    for path in PATHS:
        print("{!r:>17}: {}".format(path, os.path.dirname(path)))
