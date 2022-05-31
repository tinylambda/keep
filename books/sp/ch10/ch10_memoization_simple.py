import math

_SIN_MEMOIZATION_VALUES = {}


def memoized_sin(x):
    if x not in _SIN_MEMOIZATION_VALUES:
        _SIN_MEMOIZATION_VALUES[x] = math.sin(x)
    return _SIN_MEMOIZATION_VALUES[x]


if __name__ == "__main__":
    print(memoized_sin(1))
    print(_SIN_MEMOIZATION_VALUES)
    print(memoized_sin(2))
    print(_SIN_MEMOIZATION_VALUES)
    print(memoized_sin(2))
    print(_SIN_MEMOIZATION_VALUES)
    print(memoized_sin(1))
    print(_SIN_MEMOIZATION_VALUES)
