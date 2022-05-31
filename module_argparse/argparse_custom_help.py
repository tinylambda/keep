import argparse

parser = argparse.ArgumentParser(description="short sample app", add_help=True)
parser.add_argument("-a", action="store_true", default=False)
parser.add_argument("-b", action="store", dest="b")
parser.add_argument("-c", action="store", dest="c", type=int)

print("print_usage output:")
parser.print_usage()

print("print_help output:")
parser.print_help()
