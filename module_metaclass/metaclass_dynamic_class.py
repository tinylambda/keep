class DataCamp:
    pass


DataCampClass = type("DataCamp", (), {})
print(DataCampClass)
print(DataCamp())

# the builtin type() function, when passed one argument, returns the type of an object.
# For new style classes, that's generally the same as the object's __class__ attribute:
print(type(3))
print(type(["foo", "bar", "baz"]))
t = (1, 2, 3, 4, 5)
print(type(t))


class Foo:
    pass


print(type(Foo()))

# You can also call type() with three arguments --
# type(<name>, <bases>, <dct>):
# <name> specifies the class name. This becomes the __name__ attribute of the class.
# <bases> specifies a tuple of the base classes from which the class inherits.
# This become the __bases__ attribute of the class
# <dct> specifies a namespace dictionary containing definitions for the class body.
# This becomes the __dict__ attribute of the class.

# Calling type() in this manner creates a new instance of the type metaclass.
# In other words, it dynamically creates a new class.

# In each of the following examples, the top snippet defines a class dynamically with type(),
# while the snippet below it defines the class the usual way, with the class statement.
# In each case, the two snippets are functionally equivalent.

# In this first example, the <bases> and <dct> arguments passed to type() are both empty.
# No inheritance from any parent class is specified, and nothing is initially placed in the namespace dictionary.
# This is the simplest class definition possible.
Foo = type("Foo", (), {})
x = Foo()
print(x)


class Foo:
    pass


x = Foo()
print(x)

# Here <bases> is a tuple with a single element Foo, specifying the parent class that Bar inherits from.
# An attribute, attr is initially placed into the namespace dictionary:

Bar = type("Bar", (Foo,), dict(attr=100))
x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)


class Bar(Foo):
    attr = 100


x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)

# This time <bases> is again empty. Two objects are placed into the namespace dictionary via the <dct> argument.
# The first is an attribute named attr and the second a function named attr_val,
# which becomes a method of the defined class:

Foo = type("Foo", (), {"attr": 100, "attr_val": lambda self: self.attr})

x = Foo()
print(x.attr)
print(x.attr_val())


class Foo:
    attr = 100

    def attr_val(self):
        return self.attr


x = Foo()
print(x.attr)
print(x.attr_val())


# Only very simple functions can be defined with lambda in Python. In the following example,
# a slightly more complex function is defined externally then assigned to attr_val in the namespace dictionary
# via the name f:
def f(obj):
    print("attr = ", obj.attr)


Foo = type("Foo", (), {"attr": 100, "attr_val": f})

x = Foo()
print(x.attr)
print(x.attr_val())


class Foo:
    attr = 100

    attr_val = f


x = Foo()
print(x.attr)
print(x.attr_val())
