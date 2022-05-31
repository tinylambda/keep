import pathlib


p = pathlib.Path("..")
print(p.resolve())
for f in p.glob("*/*pathlib_*"):
    print(f)
