import bz2
import io


with bz2.BZ2File("example.bz2", "rb") as _input:
    with io.TextIOWrapper(_input, encoding="utf-8") as dec:
        print(dec.read())
