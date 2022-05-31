import argparse

parser = argparse.ArgumentParser(description="short sample app")
parser.add_argument("--optional", action="store_true", default=False)
parser.add_argument("positional", action="store")
print(parser.parse_args())

# python argparse_default_grouping.py -h
