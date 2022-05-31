import socket
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self) -> None:
        print("got connection from", self.client_address)
        for line in self.rfile:
            print(line, type(line))
            self.wfile.write(line)


if __name__ == "__main__":
    serv = TCPServer(("", 20000), EchoHandler, bind_and_activate=False)
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    serv.server_bind()
    serv.server_activate()
    serv.serve_forever()
