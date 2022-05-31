import types
import urllib.request
import sys


def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode("utf-8")
    mod = sys.modules.setdefault(url, types.ModuleType(url))
    code = compile(source, url, "exec")
    mod.__file__ = url
    mod.__package__ = ""
    exec(code, mod.__dict__)
    return mod


if __name__ == "__main__":
    fib = load_module("http://127.0.0.1:15000/fib.py")
    r = fib.fib(10)
    print(r)

    spam = load_module("http://127.0.0.1:15000/spam.py")
    spam.hello("felix")

    print(spam)
    print(fib)
