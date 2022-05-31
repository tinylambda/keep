def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump


if __name__ == "__main__":
    iterator = jumping_range(5)
    print(next(iterator))
    print(iterator.send(2))
    print(next(iterator))
    print(iterator.send(-1))
    for x in iterator:
        print(x)
