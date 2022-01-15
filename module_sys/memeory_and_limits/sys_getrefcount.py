import sys


if __name__ == '__main__':
    one = []
    print('At start: ', sys.getrefcount(one))

    two = one
    print('Second reference: ', sys.getrefcount(one))

    del two
    print('After del: ', sys.getrefcount(one))
    