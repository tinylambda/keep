from socket import *


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(b'', ('localhost', 14000))
    print(s.recvfrom(128))

    s.sendto(b'hello', ('localhost', 15000))
    print(s.recvfrom(128))
