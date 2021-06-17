import collections.abc
import bisect
from abc import ABC


class SortedItems(collections.abc.Sequence, ABC):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == '__main__':
    items = SortedItems([5, 1, 3])
    print(list(items))

    print(items[-1])
    items.add(2)
    print(list(items))
    items.add(-10)
    print(list(items))
    print(items[1:4])
    print(3 in items)
    print(len(items))

    for n in items:
        print(n)

    print(isinstance(items, collections.abc.Iterable))
    print(isinstance(items, collections.abc.Sequence))
    print(isinstance(items, collections.abc.Container))
    print(isinstance(items, collections.abc.Sized))
    print(isinstance(items, collections.abc.Mapping))
