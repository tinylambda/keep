import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith(".gz"):
            f = gzip.open(filename, "rt")
        elif filename.endswith(".bz2"):
            f = bz2.open(filename, "rt")
        else:
            f = open(filename, "rt")
        yield f
        f.close()


def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


if __name__ == "__main__":
    pyfiles = gen_find("*.py", "../")
    opened_pyfiles = gen_opener(pyfiles)
    lines = gen_concatenate(opened_pyfiles)
    os_import_lines = gen_grep("import os", lines)
    for line in os_import_lines:
        print(line)
