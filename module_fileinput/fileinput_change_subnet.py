import fileinput
import sys

if __name__ == '__main__':
    from_base = sys.argv[1]
    to_base = sys.argv[2]
    files = sys.argv[3:]

    for line in fileinput.input(files, inplace=True):
        line = line.rstrip().replace(from_base, to_base)
        print(line)
