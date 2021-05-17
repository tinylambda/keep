def recv(maxsize, *, block):
    pass


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


if __name__ == '__main__':
    recv(1024, block=True)

    try:
        recv(1024, True)
    except TypeError:
        print('go type error')

    print(minimum(1, 5, 2, -5, 10))
    print(minimum(1, 5, 2, -5, 10, clip=0))

