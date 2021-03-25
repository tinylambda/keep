import sys


class Finder:
    def find_loader(self, name):
        print('Looking for', name)
        return None, []


def check_url(path):
    if path.startswith('http://'):
        return Finder()
    else:
        raise ImportError()


sys.path.append('http://localhost:15000')
sys.path_hooks[0] = check_url


try:
    import fib
except Exception:
    pass

print(sys.path_importer_cache['http://localhost:15000'])

