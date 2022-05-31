if __name__ == "__main__":
    x = 42

    def spam(a, b=x):
        print(a, b)

    spam(1)
    x = 23
    spam(1)

    def foo(a, b=[]):
        print(b)
        return b

    x = foo(1)
    print(x)

    x.append(99)
    x.append("Yow!")
    print(x)

    foo(1)
