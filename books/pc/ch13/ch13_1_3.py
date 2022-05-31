import fileinput

with fileinput.input() as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end="")
