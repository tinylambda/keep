import collections


if __name__ == '__main__':
    Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])
    print(Stock)
    print(type(Stock))

