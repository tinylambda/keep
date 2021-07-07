from inspect import Signature, Parameter


def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(params)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


if __name__ == '__main__':
    import inspect
    print(inspect.signature(Stock))

    s1 = Stock('HUAWEI', 100, 490.1)
    try:
        s2 = Stock('HUAWEI', 100)
    except TypeError as e:
        print(e)

    try:
        s1 = Stock('HUAWEI', 100, 490.1, shares=100)
    except TypeError as e:
        print(e)

