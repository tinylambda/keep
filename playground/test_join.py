import itertools

# join two sorted (asc) list, simulate join two streams in map reduce process

a = [1, 2, 3, 4, 5, 8]
b = [3, 4, 6, 8, 8, 9, 10]

pointer = None
xi = yi = 0
a_end = b_end = False

while True:
    try:
        if not a_end:
            x = a[xi]
    except IndexError:
        a_end = True

    try:
        if not b_end:
            y = b[yi]
    except IndexError:
        b_end = True

    if all([a_end, b_end]):
        print('done')
        break

    if x == y:
        print('got pair', (x, y))
        xi += 1
        yi += 1
    else:
        if x < y:
            xi += 1
        else:
            yi += 1

    if a_end:
        yi += 1
    if b_end:
        xi += 1







