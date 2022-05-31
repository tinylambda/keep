import operator
from functools import partial
from first import first


def greater_than(number, _min=0):
    return number > _min


if __name__ == "__main__":
    print(first([-1, 0, 1, 2], key=partial(greater_than, _min=42)))
    print(first([-1, 0, 1, 2], key=partial(operator.le, 0)))
