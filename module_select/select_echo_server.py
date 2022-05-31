import select
import socket
import sys
import queue


# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# Bind the socket to the port
server_address = ("localhost", 10000)
print("Starting up on {} port {}".format(*server_address), file=sys.stderr)
server.bind(server_address)
server.listen(5)

# Sockets from which we expect to read
inputs = [server]

# Sockets to which we expect to write
outputs = []

# Output message queues
message_queues = {}


while inputs:
    print("Waiting for the next event", file=sys.stderr)
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            # A "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print("Connection from", client_address, file=sys.stderr)
            connection.setblocking(False)
            inputs.append(connection)

            # Give the connection a queue for data we want to send
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print(
                    "Received {!r} from {}".format(data, s.getpeername()),
                    file=sys.stderr,
                )
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # interpret empty result as closed connection
                print("Closing", client_address, file=sys.stderr)
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)

                # Remove message queue
                del message_queues[s]
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # No messages waiting so stop checking for writability
            print(" ", s.getpeername(), "queue empty", file=sys.stderr)
            outputs.remove(s)
        else:
            print("Sending {!r} to {}".format(next_msg, s.getpeername()))
            s.send(next_msg)

    for s in exceptional:
        print("Exception condition on", s.getpeername(), file=sys.stderr)
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]
