import array
import pprint


a = array.array('i', range(3))  # i represents signed int
print('Initial: ', a)

a.extend(range(3))
print('Extended: ', a)

print('Slice: ', a[2:5])

print('Iterator: ')
print(list(enumerate(a)))

a.append(10)
print('Appended: ', a)

