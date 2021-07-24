from socketserver import StreamRequestHandler, ThreadingTCPServer, ForkingTCPServer


class EchoHandler(StreamRequestHandler):
    # def setup(self) -> None:
    #     super().setup()
    #     print('setup')

    def handle(self) -> None:
        print('got connection from', self.client_address)
        for line in self.rfile:
            print(line, type(line))
            self.wfile.write(line)

    # def finish(self) -> None:
    #     super().finish()
    #     print('finish')


if __name__ == '__main__':
    # serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv = ForkingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
