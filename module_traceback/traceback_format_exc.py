import traceback

from module_traceback.traceback_example import produce_exception


try:
    produce_exception()
except Exception as err:
    # Like print_exc() but return a string
    # Can be used to extract exception and send it through HTTP API
    s = traceback.format_exc()
    print(s)

