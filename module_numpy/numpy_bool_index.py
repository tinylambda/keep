import numpy as np


if __name__ == "__main__":
    names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
    data = np.random.randn(7, 4)

    print(names)
    print(data)

    print(names == "Bob")

    print(data[names == "Bob"])
    print(data[names == "Bob", 2:])
    print(data[names == "Bob", 3])

    print(names != "Bob")
    print(data[~(names == "Bob")])

    cond = names == "Bob"
    print(data[~cond])

    mask = (names == "Bob") | (names == "Will")
    print(mask)
    print(data[mask])

    data[data < 0] = 0
    print(data)

    data[names != "Joe"] = 7
    print(data)
