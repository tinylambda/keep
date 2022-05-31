import numpy as np


def triangle_wave(x, c, c0, hc):
    x = x - int(x)
    if x >= c:
        r = 0.0
    elif x < c0:
        r = x / c0 * hc
    else:
        r = (c - x) / (c - c0) * hc
    return r


if __name__ == "__main__":
    x = np.linspace(0, 2, 1000)
    y1 = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])
    print(y1)

    triangle_ufunc1 = np.frompyfunc(triangle_wave, 4, 1)
    y2 = triangle_ufunc1(x, 0.6, 0.4, 1.0)
    print(y2, y2.dtype)
    y2 = y2.astype(float)
    print(y2, y2.dtype)

    triangle_ufunc2 = np.vectorize(triangle_wave, otypes=[float])
    y3 = triangle_ufunc2(x, 0.6, 0.4, 1.0)
    print(y3)

    print(np.all(y1 == y2))
    print(np.all(y2 == y3))
