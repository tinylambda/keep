from coroutine import coroutine
from queue import Queue
from threading import Thread
from cofollow import follow, printer


@coroutine
def threaded(target):
    messages = Queue()

    def run_target():
        while True:
            item = messages.get()
            if item is GeneratorExit:
                target.close()
                return
            else:
                target.send(item)

    Thread(target=run_target).start()
    try:
        while True:
            item = yield
            messages.put(item)
    except GeneratorExit:
        messages.put(GeneratorExit)


if __name__ == "__main__":
    coro = threaded(printer())

    for i in range(10):
        coro.send(i)

    coro.close()  # raise GeneratorExit inside generator
