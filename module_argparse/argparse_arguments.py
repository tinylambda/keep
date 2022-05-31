import argparse

parser = argparse.ArgumentParser(description="example with optional arguments")
parser.add_argument("count", action="store", type=int)
parser.add_argument("units", action="store")
print(parser.parse_args())
