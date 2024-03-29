class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be an int")
        self._age = value


def typed_property(name, expected_type):
    storage_name = f"_{name}"

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"{name} mut be a {expected_type}")
        setattr(self, storage_name, value)

    return prop


class Person2:
    name = typed_property("name", str)
    age = typed_property("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    from functools import partial

    String = partial(typed_property, expected_type=str)
    Integer = partial(typed_property, expected_type=int)

    class Person3:
        name = String("name")
        age = Integer("age")

        def __init__(self, name, age):
            self.name = name
            self.age = age

    p = Person("felix", 1)
    p2 = Person2("felix", 1)
    p3 = Person3("felix", 1)
