import site
import os
import sys


script_directory = os.path.dirname(__file__)
module_directory = os.path.join(script_directory, sys.argv[1])

try:
    import mymodule
except ImportError as err:
    print('Could not import mymodule: ', err)

print()
before_len = len(sys.path)
site.addsitedir(module_directory)
print('New paths: ')
for p in sys.path[before_len:]:
    print(p.replace(os.getcwd(), '.'))
print()

import mymodule


# python site_addsiteaddr.py with_modules
