from socket import socket, AF_INET, SOCK_STREAM
import ssl
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


s = socket(AF_INET, SOCK_STREAM)
s_ssl = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs=CERTFILE)
s_ssl.connect(("localhost", 20000))
s_ssl.send(b"hello world")
print(s_ssl.recv(8192))
