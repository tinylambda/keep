from books.fp.ch16.ch16_1 import simple_coroutine


if __name__ == '__main__':
    my_coro = simple_coroutine()
    my_coro.send(42)  # can't send non-None value to a just-started generator

