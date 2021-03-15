import operator

a = -1
b = 5.0
c = [1, 2, 3]
d = ['a', 'b', 'c']

print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

a = operator.iadd(a, b)
print('a = iadd(a, b) =>', a)
print()

operator.iconcat(c, d)
print('c = iconcat(c, d) =>', c)

