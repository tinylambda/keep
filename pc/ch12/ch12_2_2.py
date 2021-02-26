import time

from threading import Thread, Event


def countdown(n, start_event):
    print('countdown starting')
    start_event.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)


if __name__ == '__main__':
    start_event = Event()
    print('launching countdown')
    t = Thread(target=countdown, args=(10, start_event))
    t.start()

    start_event.wait()
    print('countdown is running')
    t.join()
    print('done')

