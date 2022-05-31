def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print(f"[{self.sequence}] Got: {result}")


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f"[{sequence}] Got: {result}")

    return handler


def make_handler_coro():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print(f"[{sequence}] Got: {result}")


class SequenceNo:
    def __init__(self):
        self.sequence = 0


def handler_extra_info(result, seq):
    seq.sequence += 1
    print(f"[{seq.sequence}] Got: {result}")


if __name__ == "__main__":

    def print_result(result):
        print("Got: ", result)

    def add(x, y):
        return x + y

    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, ("hello", "world"), callback=print_result)

    r = ResultHandler()
    apply_async(add, (2, 3), callback=r.handler)
    apply_async(add, ("hello", "world"), callback=r.handler)

    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ("hello", "world"), callback=handler)

    handler_coro = make_handler_coro()
    next(handler_coro)
    apply_async(add, (2, 3), callback=handler_coro.send)
    apply_async(add, ("hello", "world"), callback=handler_coro.send)

    seq = SequenceNo()
    from functools import partial

    apply_async(add, (2, 3), callback=partial(handler_extra_info, seq=seq))
    apply_async(add, ("hello", "world"), callback=partial(handler_extra_info, seq=seq))
