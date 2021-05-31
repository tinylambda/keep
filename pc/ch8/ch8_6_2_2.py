class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError('cannot delete attribute')

    name = property(get_first_name, set_first_name, del_first_name)


if __name__ == '__main__':
    p = Person('Pan')
    print(p.name)
    try:
        p.name = 42
    except Exception as e:
        print(e)

    try:
        del p.name
    except Exception as e:
        print(e)
