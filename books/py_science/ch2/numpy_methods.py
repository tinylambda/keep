import numpy as np

if __name__ == '__main__':
    np.random.seed(0)
    a = np.random.randint(0, 10, size=(4, 5))
    print('a:', a)
    print('np.sum(a):', np.sum(a))
    print('np.sum(a, axis=1):', np.sum(a, axis=1))
    print('np.sum(a, axis=0):', np.sum(a, axis=0))

    b = np.ones(1000000, dtype=np.float32) * 1.1
    print('b:', b)
    print('np.sum(b):', np.sum(b))
    print('np.sum(b, dtype=np.double):', np.sum(b, dtype=np.double))

    print('np.mean(a):', np.mean(a))
    print('np.mean(a, axis=1):', np.mean(a, axis=1))
    print('np.mean(a, axis=0):', np.mean(a, axis=0))

    print('np.max(a):', np.max(a))
    print('np.min(a):', np.min(a))
    print('np.ptp(a):', np.ptp(a))

    print('np.argmax(a):', np.argmax(a))
    print('np.argmax(a, axis=0):', np.argmax(a, axis=0))
    print('np.argmax(a, axis=1):', np.argmax(a, axis=1))
    print('a.ravel()[2]:', a.ravel()[2])

    idx = np.unravel_index(np.argmax(a), shape=a.shape)
    print('np.unravel_index(np.argmax(a), shape=a.shape) idx =', idx)
    print('a[idx]:', a[idx])

    idx = np.argmax(a, axis=1)
    print('idx = np.argmax(a, axis=1):', idx)
    print('max value of every row:', a[range(a.shape[0]), idx])

    print('np.sort(a):', np.sort(a))
    print('np.sort(a, axis=0):', np.sort(a, axis=0))
    print('np.sort(a, axis=None):', np.sort(a, axis=None))

    idx = np.argsort(a)
    print('np.argsort(a) idx = ', idx)
