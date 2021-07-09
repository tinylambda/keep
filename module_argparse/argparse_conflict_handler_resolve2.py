import argparse

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('-a', action='store')
parser.add_argument('--long-b', '-b', action='store', help='long and short together')
parser.add_argument('-b', action='store', help='short alone')
print(parser.parse_args(['-h']))

