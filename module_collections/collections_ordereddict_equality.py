import collections


print('dict: ', end=' ')
d1 = dict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = dict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

print('OrderedDict: ', end=' ')
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = collections.OrderedDict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

# since the two ordered dictionaries are created from values in a different order, they are considered to be different
print(d1 == d2)

