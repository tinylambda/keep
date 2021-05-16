def myfunc():
    return 1, 2, 3


if __name__ == '__main__':
    a, b, c = myfunc()
    print(a, b, c)

    x = myfunc()
    print(x)

