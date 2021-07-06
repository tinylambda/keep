import weakref

_spam_cache = weakref.WeakValueDictionary()


class Spam:
    def __init__(self, name):
        self.name = name


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    return _spam_cache[name]


if __name__ == '__main__':
    a = get_spam('foo')
    b = get_spam('bar')
    print(a is b)
    c = get_spam('foo')
    print(a is c)

