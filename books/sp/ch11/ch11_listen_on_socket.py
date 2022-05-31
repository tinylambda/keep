import select
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
# a server socket is created and set to non-blocking, meaning that any read or write operation attempted
# on that socket won't block the program. If the program tries to read from the socket when there is no data
# ready to be read, the socket recv() method will raise an OSError indicating that the socket is not ready.
# if we didn't call setblocking(False), the socket would stay in blocking mode rather than raise an error,
# which is not what we want here. The sockt is then bound to a port and listens with a maximum backlog of eight
# connections.
server.bind(("localhost", 10000))
server.listen(8)

while True:
    inputs, outputs, excepts = select.select([server], [], [server])
    if server in inputs:
        print("process new connection")
        connection, client_address = server.accept()
        connection.send(b"hello!\n")
        connection.close()
