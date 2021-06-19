class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, item):
        return getattr(self._items, item)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __delitem__(self, key):
        del self._items[key]


if __name__ == '__main__':
    a = ListLike()
    a.append(2)
    a.insert(0, 1)
    a.sort()

    try:
        print(len(a))
    except TypeError as e:
        print(e)

    try:
        print(a[0])
    except TypeError as e:
        print(e)

