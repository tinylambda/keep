import numpy as np

if __name__ == '__main__':
    arr = np.array([[1., 2., 3.], [4., 5., 6.]])
    print(arr)

    print(arr * arr)
    print(arr - arr)

    print(1 / arr)
    print(arr ** 0.5)

    arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
    print(arr2)
    print(arr2 > arr)

