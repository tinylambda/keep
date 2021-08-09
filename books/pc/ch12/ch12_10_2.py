from queue import Queue
from threading import Thread, Event


# sentinel used for shutdown
class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()
        self._terminated = None

    def send(self, msg):
        """send a message to the actor"""
        self._mailbox.put(msg)

    def recv(self):
        """receive an incomming message"""
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        """close the actor, thus shutting it down"""
        self.send(ActorExit)

    def start(self):
        """start concurrent execution"""
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        """run method to be implemented by the user"""
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('got: ', msg)


if __name__ == '__main__':
    p = PrintActor()
    p.start()
    p.send('hello')
    p.send('world')
    p.close()
    p.join()
