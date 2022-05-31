import socket


def get_available_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("", 0))
        return s.getsockname()[1]
    finally:
        s.close()


if __name__ == "__main__":
    ports = []
    for _ in range(500):
        port = get_available_port()
        if port in ports:
            print("Duplicated port !")
            continue
        ports.append(port)
