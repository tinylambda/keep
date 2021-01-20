import numpy as np

if __name__ == '__main__':
    arr1 = np.array([1, 2, 3], dtype=np.float64)
    arr2 = np.array([1, 2, 3], dtype=np.int32)

    print(arr1, arr1.dtype)
    print(arr2, arr2.dtype)

    arr = np.array([1, 2, 3, 4, 5])
    print(arr.dtype)

    float_arr = arr.astype(np.float64)
    print(float_arr, float_arr.dtype)

    arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
    print(arr, arr.dtype)

    print(arr.astype(np.int32))

    numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
    print(numeric_strings.astype(float))

    int_array = np.arange(10)
    print(int_array, int_array.dtype)

    calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
    print(int_array.astype(calibers.dtype))

    empty_uint32 = np.empty(8, dtype='u4')
    print(empty_uint32, empty_uint32.dtype)

