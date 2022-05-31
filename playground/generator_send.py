def minimize():
    current = yield  # current will be the first value sent from outside
    while True:
        value = (
            yield current
        )  # return current to outside and set value to the sent value (new value)
        current = min(value, current)


if __name__ == "__main__":
    it = minimize()
    next(it)
    print(it.send(10))
    print(it.send(4))
    print(it.send(22))
    print(it.send(-1))
