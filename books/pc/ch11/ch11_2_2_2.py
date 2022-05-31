from socket import socket, AF_INET, SOCK_STREAM


if __name__ == "__main__":
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 20000))
    s.send(b"hello world\n")
    print(s.recv(8192))
    s.close()
