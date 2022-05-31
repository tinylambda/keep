import queue
import socket
import os
import select
import threading
import time


class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        # create a pair of connected sockets
        if os.name == "posix":
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # compatibility on non-POSIX systems
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("", 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, item):
        super().put(item)
        self._putsocket.send(b"x")

    def get(self):
        self._getsocket.recv(1)
        return super().get()


def consumer(queues):
    while True:
        can_read, _, _ = select.select(queues, [], [])
        for r in can_read:
            item = r.get()
            print("got", item)


if __name__ == "__main__":
    q1 = PollableQueue()
    q2 = PollableQueue()
    q3 = PollableQueue()
    t = threading.Thread(target=consumer, args=([q1, q2, q3],))
    t.daemon = True
    t.start()

    q1.put(1)
    q2.put(2)
    q3.put(3)

    time.sleep(2)
