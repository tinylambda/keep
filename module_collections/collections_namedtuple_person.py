import collections


Person = collections.namedtuple("Person", "name age")

bob = Person(name="Bob", age=30)
print("\nRepresentation: ", bob)

jane = Person(name="Jane", age=29)
print("\nField by name: ", jane.name)

print("\nFields by index: ")
for p in [bob, jane]:
    print("{} is {} years old".format(*p))

#  it is possible to access the fields of the namedtuple by name using dotted notation (obj.attr) as well as by
#  using the positional indexes of standard tuples.
