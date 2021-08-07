import threading
import time

from books.pc.ch12.ch12_5_2 import acquire


def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(threading.current_thread(), 'eating')


N_TICKS = 5
chopsticks = [threading.Lock() for _ in range(N_TICKS)]
for n in range(N_TICKS):
    t = threading.Thread(target=philosopher, args=(chopsticks[n], chopsticks[(n+1) % N_TICKS]))
    t.daemon = True
    t.start()

time.sleep(5)
