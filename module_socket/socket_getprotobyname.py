import socket


def get_constants(prefix):
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


protocols = get_constants('IPPROTO_')

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print(f'{name:>4} -> {proto_num:2d} (socket.{const_name:<12} = {getattr(socket, const_name):2d})')
