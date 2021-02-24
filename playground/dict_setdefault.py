import collections


dd = collections.defaultdict(list)
dd['x']
dd['y']
print(dd)

d = {}
d.setdefault('a', []).append('x')
print(d)

d.setdefault('a', [])
print(d)

d.setdefault('b', [])
print(d)

print(d['c'])  # key error

