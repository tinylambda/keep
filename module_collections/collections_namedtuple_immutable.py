import collections


Person = collections.namedtuple('Person', 'name age')

pat = Person(name='Pat', age=12)
print('\nRepresentation: ', pat)

pat.age = 21

# Just like a regular tuple, a namedtuple is immutable. This restriction allows tuple instances to have a
# consistent hash value, which makes it possible to use them as keys in dictionaries and to be included in sets.

