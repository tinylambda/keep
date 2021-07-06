import logging

if __name__ == '__main__':
    a = logging.getLogger('foo')
    b = logging.getLogger('bar')
    print(a is b)
    c = logging.getLogger('foo')
    print(a is c)

