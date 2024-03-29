import socket


def get_constants(prefix):
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


families = get_constants("AF_")
types = get_constants("SOCK_")
protocols = get_constants("IPPROTO_")

responses = socket.getaddrinfo(
    host="www.python.org",
    port="http",
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
    flags=socket.AI_CANONNAME,
)

for response in responses:
    family, socktype, proto, canonname, sockaddr = response
    print(f"family {families[family]}")
    print(f"type {types[socktype]}")
    print(f"protocol {protocols[proto]}")
    print(f"canonical name: {canonname}")
    print(f"socket address: {sockaddr}")
    print()
