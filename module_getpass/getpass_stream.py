import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print('you entered: ', p)

