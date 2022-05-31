import itertools


if __name__ == "__main__":

    def vowel(c):
        return c.lower() in "aeiou"

    print(list(filter(vowel, "Aardvark")))

    print(list(itertools.dropwhile(vowel, "Aardvark")))

    print(list(itertools.takewhile(vowel, "Aardvark")))

    print(list(itertools.compress("Aardvark", (1, 0, 1, 1, 0, 1))))

    print(list(itertools.islice("Aardvark", 4)))
    print(list(itertools.islice("Aardvark", 4, 7)))
    print(list(itertools.islice("Aardvark", 1, 7, 2)))
