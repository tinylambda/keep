def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, .5):
    print(n)

print(
    list(frange(0, 1, .125))
)

