import threading
import socketserver


class ThreadedEchoRequestHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = b'%s: %s' % (cur_thread.name.encode(), data)
        self.request.send(response)


if __name__ == '__main__':
    import socket

    address = ('localhost', 0)
    server = socketserver.ThreadingTCPServer(address, ThreadedEchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    print('Server loop running in thread: ', t.getName())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    message = 'Hello world'.encode()
    print('Sending {!r}'.format(message))
    len_sent = s.send(message)

    response = s.recv(len_sent)
    print('Received: {!r}'.format(response))

    server.shutdown()
    s.close()
    server.socket.close()
