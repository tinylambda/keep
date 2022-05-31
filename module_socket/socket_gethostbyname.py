import socket


HOSTS = [
    "apu",
    "pymotw.com",
    "www.python.org",
    "nosuchname",
]

if __name__ == "__main__":
    for host in HOSTS:
        try:
            print(f"{host}: {socket.gethostbyname(host)}")
        except socket.error as msg:
            print(f"{host}: {msg}")
