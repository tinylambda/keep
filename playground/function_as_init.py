class A:
    pass


def f(self):
    print(self)


def __init__(self):
    print('in self')


A.f = f
A.__init__ = __init__


a = A()
a.f()

