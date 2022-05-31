import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(id(cls), cls)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args, **kwargs):
        if len(args) != len(cls._fields):
            raise ValueError("{} arguments required".format(len(cls._fields)))
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ["name", "shares", "price"]


class Point(StructTuple):
    _fields = ["x", "y"]


if __name__ == "__main__":
    s = Stock("HUAWEI", 50, 91.1)
    s2 = Stock("TET", 100, 100.0)
    print(id(s.__class__))
    print(id(s2.__class__))
    print(s)
    print(s[0])
    print(s.name)
    print(s.shares * s.price)
    try:
        s.shares = 23
    except AttributeError as e:
        print(e)
