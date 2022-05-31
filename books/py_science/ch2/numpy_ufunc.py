from pprint import pprint

import numpy as np


if __name__ == "__main__":
    x = np.linspace(0, 2 * np.pi, 10)
    y = np.sin(x)
    pprint(y)

    t = np.sin(x, out=x)
    pprint(x)
    pprint(t is x)

    a = np.arange(0, 4)
    b = np.arange(1, 5)
    print("a: ", a)
    print("b: ", b)
    print("np.add(a, b): ", np.add(a, b))
    print("a + b = ", a + b)
    print("a - b = ", a - b)
    print("a * b = ", a * b)
    print("a / b = ", a / b)
    print("a // b = ", a // b)
    print("-a = ", -a)
    print("a ** b = ", a**b)
    print("a % b = ", a % b)

    print("a < b = ", a < b, np.less(a, b))
    print("a <= b = ", a <= b, np.less_equal(a, b))
    print("a == b = ", a == b, np.equal(a, b))
    print("a != b = ", a != b, np.not_equal(a, b))
    print("a > b = ", a > b, np.greater(a, b))
    print("a >= b = ", a >= b, np.greater_equal(a, b))

    print("np.logical_or: ", np.logical_or(a == b, a < b))
    print("np.logical_and: ", np.logical_and(a == b, a < b))
    print("np.logical_not: ", np.logical_not(a == b))
    print("np.logical_xor: ", np.logical_xor(a == b, a < b))

    print("np.any(a == b): ", np.any(a == b))
    print("np.all(a == b): ", np.all(a == b))

    print("(a == b) | (a > b): ", (a == b) | (a > b), np.bitwise_or(a == b, a > b))
    print("(a == b) & (a > b): ", (a == b) & (a > b), np.bitwise_and(a == b, a > b))
    print("~(a == b): ", ~(a == b), np.bitwise_not(a == b))
    print("(a == b) ^ (a > b): ", (a == b) ^ (a > b), np.bitwise_xor(a == b, a > b))

    c0 = np.arange(5)
    print("~c0: ", ~c0, np.bitwise_not(c0))

    c1 = np.arange(5, dtype=np.uint8)
    print("~c1: ", ~c1, np.bitwise_not(c1))
