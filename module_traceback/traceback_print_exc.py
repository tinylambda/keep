import traceback
import sys

from module_traceback.traceback_example import produce_exception


print("print_exc() with no exception:")
traceback.print_exc(file=sys.stdout)
print()

try:
    produce_exception()
except Exception as err:
    print("print_exc():")
    traceback.print_exc(file=sys.stdout)
    print()
    print("print_exc(1):")
    traceback.print_exc(limit=1, file=sys.stdout)
