from timeit import timeit


if __name__ == "__main__":
    x = timeit("math.sqrt(2)", "import math")
    print(x)

    y = timeit("sqrt(2)", "from math import sqrt")
    print(y)

    x = timeit("math.sqrt(2)", "import math", number=10000000)
    print(x)

    y = timeit("sqrt(2)", "from math import sqrt", number=10000000)
    print(y)
