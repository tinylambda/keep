import pathlib

p = pathlib.Path("/tmp")

# iterdir() is a generator, yielding a new Path instance for each item in the containing directory.
# not recursive !
for f in p.iterdir():
    print(f, type(f), f.is_file(), f.absolute())
