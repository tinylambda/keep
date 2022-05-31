class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print("getattr:", item)
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith("_"):
            super().__setattr__(key, value)
        else:
            print("setattr:", key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith("_"):
            super().__delattr__(item)
        else:
            print("delattr:", item)
            delattr(self._obj, item)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print("Spam.bar", self.x, y)


if __name__ == "__main__":
    s = Spam(2)
    p = Proxy(s)
    print(p.x)
    p.bar(3)
    p.x = 7
