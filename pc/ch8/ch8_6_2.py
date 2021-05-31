class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('cannot delete attribute')


if __name__ == '__main__':
    a = Person('Guido')
    print(a.first_name)
    try:
        a.first_name = 42
    except Exception as e:
        print(e)

    try:
        del a.first_name
    except Exception as e:
        print(e)

