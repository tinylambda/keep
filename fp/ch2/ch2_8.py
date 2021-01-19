if __name__ == '__main__':
    a, b, *args = range(5)
    print(a, b)
    print(args)

    a, b, *args = range(3)
    print(a, b)
    print(args)

    a, b, *args = range(2)
    print(a, b)
    print(args)

    a, *body, c, d = range(5)
    print(a, c, d)
    print(body)

    *head, b, c, d = range(5)
    print(b, c, d)
    print(head)

