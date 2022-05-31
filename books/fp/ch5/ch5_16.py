from operator import mul
from functools import partial


if __name__ == "__main__":
    triple = partial(mul, 3)
    print(triple(7))

    print(list(map(triple, range(1, 10))))
