b = 6


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__ == "__main__":
    f3(3)
    print(b)

    f3(3)

    b = 30
