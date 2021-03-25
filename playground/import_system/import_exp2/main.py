import sys

sys.path_importer_cache.clear()


def check_path(path):
    print('Checking', path)
    raise ImportError()


print(sys.path_hooks)
sys.path_hooks.insert(0, check_path)
import fib

