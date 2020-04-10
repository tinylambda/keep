import types


def set_age(self, age):
    self.age = age


class Student:
    pass


if __name__ == '__main__':
    s1 = Student()
    s1.set_age = types.MethodType(set_age, s1)
    s1.set_age(22)
    print(s1.age)

    s2 = Student()
    s2.set_age(23)
    print(s2.age)

