import numpy as np


if __name__ == "__main__":
    data = np.random.randn(2, 3)
    print(data)

    data2 = data * 10
    print(data2)

    data3 = data + data
    print(data3)

    print(data.shape)
    print(data.dtype)
