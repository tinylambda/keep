from pprint import pprint

import numpy as np

if __name__ == '__main__':
    a = np.arange(10)
    pprint(a)

    print('\nget a single element')
    pprint(a[5])

    print('\nget part of an array')
    pprint(a[3:5])
    pprint(a[:5])
    pprint(a[:-1])

    print('\nmodify part of an array')
    a[2:4] = 100, 101
    pprint(a)

    print('\npart of an array with step')
    pprint(a[1:-1:2])

    print('\nreverse')
    pprint(a[::-1])

    print('\nnegative step')
    pprint(a[5:1:-2])

    print('\nsliced array share data with the original array')
    b = a[3:7]
    pprint(b)
    b[2] = -10
    pprint(b)
    pprint(a)

    print('\nnew array by list of ints')
    x = np.arange(10, 1, -1)
    pprint(x)
    pprint(x[[3, 3, 1, 8]])

    print('\ndo not share data')
    b = x[[3, 3, 1, 8]]
    pprint(b)
    b[2] = 100
    pprint(b)
    pprint(x)

    print('\nuse int list to change data')
    x[[1, 2, 3]] = -1, -2, -3
    pprint(x)

    print('\nuse int array')
    x = np.arange(10, 1, -1)
    pprint(x)
    pprint(x[np.array([3, 3, 1, 8])])
    pprint(x[np.array([[3, 3, 1, 8], [3, 3, 1, 8]])])

    print('\nuse bool array')
    x = np.arange(5, 0, -1)
    pprint(x)
    pprint(x[np.array([True, False, True, False, False])])

    print('\nuse bool list will return the same result')
    pprint(x[[True, False, True, False, False]])

    print('\nnot enough bools')
    try:
        pprint(x[[True, True]])
    except Exception as e:
        print(e)

    print('\nuse bool index to modify data')
    x[[True, True, False, False, False]] = 100, 200
    pprint(x)

    print('\ntest ufunc')
    x = np.random.rand(10)
    pprint(x)
    pprint(x > 0.5)
    pprint(x[x > 0.5])

