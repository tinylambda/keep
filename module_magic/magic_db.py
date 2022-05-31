class LazyDB:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = "Value for %s" % item
        setattr(self, item, value)
        return value


class LoggingLazyDB(LazyDB):
    def __getattr__(self, item):
        print("Called __getattr__(%s)" % item)
        return super(LoggingLazyDB, self).__getattr__(item)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print("Called __getattribute__(%s)" % item)
        try:
            return super(ValidatingDB, self).__getattribute__(item)
        except AttributeError:
            value = "Value for %s" % item
            setattr(self, item, value)
            return value


class MissingPropertyDB:
    def __getattr__(self, item):
        if item == "bad_name":
            raise AttributeError("%s is missing" % item)


class SavingDB:
    def __setattr__(self, key, value):
        super(SavingDB, self).__setattr__(key, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, key, value):
        print("Called __setattr__(%s, %r)" % (key, value))
        super(LoggingSavingDB, self).__setattr__(key, value)


class BrokenDictionaryDB:
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, item):
        print("Called __getattribute__(%s)" % item)
        return self._data[item]


class DictionaryDB:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        data_dict = super(DictionaryDB, self).__getattribute__("_data")
        return data_dict[item]


if __name__ == "__main__":
    # data = LazyDB()
    # print('Before: ', data.__dict__)
    # print('foo: ', data.foo)
    # print('After: ', data.__dict__)

    # data = LoggingLazyDB()
    # print('exists: ', data.exists)
    # print('foo: ', data.foo)
    # print('foo: ', data.foo)

    # data = ValidatingDB()
    # print('exists: ', data.exists)
    # print('foo: ', data.foo)
    # print('foo: ', data.foo)
    #
    # data = MissingPropertyDB()
    # data.bad_name

    # data = LoggingLazyDB()
    # print('Before: ', data.__dict__)
    # print('foo exists: ', hasattr(data, 'foo'))
    # print('After: ', data.__dict__)
    # print('foo exists: ', hasattr(data, 'foo'))

    # data = ValidatingDB()
    # print('foo exists: ', hasattr(data, 'foo'))
    # print('foo exists: ', hasattr(data, 'foo'))

    # data = LoggingSavingDB()
    # print('Before: ', data.__dict__)
    # data.foo = 5
    # print('After: ', data.__dict__)
    # data.foo = 7
    # print('Finally: ', data.__dict__)

    data = BrokenDictionaryDB({"foo": 3})
    data.foo
