from socketserver import (
    StreamRequestHandler,
    ThreadingTCPServer,
    ForkingTCPServer,
    TCPServer,
)


class EchoHandler(StreamRequestHandler):
    def handle(self) -> None:
        print("got connection from", self.client_address)
        for line in self.rfile:
            print(line, type(line))
            self.wfile.write(line)


if __name__ == "__main__":
    from threading import Thread

    NWORKERS = 2
    serv = TCPServer(("", 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()
