import numpy as np


if __name__ == '__main__':
    arr = np.arange(10)
    print(arr)

    print(arr[5])
    print(arr[5:8])
    arr[5:8] = 12
    print(arr)

    arr_slice = arr[5:8]
    print(arr_slice)

    arr_slice[1] = 12345
    print(arr)

    arr_slice[:] = 64
    print(arr)

    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr_2d[2])
    print(arr_2d[0][2])

    arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(arr_3d)
    print(arr_3d.shape)
    print(arr_3d[0].shape)

    old_values = arr_3d[0].copy()
    arr_3d[0] = 42
    print(arr_3d)

    arr_3d[0] = old_values
    print(arr_3d)

    print(arr_3d[1, 0])

    print(arr[1:6])
    print(arr_2d[:2])
    print(arr_2d[:2, 1:])
    print(arr_2d[1, :2])
    print(arr_2d[:2, 2])
    print(arr_2d[:, :1])
    arr_2d[:2, 1:] = 0
    print(arr_2d)
