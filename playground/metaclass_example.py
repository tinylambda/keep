class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('new: ', name, bases, dct)
        dct.update({'attr10': 100})
        cls = super().__new__(mcs, name, bases, dct)
        return cls

    def __init__(cls, name, bases, dct):
        print('init: ', name, bases, dct)
        cls.attr = 100


class A(metaclass=Meta):
    def __init__(self):
        self.attr2 = 200


class B:
    attr = 100

    def __init__(self):
        self.attr2 = 200


class Test:
    a = 1

    def f(self):
        pass


if __name__ == '__main__':
    a = A()
    print(A.__dict__)
    print(a.__dict__)
    print(a.attr, a.attr2)

    b = B()
    print(b.__dict__)
    print(b.attr, b.attr2)

