from socket import *
import numpy


def recv_into(arr, source):
    view = memoryview(arr).cast("B")
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]


if __name__ == "__main__":
    c = socket(AF_INET, SOCK_STREAM)
    c.connect(("localhost", 25000))

    a = numpy.zeros(shape=5000000, dtype=float)
    print(a[:10])
    recv_into(a, c)
    print(a[:10])
