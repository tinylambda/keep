import numpy as np

if __name__ == "__main__":
    a = np.arange(0, 60, 10).reshape(-1, 1)
    print(a, a.shape)

    b = np.arange(0, 5)
    print(b, b.shape)

    c = a + b
    print(c, c.shape)

    x, y = np.ogrid[:5, :5]
    print(x, x.shape)
    print(y, y.shape)

    x, y = np.mgrid[:5, :5]
    print(x, x.shape)
    print(y, y.shape)

    x = np.array([0, 1, 4, 10])
    y = np.array([2, 3, 8])

    gy, gx = np.ix_(y, x)
    print("gx", gx)
    print("gy", gy)
    print("gx + gy", gx + gy)
