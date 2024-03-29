import sys
import socketserver


class Echo(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        # Get some bytes and echo them back to the client
        data = self.request.recv(1024)
        self.request.send(data)


if __name__ == "__main__":
    import codecs
    import socket
    import threading

    address = ("localhost", 0)  # let the kernel assign a port
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address  # what port was assigned ?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # don't hang on exit
    t.start()

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Send the data
    # WRONG: Not encoded first!
    text = "中国"
    len_sent = s.send(text)

    # Receive a response
    response = s.recv(len_sent)
    print(repr(response))

    # Clean up
    s.close()
    server.socket.close()
