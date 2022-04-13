import logging
import socketserver


logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )


class EchoRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)

    def setup(self) -> None:
        self.logger.debug('setup')
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug('handle')

        # Echo the back to the client
        data = self.request.recv(1024)
        self.logger.debug('recv() -> "%s"', data)
        self.request.send(data)

    def finish(self) -> None:
        self.logger.debug('finish')
        return socketserver.BaseRequestHandler.finish(self)


class EchoServer(socketserver.TCPServer):
    def __init__(self, server_address, handler_class=EchoRequestHandler):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug('__init__')
        socketserver.TCPServer.__init__(self, server_address, handler_class)

    def server_activate(self) -> None:
        self.logger.debug('server_activate')
        socketserver.TCPServer.server_activate(self)

    def verify_request(self, request, client_address) -> bool:
        self.logger.debug('verify_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address) -> None:
        self.logger.debug('process_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.process_request(self, request, client_address)

    def server_close(self) -> None:
        self.logger.debug('server_close')
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request, client_address) -> None:
        self.logger.debug('finish_request(%s, %s)', request, client_address)
        return socketserver.TCPServer.finish_request(self, request, client_address)

    def close_request(self, request) -> None:
        self.logger.debug('close_request(%s)', request)
        return socketserver.TCPServer.close_request(self, request)

    def shutdown(self) -> None:
        self.logger.debug('shutdown()')
        return socketserver.TCPServer.shutdown(self)


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()

    logger = logging.getLogger('Client')
    logger.info('Server on %s:%s', ip, port)

    logger.debug('Connecting to server')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('Connecting to server')
    s.connect((ip, port))

    message = 'Hello world'.encode()
    logger.debug('Sending data: %s', message)
    len_sent = s.send(message)

    logger.debug('Waiting for response')
    response = s.recv(len_sent)
    logger.debug('Response from server: %r', response)

    server.shutdown()
    logger.debug('Closing socket')
    s.close()
    logger.debug('done')
    server.socket.close()
