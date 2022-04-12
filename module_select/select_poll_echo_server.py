import select
import socket
import sys
import queue


"""
The poll() function provides similar features to select(), but the underlying implementation is more efficient. 
The trade-off is that poll() is not supported under Windows, so programs using poll() are less portable.

The timeout value passed to poll() is represented in milliseconds, instead of seconds, 
so in order to pause for a full second the timeout must be set to 1000.
"""

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Keep up with the queues of outgoing messages
message_queues = {}

# Do not block forever (milliseconds)
TIMEOUT = 1000

# Commonly used flag sets
READ_ONLY = (
    select.POLLIN |
    select.POLLPRI |
    select.POLLHUP |
    select.POLLERR
)
READ_WRITE = READ_ONLY | select.POLLOUT


# Set up the poller
poller = select.poll()
poller.register(server, READ_ONLY)

# Map file descriptors to socket objects
fd_to_socket = {
    server.fileno(): server,
}

while True:
    # Wait for at least one of the sockets to be ready for processing
    print('Waiting for the next event', file=sys.stderr)
    events = poller.poll(TIMEOUT)
    for fd, flag in events:
        # Retrieve the actual socket from its file descriptor
        s = fd_to_socket[fd]

        # Handling inputs
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                # A readable socket is ready to accept a connection
                connection, client_address = s.accept()
                print('Connection', client_address, file=sys.stderr)
                connection.setblocking(False)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                # Give the connection a queue for data to send
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    # A readable client socket has data
                    print('Received {!r} from {}'.format(data, s.getpeername()), file=sys.stderr)
                    message_queues[s].put(data)
                    # Add output channel for response
                    poller.modify(s, READ_WRITE)
                else:
                    # Interpret empty result as closed connection
                    print('Closing', client_address, file=sys.stderr)
                    # Stop listening for input on the connection
                    poller.unregister(s)
                    s.close()

                    # Remove message queue
                    del message_queues[s]
        elif flag & select.POLLHUP:
            # Client hung up
            print('Closing', client_address, '(HUP)', file=sys.stderr)
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()
        elif flag & select.POLLOUT:
            # Socket is ready to send data if there is any to send.
            try:
                next_msg = message_queues[s].get_nowait()
            except queue.Empty:
                # No messages waiting so stop checking
                print(s.getpeername(), 'queue empty', file=sys.stderr)
                poller.modify(s, READ_ONLY)
            else:
                print('Sending {!r} to {}'.format(next_msg, s.getpeername()), file=sys.stderr)
                s.send(next_msg)
        elif flag & select.POLLERR:
            print('Exception on', s.getpeername(), file=sys.stderr)
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()

            # Remove message queue
            del message_queues[s]
