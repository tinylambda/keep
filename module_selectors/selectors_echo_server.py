import selectors
import socket


mysel = selectors.DefaultSelector()
keep_running = True


def read(connection, mask):
    """Callback for read events"""
    global keep_running

    client_address = connection.getpeername()
    print("Read({})".format(client_address))
    data = connection.recv(1024)
    if data:
        # A readable client socket has data
        connection.sendall(data)
    else:
        # Interpret empty result as closed connection
        print("Closing")
        mysel.unregister(connection)
        connection.close()
        # Tell the main loop to stop
        keep_running = False


def accept(sock, mask):
    """Callback for new connections"""
    new_connection, addr = sock.accept()
    print("Accept({})".format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)


if __name__ == "__main__":
    server_address = ("localhost", 10000)
    print("Starting up on {} port {}".format(*server_address))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    server.bind(server_address)
    server.listen(5)
    mysel.register(server, selectors.EVENT_READ, accept)

    while keep_running:
        print("Waiting for I/O")
        for key, mask in mysel.select(timeout=1):
            callback = key.data
            callback(key.fileobj, mask)

    print("Shutting down")
    mysel.close()
