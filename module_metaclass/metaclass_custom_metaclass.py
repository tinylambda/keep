class MyMeta(type):
    pass


class MyClass(metaclass=MyMeta):
    pass


class MySubClass(MyClass):
    pass


class Foo:
    pass


f = Foo()
# The expression Foo() creates a new instance of class Foo. When the interpreter encounters Foo(), the following occurs:
# * The __call__() method of Foo's parent class is called. Since Foo is a standard new-style class,
# Its parent class is the type metaclass, so type's ___call__() method is invoked.
# * The __call__() method in turn invokes the following:
# - __new__()
# - __init__()
# If Foo does not define __new__() and __init__(), default methods are inherited from Foo's ancestry.
# But if Foo does define these methods, they override those from the ancestry,
# which allows for customized behavior when instantiating Foo.
# In the following, a custom method called new() is defined and assigned as the __new__() method for Foo:


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new

f = Foo()
print(f.attr)

g = Foo()
print(f.attr)
# This modifies the instantiation behavior of class Foo: each time an instance of Foo is created,
# by default it is initialized with an attribute called attr, which has a value of 100.
# (Code like this would more usually appear in the __init__() method and not typically in __new__().
# This example is contrived for demonstration purpose)
# Now, as has already been reiterated, classes are objects too. Suppose you wanted to similarly customize instantiation
# behavior when creating class like Foo. If you were to follow the pattern above, you'd again define a custom method and
# assign it as the __new__() method for the class of which Foo is an instance. Foo is an instance of the type metaclass,
# so the code looks like something like this:


def new(cls):
    x = type.__new__(cls)
    x.attr = 100
    return x


# type.__new__ = new  # Won't work
# As you can see, you cannot reassign the __new__() method of the type metaclass.
# Python doesn't allow it.

# This probably just as well. type is the metaclass from which all new-style classes are
# derived. You really shouldn't be mucking around with it anyway. But then what recourse is
# there, if you want to customize instantiation of a class?

# One possible solution is a custom metaclass. Essentially, instead of mucking around with the type metaclass
# you can define your own metaclass, which derived from type, and then you can muck around with that instead.

# The first step is to define a metaclass that derives from type, as follows:
class Meta(type):
    def __new__(mcs, name, bases, dct):
        x = super().__new__(mcs, name, bases, dct)
        x.attr = 100
        return x

# The definition header class Meta(type): specifies that Meta derives from type. Since type is a metaclass,
# that makes Meta a metaclass as well.
# Note that a custom __new__() method has been defined for Meta. It wasn't possible to do that to the type metaclass
# directly. the __new__() method does the following:
# - Delegates via super() to the __new__() method of the parent metaclass (type) to actually create a new class.
# - Assigns the custom attribute attr to the class, with a value of 100
# - Returns the newly created class.
# Now the other half of the voodoo: Define a new class Foo and specify that its metaclass is the custom metaclass meta,
# rather than the standard metaclass type. This is done using the metaclass keyword in the class definition as follows:


class Foo(metaclass=Meta):
    pass


print(Foo.attr)
# Voila! Foo has picked up the attr attribute automatically from the Meta metaclass. Of course,
# any other classes you define similarly will do likewise:


class Bar(metaclass=Meta):
    pass


class Qux(metaclass=Meta):
    pass


print(Bar.attr, Qux.attr)
# In the same way that a class functions as a template for the creation of objects, a metaclass
# functions as a template for creation of classes. Metaclasses are sometimes referred to as class factories.

# Compare the following two examples:
# Object factory:


class Foo:
    def __init__(self):
        self.attr = 100


x = Foo()
print(x.attr)

y = Foo()
print(y.attr)

z = Foo()
print(z.attr)

# Class factory:


class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100


class X(metaclass=Meta):
    pass


print(X.attr)


class Y(metaclass=Meta):
    pass


print(Y.attr)


class Z(metaclass=Meta):
    pass


print(Z.attr)

# Is this really necessary?
# As simple as the above class factory example is, it is the essence of how metaclasses work.
# they allow customization of class instantiation.

# Still, this is a lot of fuss just to bestow the custom attribute attr on each newly created class.
# Do you really need a metaclass just for that ?

# In Python, there are at least a couple other ways in which effectively the same thing can be accomplished:
# Simple inheritance:


class Base:
    attr = 100


class X(Base):
    pass


class Y(Base):
    pass


class Z(Base):
    pass


print(X.attr, Y.attr, Z.attr)


# Class decorator:
def decorator(cls):
    class NewClass(cls):
        attr = 100
    return NewClass


@decorator
class X:
    pass


@decorator
class Y:
    pass


@decorator
class Z:
    pass


print(X.attr, Y.attr, Z.attr)


# Conclusion
# As Tim Peters suggests, metaclass can easily veer into the realm of being a "solution in search of a problem",
# It isn't typically necessary to create custom metaclass. If the problem at hand can be solved in a simpler way,
# It probably should be. Still, it is beneficial to understand metaclasses so that you understand Python classes in
# general and can recognize when a metaclass really is the appropriate tool to use.

# if __name__ == '__main__':
#     print(type(MyMeta))
#     print(type(MyClass))
#     print(type(MySubClass))

