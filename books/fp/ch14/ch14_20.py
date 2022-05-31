import itertools


if __name__ == "__main__":
    print(list(itertools.product("ABC", range(2))))

    suits = "spades hearts diamonds clubs".split()
    print(list(itertools.product("AK", suits)))

    print(list(itertools.product("ABC")))

    print(list(itertools.product("ABC", repeat=2)))

    print(list(itertools.product(range(2), repeat=3)))

    rows = itertools.product("AB", range(2), repeat=2)
    for row in rows:
        print(row)
