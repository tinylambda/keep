from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False

    def handle(self) -> None:
        print("got connection from", self.client_address)
        for line in self.rfile:
            self.wfile.write(line)


if __name__ == "__main__":
    TCPServer.allow_reuse_address = True
    serv = TCPServer(("", 20000), EchoHandler, bind_and_activate=True)
    serv.serve_forever()
