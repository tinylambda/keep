import socket


if __name__ == "__main__":
    for host in ["apu", "pymotw.com"]:
        print(f"{host:>10} : {socket.getfqdn(host)}")
