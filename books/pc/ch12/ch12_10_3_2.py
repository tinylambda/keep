from threading import Event

from books.pc.ch12.ch12_10_2 import Actor


class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            received = self.recv()
            func, args, kwargs, r = received
            r.set_result(func(*args, **kwargs))


if __name__ == '__main__':
    worker = Worker()
    worker.start()
    result = worker.submit(pow, 2, 3)
    worker.close()
    worker.join()
    print(result.result())
