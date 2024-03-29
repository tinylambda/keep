import gzip
import io
import itertools
import os


with gzip.open("/tmp/example_lines.txt.gz", "wb") as output:
    with io.TextIOWrapper(output, encoding="utf-8") as enc:
        enc.writelines(itertools.repeat("The same line, over and over.\n", 10))

os.system("gzcat /tmp/example_lines.txt.gz")
