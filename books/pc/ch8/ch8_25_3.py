import weakref


class Spam:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('initializing Spam')
        self.name = name


if __name__ == '__main__':
    s = Spam('Felix')
    t = Spam('Felix')
    print(s is t)

