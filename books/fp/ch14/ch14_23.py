import itertools


if __name__ == "__main__":
    print(list(itertools.groupby("LLLLAAGGG")))

    for char, group in itertools.groupby("LLLLAAGGG"):
        print(char, "->", list(group))

    animals = ["duck", "eagle", "rat", "lion", "eagle", "shark", "giraffe", "dolphin"]
    animals.sort(key=len)
    print(animals)

    for length, group in itertools.groupby(animals, len):
        print(length, "->", list(group))

    for length, group in itertools.groupby(reversed(animals), len):
        print(length, "->", list(group))

    print(itertools.tee("ABC"))
    g1, g2 = itertools.tee("ABC")
    print(next(g1), next(g2))
    print(list(g1), list(g2))

    print(list(zip(*itertools.tee("ABC"))))
