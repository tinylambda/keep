from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self) -> None:
        print('got connection from', self.client_address)
        for line in self.rfile:
            print(line, type(line))
            self.wfile.write(line)


if __name__ == '__main__':
    TCPServer.allow_reuse_address = True
    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=True)
    serv.serve_forever()
