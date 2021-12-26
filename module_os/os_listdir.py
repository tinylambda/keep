import os
import sys


if __name__ == '__main__':
    print(sorted(os.listdir(sys.argv[1])))
