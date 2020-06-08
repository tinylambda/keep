import linecache
from module_linecache.linecache_data import *


filename = make_tempfile()

# Blank lines include the new line
print('BLANK: {!r}'.format(linecache.getline(filename, 8)))

cleanup(filename)

