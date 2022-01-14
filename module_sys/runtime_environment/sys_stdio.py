import sys

if __name__ == '__main__':
    print('STATUS: Reading from stdin', file=sys.stderr)
    data = sys.stdin.read()

    print('STATUS: Writing data to stdout', file=sys.stderr)
    sys.stdout.write(data)
    sys.stdout.flush()

    print('STATUS: Done', file=sys.stderr)
