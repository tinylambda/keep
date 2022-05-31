import numpy


if __name__ == "__main__":
    a = numpy.arange(12)
    print(a, type(a))
    print(a.shape)
    a.shape = 3, 4
    print(a)

    print(a[2])
    print(a[2][1])

    print(a[:, 1])

    b = a.transpose()
    print(b)
