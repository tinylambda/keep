import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true')
group.add_argument('-b', action='store_true')

print(parser.parse_args())

# python argparse_mutually_exclusive.py -a
# python argparse_mutually_exclusive.py -b
# python argparse_mutually_exclusive.py -a -b  <- error

