import getpass
import sys


if sys.stdin.isatty():
    p = getpass.getpass('using getpass: ')
else:
    print('using readline')
    p = sys.stdin.readline().rstrip()

print('read: ', p)

