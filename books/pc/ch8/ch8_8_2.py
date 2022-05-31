class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("cannot delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print("getting name")
        return super().name

    @name.setter
    def name(self, value):
        print("setting name to", value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("deleting name")
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPerson2(Person):
    @Person.name.getter
    def name(self):
        print("getting name")
        return super().name


class SubPerson3(Person):
    @Person.name.setter
    def name(self, value):
        print("setting name to", value)
        super(SubPerson3, SubPerson3).name.__set__(self, value)


class SubPerson4(Person):
    @Person.name.getter
    def name(self):
        print("getting name")
        return super().name


if __name__ == "__main__":
    s = SubPerson("Guido")
    print(s.name)
    s.name = "Larry"
    try:
        s.name = 42
    except Exception as e:
        print(e)

    s2 = SubPerson2("Guido2")
    print(s2.name)

    s3 = SubPerson3("Guido3")
    print(s3.name)
    s3.name = "Felix"
    print(s3.name)

    try:
        s4 = SubPerson4("Guido4")
        print(s4.name)
    except AttributeError as e:
        print(e)
