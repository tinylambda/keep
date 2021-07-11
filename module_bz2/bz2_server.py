import bz2
import logging
import socketserver
import binascii


BLOCK_SIZE = 32


class Bz2RequestHandler(socketserver.BaseRequestHandler):
    logger = logging.getLogger('Server')

    def handle(self) -> None:
        compressor = bz2.BZ2Compressor()

        # find out what file the client wants
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('client asked for: "%s"', filename)
        # send chunks of the file as they are compressed
        with open(filename, 'rb') as _input:
            while True:
                block = _input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug('SENDING %r', binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('BUFFERING')

        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('FLUSHING %r', binascii.hexlify(to_send))
            self.request.send(to_send)


if __name__ == '__main__':
    import socket
    import sys
    import threading

    from io import StringIO

    logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s')
    address = ('localhost', 0)  # let the kernel assign a port
    server = socketserver.TCPServer(address, Bz2RequestHandler)
    ip, port = server.server_address
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    logger = logging.getLogger('Client')
    logger.info('Contacting server on %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    requested_file = (sys.argv[0] if len(sys.argv) > 1 else 'lorem.txt')
    logger.debug('sending filename: "%s"', requested_file)
    len_sent = s.send(requested_file.encode('utf-8'))

    buffer = StringIO()
    decompressor = bz2.BZ2Decompressor()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ %r', binascii.hexlify(response))
        decompressed = decompressor.decompress(response)
        if decompressed:
            logger.debug('DECOMPRESSED %r', decompressed)
            buffer.write(decompressed.decode('utf-8'))
        else:
            logger.debug('BUFFERING')
    full_response = buffer.getvalue()
    lorem = open(requested_file, 'rt').read()
    logger.debug('response matches file contents: %s', full_response == lorem)

    server.shutdown()
    server.socket.close()
    s.close()



