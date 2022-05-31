def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == "__main__":
    fact = factorial
    print(fact)
    print(fact(5))
    r = map(fact, range(11))
    print(list(r))
