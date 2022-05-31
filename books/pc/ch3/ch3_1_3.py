if __name__ == "__main__":
    x = 1.23456
    print(format(x, "0.2f"))

    print(format(x, "0.3f"))

    print("value is {:0.3f}".format(x))

    a = 2.1
    b = 4.2
    c = a + b
    print(c)

    c = round(c, 2)  # not recommended
    print(c)
