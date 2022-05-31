import linecache
from module_linecache.linecache_data import *


filename = make_tempfile()

# The cache always returns a string, and uses
# an empty string to indicate a line which does
# not exist.
not_there = linecache.getline(filename, 500)
print("NOT THERE: {!r} includes {} characters".format(not_there, len(not_there)))

cleanup(filename)
