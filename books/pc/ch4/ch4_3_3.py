def countdown(n):
    print("starting to count from", n)
    while n > 0:
        yield n
        n -= 1
    print("done!")


if __name__ == "__main__":
    c = countdown(3)
    print(c)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
