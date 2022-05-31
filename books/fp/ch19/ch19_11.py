class Class:
    data = "the class data attr"

    @property
    def prop(self):
        return "the prop value"


if __name__ == "__main__":
    obj = Class()
    print(vars(obj))

    print(obj.data)

    obj.data = "bar"
    print(vars(obj))
    print(obj.data)

    print(Class.data)

    print(Class.prop)
    print(obj.prop)

    obj.__dict__["foo"] = "bar"
    print(vars(obj))
    print(obj.prop)

    Class.prop = "baz"
    print(obj.prop)

    print(obj.data)
    print(Class.data)
    Class.data = property(lambda self: 'the "data" prop value')
    print(obj.data)

    del Class.data
    print(obj.data)
