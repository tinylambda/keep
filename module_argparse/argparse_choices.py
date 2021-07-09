import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mode', choices=('read-only', 'read-write'))
print(parser.parse_args())

# python argparse_choices.py -h
# python argparse_choices.py --mode read-only
# python argparse_choices.py --mode invlaid

