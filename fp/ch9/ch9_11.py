from fp.ch9.ch9_1 import Vector2d


if __name__ == '__main__':
    v1 = Vector2d(1.1, 2.2)
    dumped = bytes(v1)
    print(dumped, len(dumped))

    v1.typecode = 'f'
    dumpf = bytes(v1)
    print(dumpf, len(dumpf))

    print(Vector2d.typecode)

