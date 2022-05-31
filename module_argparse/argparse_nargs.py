import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--three", nargs=3)
parser.add_argument("--optional", nargs="?")
parser.add_argument("--all", nargs="*", dest="all")
parser.add_argument("--one-or-more", nargs="+")

print(parser.parse_args())

# python argparse_nargs.py -h
# python argparse_nargs.py --three <- error
# python argparse_nargs.py --three a b c
# python argparse_nargs.py --optional with_value
# python argparse_nargs.py --one-or-more  <- error
# python argparse_nargs.py --one-or-more with multiple values
