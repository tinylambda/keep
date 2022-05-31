import bz2
import os


data = "hello 中国"

with bz2.open("example1.bz2", "wt", encoding="utf-8") as _output:
    _output.write(data)

with bz2.open("example1.bz2", "rt", encoding="utf-8") as _input:
    print("full file: {}".format(_input.read()))

with bz2.open("example1.bz2", "rt", encoding="utf-8") as _input:
    _input.seek(6)
    print("one character: {}".format(_input.read(1)))

with bz2.open("example1.bz2", "rt", encoding="utf-8") as _input:
    _input.seek(7)
    try:
        print(_input.read(1))
    except UnicodeError:
        print("ERROR: failed to decode")
