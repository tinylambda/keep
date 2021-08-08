from socket import socket, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor


def echo_client(sock, client_addr):
    """handle a client connection"""
    print('got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('client closed connection')
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


if __name__ == '__main__':
    echo_server(('', 15000))
