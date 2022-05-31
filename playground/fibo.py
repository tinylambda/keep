import itertools


class Fibonacci:
    def __iter__(self):
        return FibonacciGenerator()


class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fg = FibonacciGenerator()
    r = itertools.takewhile(lambda n: n < 1000, fg)
    print(list(r))

    fg2 = fibonacci()
    r = itertools.takewhile(lambda n: n < 1000, fg2)
    print(list(r))
