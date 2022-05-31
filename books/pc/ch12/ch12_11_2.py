from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

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
        print(f"{self.name} is processing message {msg}")


if __name__ == "__main__":
    task_a = Task("a")
    task_b = Task("b")
    exc = get_exchange("exc")
    exc.attach(task_a)
    exc.attach(task_b)

    exc.send("msg1")
    exc.send("msg2")

    exc.detach(task_a)
    exc.detach(task_b)
