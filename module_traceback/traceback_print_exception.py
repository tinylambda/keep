import traceback
import sys

from module_traceback.traceback_example import produce_exception


try:
    produce_exception()
except Exception as err:
    print("print_exception():")
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_tb, file=sys.stderr)
