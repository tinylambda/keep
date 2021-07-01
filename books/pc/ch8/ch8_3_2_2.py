from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()


if __name__ == '__main__':
    from functools import partial
    conn = LazyConnection(('www.python.org', 80))
    with conn as s1:
        with conn as s2:
            print(s2, conn.connections)
        print(s1, conn.connections)
    print('done', conn.connections)

