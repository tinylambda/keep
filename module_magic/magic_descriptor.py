import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess:
    def __get__(self, instance, owner):
        value = instance._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, instance, value):
        logging.info('Updating %r to %r', 'age', value)
        instance._age = value


class Person:
    # Descriptors only work when used as class variables. When put in instances, they have no effect.
    # The main motivation for descriptors is to provide a hook allowing objects stored in class variables
    # to control what happens during attribute lookup.
    age = LoggedAgeAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


if __name__ == '__main__':
    mary = Person('Mary M', 30)
    dave = Person('David D', 40)

    print(vars(mary))
    print(vars(dave))

    print(mary.age)
    mary.birthday()

    print(dave.name)
    print(dave.age)

