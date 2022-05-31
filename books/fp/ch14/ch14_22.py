import itertools


if __name__ == "__main__":
    print(list(itertools.combinations("ABC", 2)))

    print(list(itertools.combinations_with_replacement("ABC", 2)))

    print(list(itertools.permutations("ABC", 2)))

    print(list(itertools.product("ABC", repeat=2)))
