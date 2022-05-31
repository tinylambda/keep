from socketserver import StreamRequestHandler, TCPServer
from functools import partial


class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self) -> None:
        for line in self.rfile:
            self.wfile.write(self.ack + line)


if __name__ == "__main__":
    serv = TCPServer(("", 15000), partial(EchoHandler, ack=b"Got: "))
    serv.serve_forever()
