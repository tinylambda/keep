import importlib


a = importlib.import_module('.a', package=__package__)


def bar():
    print('calling a.spam() in b.bar')
    a.spam()
