import pathlib

home = pathlib.Path.home()
print("home: ", home)

cwd = pathlib.Path.cwd()
print("cwd: ", cwd)

fp = pathlib.Path(__file__)
print("file full path", fp)
print("fp parent", fp.parent)
