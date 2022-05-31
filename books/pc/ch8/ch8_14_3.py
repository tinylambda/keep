import collections.abc
from abc import ABC


class Items(collections.abc.MutableSequence, ABC):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, item):
        print("getting:", item)
        return self._items[item]

    def __setitem__(self, key, value):
        print("setting:", key, value)
        self._items[key] = value

    def __delitem__(self, key):
        print("deleting:", key)
        del self._items[key]

    def insert(self, index: int, value) -> None:
        print("inserting:", index, value)
        self._items.insert(index, value)

    def __len__(self):
        print("len")
        return len(self._items)


if __name__ == "__main__":
    items = Items([1, 2, 3])
    print(len(items))

    print("-" * 64)

    items.append(4)
    print(list(items))

    print("-" * 64)
    print(items.count(2))

    print("-" * 64)
    items.remove(3)
