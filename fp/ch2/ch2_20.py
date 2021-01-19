from array import array
from random import random


if __name__ == '__main__':
    # floats = array('d', (random() for i in range(10**7)))
    # print(floats[-1])
    #
    # fp = open('floats.bin', 'wb')
    # floats.tofile(fp)
    # fp.close()

    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()
    print(floats2[0])
    print(floats2[-1])
    print(floats2.index(0.15821509313622806))
    floats2.reverse()
    print(floats2[-1])

