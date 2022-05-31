if __name__ == "__main__":
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y

    print(a(10))
    x = 15
    print(a(10))
    x = 3
    print(a(10))

    print("-" * 64)

    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10))
    print(b(10))
