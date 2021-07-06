import weakref


class CacheSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            self._cache[name] = Spam()
        return self._cache[name]

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CacheSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(self):
        return Spam.manager.get_spam(self.name)


if __name__ == '__main__':
    a = Spam('foo')
    b = Spam('foo')
    print(a is b)

