from ch8_13_2 import *


class CheckedMeta(type):
    def __new__(mcs, clsname, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(mcs, clsname, bases, class_dict)


class Stock(metaclass=CheckedMeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('ABCD', 77, 99.1)

