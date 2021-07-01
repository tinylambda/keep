def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, name):
        print('getting', str(name))
        return cls_getitem(self, name)

    def __setitem__(self, key, value):
        print('setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('deleting', str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


if __name__ == '__main__':
    @LoggedMapping
    class LoggedDict(dict):
        pass

    d = LoggedDict()
    d['x'] = 100
    d['x']
    del d['x']

