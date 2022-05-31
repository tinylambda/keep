import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", type=int)
parser.add_argument("-f", type=float)
parser.add_argument("--file", type=open)

try:
    print(parser.parse_args())
except IOError as msg:
    parser.error(str(msg))

# python argparse_type.py -i 100
# python argparse_type.py -f 100
# python argparse_type.py --file /tmp/a.log
# python argparse_type.py --file argparse_type.py
