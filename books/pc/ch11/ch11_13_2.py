import numpy


def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]


if __name__ == '__main__':
    from socket import *
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 25000))
    s.listen(1)
    c, a = s.accept()

    arr = numpy.arange(0.0, 5000000.0)
    send_from(arr, c)
