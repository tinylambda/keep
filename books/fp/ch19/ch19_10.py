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
