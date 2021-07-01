import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


if __name__ == '__main__':
    d = StrKeyDict([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d[4])

    print(d.get('2'))
    print(d.get(4))
    print(d.get(1, 'N/A'))

    print(2 in d)
    print(1 in d)

    print(d[1])