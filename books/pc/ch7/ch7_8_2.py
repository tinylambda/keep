def spam(a, b, c, d):
    print(a, b, c, d)


if __name__ == "__main__":
    from functools import partial

    s1 = partial(spam, 1)
    s1(2, 3, 4)
    s1(4, 5, 6)

    s2 = partial(spam, d=42)
    s2(1, 2, 3)
    s2(4, 5, 5)

    s3 = partial(spam, 1, 2, d=42)
    s3(3)
    s3(4)
    s3(5)
