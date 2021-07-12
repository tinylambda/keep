import operator
from first import first


def greater_than_zero(number):
    return number > 0


if __name__ == '__main__':
    print(first([-1, 0, 1, 2], key=greater_than_zero))


