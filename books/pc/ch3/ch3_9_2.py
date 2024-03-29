import numpy as np


if __name__ == "__main__":
    print("python lists")
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    # print(x + 10)  # error
    print(x + y)

    print("numpy arrays")
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + 10)
    print(ax + ay)
    print(ax * ay)

    print("spread function call to every element of array")

    def f(x):
        return 3 * x**2 - 2 * x + 7

    print(f(ax))

    print(np.sqrt(ax))
    print(np.cos(ax))

    print("grid: ")
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    print(grid)
    grid += 10
    print(grid)
    print(np.sin(grid))

    print("some experiments")
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    print(a[1])
    print(a[:, 1])
    a[1:3, 1:3] += 10
    print(a)

    print(a + [100, 101, 102, 103])
    print(a)

    print(np.where(a < 10, a, 10))
