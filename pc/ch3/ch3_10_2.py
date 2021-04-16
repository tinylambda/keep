import numpy as np
import numpy.linalg


if __name__ == '__main__':
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)

    print(m.T)
    print(m.I)

    v = np.matrix([[2], [3], [4]])
    print(v)
    print(m * v)

    print(numpy.linalg.det(m))
    print(numpy.linalg.eigvals(m))
    x = numpy.linalg.solve(m, v)
    print(x)

    print(m * x)
    print(v)


