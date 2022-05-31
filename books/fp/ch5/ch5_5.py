import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pickle(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self):
        return self.pickle()


if __name__ == "__main__":
    bingo = BingoCage(range(3))

    print(bingo.pickle())

    print(bingo())

    print(callable(bingo))

    print(bingo())
    print(bingo())
