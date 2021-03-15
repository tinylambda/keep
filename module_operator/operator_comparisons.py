import operator

a = 1
b = 5.0

print('a =', a)
print('b =', b)

for func in (operator.lt, operator.le, operator.eq, operator.ge, operator.gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b)))

