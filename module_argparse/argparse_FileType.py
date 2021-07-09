import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', metavar='in-file', type=argparse.FileType('rt'))
parser.add_argument('-o', metavar='out-file', type=argparse.FileType('wt'))

try:
    results = parser.parse_args()
    print('input file: ', results.i)
    print('output file: ', results.o)
except IOError as msg:
    parser.error(str(msg))

# python argparse_FileType.py -h
# python argparse_FileType.py -i argparse_FileType.py
# python argparse_FileType.py -i argparse_FileType.py -o /tmp/file.txt
# python argparse_FileType.py -i nosuchfile.txt

