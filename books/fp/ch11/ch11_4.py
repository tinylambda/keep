import collections
import random

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(1, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index, value):
        self._cards.insert(index, value)


if __name__ == "__main__":
    fd = FrenchDeck2()
    print(
        isinstance(fd, collections.Sized),
        isinstance(fd, collections.MutableSequence),
        isinstance(fd, collections.Sequence),
        isinstance(fd, collections.UserDict),
        isinstance(fd, collections.Callable),
        isinstance(fd, collections.Iterable),
        isinstance(fd, collections.UserString),
        isinstance(fd, collections.Mapping),
    )

    print(
        fd.count(1),
        fd[23],
    )

    print([item for item in fd])
    random.shuffle(fd)
    print([item for item in fd])

    print(isinstance(fd, collections.Hashable))
    print(hash(fd))
