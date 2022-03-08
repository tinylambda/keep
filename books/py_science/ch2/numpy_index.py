import numpy as np

if __name__ == '__main__':
    a = np.arange(3 * 4 * 5).reshape((3, 4, 5))
    print(a)

    lidx = [[0], [1], [2]]
    aidx = np.array(lidx)

    print('tuple index', a[tuple(lidx)])
    print('array index', a[aidx])
