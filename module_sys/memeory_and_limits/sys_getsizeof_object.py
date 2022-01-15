import sys


class WithoutAttributes:
    pass


class WithAttributes:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return


if __name__ == '__main__':
    without_attrs = WithoutAttributes()
    print('WithoutAttributes: ', sys.getsizeof(without_attrs))

    with_attrs = WithAttributes()
    print('WIthAttributes: ', sys.getsizeof(with_attrs))
