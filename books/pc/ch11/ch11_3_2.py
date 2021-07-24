import time
from socketserver import DatagramRequestHandler, UDPServer, ThreadingUDPServer, ForkingUDPServer


class TimeHandler(DatagramRequestHandler):
    def handle(self) -> None:
        print('got connection from', self.client_address)
        resp = time.ctime()
        self.wfile.write(resp.encode('ascii'))


if __name__ == '__main__':
    # serv = UDPServer(('', 20000), TimeHandler)
    # serv = ThreadingUDPServer(('', 20000), TimeHandler)
    serv = ForkingUDPServer(('', 20000), TimeHandler)
    serv.serve_forever()


'''
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'', ('localhost', 20000))
s.recvfrom(8192)
'''
