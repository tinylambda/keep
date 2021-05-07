from help_send import writer_wrapper
from help_send import writer_wrapper2


class SpamException(Exception):
    pass


def writer():
    while True:
        try:
            w = (yield)
        except SpamException:
            print('***')
        else:
            print('>> ', w)


def writer_wrapper3(coro):
    coro.send(None)
    while True:
        try:
            try:
                x = (yield)
            except Exception as e:
                coro.throw(e)
            else:
                coro.send(x)
        except StopIteration:
            pass


if __name__ == '__main__':
    w = writer()
    # wrap = writer_wrapper(w)  # wont work
    # wrap = writer_wrapper3(w)  # work
    wrap = writer_wrapper2(w)  # work
    wrap.send(None)
    for i in [0, 1, 2, 'spam', 4]:
        if i == 'spam':
            wrap.throw(SpamException)
        else:
            wrap.send(i)




