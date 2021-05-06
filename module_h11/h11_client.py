import socket
import ssl

import h11


conn = h11.Connection(our_role=h11.CLIENT)

ssl.create_default_context = ssl._create_unverified_context
ctx = ssl.create_default_context()
sock = ctx.wrap_socket(socket.create_connection(('www.baidu.com', 443)), server_hostname='www.baidu.com')


def send(event):
    print('sending event:', event)
    # pass the event through h11's state machine and encoding machinery
    data = conn.send(event)
    sock.sendall(data)


send(
    h11.Request(
        method='GET',
        target='/',
        headers=[('Host', 'www.baidu.com'), ('Connection', 'close')],
    )
)
send(h11.EndOfMessage())


def next_event():
    while True:
        event = conn.next_event()
        if event is h11.NEED_DATA:
            data = sock.recv(2048)
            conn.receive_data(data)
            continue
        print('RETURN....')
        return event


while True:
    event = next_event()
    print('received event:')
    print(event)
    if type(event) is h11.EndOfMessage:
        break

sock.close()

