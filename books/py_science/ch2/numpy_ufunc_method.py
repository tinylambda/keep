import numpy as np

if __name__ == "__main__":
    print("add reduce", np.add.reduce([1, 2, 3]))
    print("add reduce axis=1", np.add.reduce([[1, 2, 3], [4, 5, 6]], axis=1))
    print("add reduce axis=0", np.add.reduce([[1, 2, 3], [4, 5, 6]], axis=0))

    print("add accumulate", np.add.accumulate([1, 2, 3]))
    print("add accumulate axis=1", np.add.accumulate([[1, 2, 3], [4, 5, 6]], axis=1))
    print("add accumulate axis=0", np.add.accumulate([[1, 2, 3], [4, 5, 6]], axis=0))

    a = np.array([1, 2, 3, 4])
    result = np.add.reduceat(a, indices=[0, 1, 0, 2, 0, 3, 0])
    print("add reduceat", result)

    result = np.multiply.outer([1, 2, 3, 4, 5], [2, 3, 4])
    print("multiply outer", result)
