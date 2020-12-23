class Foo:
    pass


x = Foo()
print(type(x))  # type of x is class Foo
print(type(Foo))  # type of Foo is type

for t in int, float, dict, list, tuple:
    print(type(t))

print(type(type))

# type is a metaclass, of which classes are instances.
# x is an instance of class Foo
# Foo is an instance of the type metaclass
# type is also an instance of the type metaclass, so it is an instance of itself

