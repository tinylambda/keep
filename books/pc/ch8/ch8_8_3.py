class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('expected a string!!!')
        instance.__dict__[self.name] = value


class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson(Person):
    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete(self)


if __name__ == '__main__':
    s = SubPerson('Guido')
    s.name = 'Felix'
    s.name = 47

