import numpy as np


if __name__ == "__main__":
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    print(arr)

    print(arr[[4, 3, 0, 6]])
    print(arr[[-3, -5, -7]])

    arr = np.arange(32).reshape((8, 4))
    print(arr)

    print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

    print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
