import argparse

parser = argparse.ArgumentParser(description='short sample app')
parser.add_argument('-a', action='store_true', default=False)
parser.add_argument('-b', action='store', dest='b')
parser.add_argument('-c', action='store', type=int)

print(parser.parse_args(['-a', '-bval', '-c', '3']))

