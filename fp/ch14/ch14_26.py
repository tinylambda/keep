from random import randint


def d6():
    return randint(1, 6)


if __name__ == '__main__':
    d6_iter = iter(d6, 1)
    print(d6_iter)

    for roll in d6_iter:
        print(roll)

