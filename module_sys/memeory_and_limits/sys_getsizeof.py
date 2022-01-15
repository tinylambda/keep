import sys


class MyClass:
    pass


if __name__ == '__main__':
    objects = [
        [], (), {}, 'c', 'string', b'bytes', 1, 2.3, MyClass, MyClass()
    ]

    for obj in objects:
        # reports the size of an object in bytes.
        print('{:>10}: {}'.format(type(obj).__name__, sys.getsizeof(obj)))
