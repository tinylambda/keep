import socket
import sys


messages = [
    "This is the message. ",
    "It will be sent ",
    "in parts.",
]
server_address = ("localhost", 10000)


socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# Connect the socket to the port where the server is listening on
print("Connecting to {} port {}".format(*server_address))
for s in socks:
    s.connect(server_address)

for message in messages:
    outgoing_data = message.encode()
    # Send message on both sockets
    for s in socks:
        print(
            "{}: sending {!r}".format(s.getpeername(), outgoing_data), file=sys.stderr
        )
        s.send(outgoing_data)

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print("{}: received {!r}".format(s.getsockname(), data), file=sys.stderr)
        if not data:
            print("Closing socket", s.getsockname(), file=sys.stderr)
            s.close()
