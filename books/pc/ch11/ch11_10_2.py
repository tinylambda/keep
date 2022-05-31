from socket import socket, AF_INET, SOCK_STREAM
import ssl
import pathlib
import os


fp = os.path.abspath(__file__)
dp = os.path.dirname(fp)
p = os.path.abspath(os.path.join(dp, "../../../"))

KEYFILE = os.path.join(p, "pymotw.key")
CERTFILE = os.path.join(p, "pymotw.crt")
PEMFILE = os.path.join(p, "pymotw.pem")
print(KEYFILE)
print(CERTFILE)
print(PEMFILE)


def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b"":
            break
        s.send(data)
    s.close()
    print("connection closed")


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)

    while True:
        try:
            c, a = s_ssl.accept()
            print("got connection", c, a)
            echo_client(c)
        except Exception as e:
            print("{}: {}".format(e.__class__.__name__, e))


if __name__ == "__main__":
    echo_server(("", 20000))


"""
from socket import socket, AF_INET, SOCK_STREAM
import ssl
s = socket(AF_INET, SOCK_STREAM)
s_ssl = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/home/felix/PycharmProjects/keep/pymotw.crt')
s_ssl.connect(('localhost', 20000))
s_ssl.send(b'hello world')
print(s_ssl.recv(8192)
"""
