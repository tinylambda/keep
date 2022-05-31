def times_two(x):
    return 2 * x


def multiple(x, y):
    return x, y, x * y


print("Doubles: ")
for i in map(times_two, range(5)):
    print(i)


print("Multiples: ")
r1 = range(5)
r2 = range(5, 10)
for i in map(multiple, r1, r2):
    print("{:d} * {:d} = {:d}".format(*i))


print("Stopping: ")
r1 = range(5)
r2 = range(2)
for i in map(multiple, r1, r2):
    print(i)
