from itertools import accumulate


def f(a, b):
    print(a, b)
    return b + a + b


print(list(accumulate("abcde", f)))
