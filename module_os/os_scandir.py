import os
import sys


if __name__ == '__main__':
    for entry in os.scandir(sys.argv[1]):
        if entry.is_dir():
            typ = 'dir'
        elif entry.is_file():
            typ = 'file'
        elif entry.is_symlink():
            typ = 'link'
        else:
            typ = 'unknown'

        print(f'{entry.name} {typ}')
