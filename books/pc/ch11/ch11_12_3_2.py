from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM

if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_DGRAM)
    for x in range(40):
        sock.sendto(str(x).encode('ascii'), ('localhost', 16000))
        resp = sock.recvfrom(8192)
        print(resp)
