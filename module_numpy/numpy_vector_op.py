import numpy as np

if __name__ == "__main__":
    arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    print(arr)

    print(arr * arr)
    print(arr - arr)

    print(1 / arr)
    print(arr**0.5)

    arr2 = np.array([[0.0, 4.0, 1.0], [7.0, 2.0, 12.0]])
    print(arr2)
    print(arr2 > arr)
