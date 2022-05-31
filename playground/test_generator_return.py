def g():
    r = 0
    for i in range(10):
        yield i
        r += i
    print("returning ", r)
    return r


if __name__ == "__main__":
    gg = g()
    for i in range(10):
        next(gg)
    try:
        next(gg)
    except StopIteration as e:
        print(e.value)
