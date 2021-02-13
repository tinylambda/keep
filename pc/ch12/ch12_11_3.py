from contextlib import contextmanager
from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


class Task:
    def __init__(self, name):
        self.name = name

    def send(self, msg):
        print(f'{self.name} is processing message {msg}')


if __name__ == '__main__':
    exc = get_exchange('name')
    task_a = Task('a')
    task_b = Task('b')
    with exc.subscribe(task_a, task_b):
        exc.send('msg1')
        exc.send('msg2')

