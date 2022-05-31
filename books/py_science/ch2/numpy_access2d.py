import numpy as np
from pprint import pprint


if __name__ == "__main__":
    a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
    pprint(a)

    print("\na[0, 3:5]")
    pprint(a[0, 3:5])

    print("\na[4:, 4:]")
    pprint(a[4:, 4:])

    print("\na[:, 2]")
    pprint(a[:, 2])

    print("\na[2::2, ::2]")
    pprint(a[2::2, ::2])

    print("\nslice share data with the original data")
    b = a[0, 3:5]
    pprint(b)
    b[0] = -b[0]
    pprint(b)
    pprint(a)

    print("\nuse slice object")
    idx = slice(None, None, 2), slice(2, None)  # [::2, 2:]
    pprint(a[idx])
    pprint(a[idx][idx])

    print("\ncreate slice object by s_")
    pprint(np.s_[::2, 2:])

    print("\ntuple or list of ints, array of ints or bool will create new data")
    pprint(a)
    pprint(a[(0, 1, 2, 3), (1, 2, 3, 4)])

    pprint(a[3:, [0, 2, 5]])
    pprint(a[3:, (0, 2, 5)])

    print("\nuse bool array")
    mask = np.array([1, 0, 1, 0, 0, 1], dtype=bool)
    pprint(a[mask, 2])

    mask2 = np.array([1, 0, 1, 0, 0, 1])
    pprint(a[mask, 2])

    mask3 = np.array([True, False, True, False, False, True])
    pprint(a[mask3, 2])

    print("\ndefault slice")
    b = a[[1, 2]]
    pprint(b)
    b[0][0] = -1000
    pprint(b)
    pprint(a)

    print("\nuse multi array")
    x = np.array([[0, 1], [2, 3]])
    y = np.array([[-1, -2], [-3, -4]])
    pprint(a[x, y])
    pprint(a[(0, 1, 2, 3), (-1, -2, -3, -4)].reshape(2, 2))

    print("\nonly specify the x axis")
    pprint(a[x])
