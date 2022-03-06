import math
import time

import numpy as np

if __name__ == '__main__':
    scale = 1000000
    x = [i * 0.001 for i in range(scale)]
    start = time.perf_counter()
    for i, t in enumerate(x):
        x[i] = math.sin(t)
    print('match.sin: ', time.perf_counter() - start)

    x = [i * 0.001 for i in range(scale)]
    x = np.array(x)
    start = time.perf_counter()
    np.sin(x, out=x)
    print('numpy.sin: ', time.perf_counter() - start)

    x = [i * 0.001 for i in range(scale)]
    start = time.perf_counter()
    for i, t in enumerate(x):
        x[i] = np.sin(t)
    print('numpy.sin loop: ', time.perf_counter() - start)

    x = [i * 0.001 for i in range(scale)]
    start = time.perf_counter()
    y = [math.sin(t) for t in x]
    print('math.sin list comprehension: ', time.perf_counter() - start)

    print('type(math.sin(0.5)): ', type(math.sin(0.5)))
    print('type(np.sin(0.5)): ', type(np.sin(0.5)))

    print('item will return raw Python type:')
    a = np.arange(6.0).reshape((2, 3))
    print('type of item: ', type(a.item(1, 2)))
    print('type in np: ', type(a[1, 2]))


