from pprint import pprint

import numpy as np


if __name__ == '__main__':
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

    print(b)
    print(c)

    print('get shape')
    print(a.shape)
    print(c.shape)

    print('set shape')
    c.shape = 4, 3
    print(c)

    print('set -1 on an axis will compute it automatically')
    c.shape = 2, -1
    print(c)

    print('Use reshape to generate new array, keep original untouched')
    d = a.reshape(2, 2)
    print(d)
    print(a)

    print('a and d share the underlying data')
    a[1] = 100
    print(d)

    print('get dtype')
    print(c.dtype)

    print('set dtype')
    s1 = np.array([1, 2, 3, 4], dtype=float)
    s2 = np.array([1, 2, 3, 4], dtype=complex)
    print(s1)
    print(s2)

    print('np.typeDict')
    pprint(np.typeDict)

    print('np.arange')
    pprint(np.arange(0, 1, 0.1))

    print('np.linspace endpoint=True')
    pprint(np.linspace(0, 1, 10))

    print('np.linspace endpoint=False')
    pprint(np.linspace(0, 1, 10, endpoint=False))

    print('np.logspace base 10')
    pprint(np.logspace(0, 2, 5))

    print('np.logspace base 2')
    pprint(np.logspace(0, 2, 5, base=2))

    print('np.logspace base 2 endpoint False')
    pprint(np.logspace(0, 1, 12, base=2, endpoint=False))

    print('\nnp.empty')
    pprint(np.empty((2, 3), dtype=int))

    print('\nnp.zeros')
    pprint(np.zeros((2, 3), dtype=int))

    print('\nnp.frombuffer')
    s = b'abcdefgh'
    pprint(np.frombuffer(s, dtype=np.int8))

    print('\nnp.frombuffer dtype np.int16')
    pprint(np.frombuffer(s, dtype=np.int16))

    print('\nnp.frombuffer dtype float')
    pprint(np.frombuffer(s, dtype=float))

    print('\nnp.fromfunction')

    def func(i):
        return i % 4 + 1

    pprint(np.fromfunction(func, (10, )))

    print('\nnp.fromfunction 2d')

    def func2(i, j):
        return (i + 1) * (j + 1)

    pprint(np.fromfunction(func2, (9, 9)))
