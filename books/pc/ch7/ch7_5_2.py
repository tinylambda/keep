def spam(a, b=42):
    print(a, b)


def foo(a, b=None):
    if b is None:
        b = []
    print(a, b)


_no_value = object()


def bar(a, b=_no_value):
    if b is _no_value:
        print("no b value supplied")
    print(a, b)


if __name__ == "__main__":
    spam(1)
    spam(1, 2)

    foo(1)
    foo(1, [2, 3])

    bar(1)
    bar(1, [])
    bar(1, None)
