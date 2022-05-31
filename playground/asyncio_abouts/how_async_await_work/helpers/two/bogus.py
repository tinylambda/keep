def countdown(n):
    print("counting down from", n)
    while n > 0:
        newvalue = yield n
        # if a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


if __name__ == "__main__":
    c = countdown(5)
    for n in c:
        print(n)
        if n == 5:
            c.send(3)
