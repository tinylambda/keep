import pathlib


p = pathlib.Path('/home/felix/PycharmProjects/keep/')

# iterdir() is a generator, yielding a new Path instance for each item in the containing directory.
# not recursive !
for f in p.iterdir():
    print(f)
