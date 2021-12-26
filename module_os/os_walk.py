import os
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        root = '/tmp'
    else:
        root = sys.argv[1]

    for dir_name, sub_dirs, files in os.walk(root):
        print(dir_name)
        sub_dirs = [n + '/' for n in sub_dirs]
        contents = sub_dirs + files
        contents.sort()
        for c in contents:
            print('\t{}'.format(c))
        print()
    