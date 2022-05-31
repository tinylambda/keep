from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
import os
from socket import socket, AF_INET, SOCK_STREAM


def worker(server_address):
    serv = Client(server_address, authkey=b"peekaboo")
    serv.send(os.getpid())
    while True:
        try:
            fd = recv_handle(serv)
        except Exception as e:
            continue

        print("worker: got fd", fd)
        with socket(AF_INET, SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print("worker: recv {!r}".format(msg))
                client.send(msg)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("usage: worker.py server_address", file=sys.stderr)
        raise SystemExit(1)

    worker(sys.argv[1])
