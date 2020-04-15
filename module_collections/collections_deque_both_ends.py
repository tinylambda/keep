import collections
import threading
import time


candle = collections.deque(range(5))


def burn(direction, next_source):
    while True:
        try:
            next = next_source()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
    print('{:>8} done'.format(direction))


left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

