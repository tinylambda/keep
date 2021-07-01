import time

from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


if __name__ == '__main__':
    # t = Thread(target=countdown, args=(3, ))
    # t.start()

    # while t.is_alive():
    #     print('still running')
    #     time.sleep(1)

    # t.join()

    threads = []
    for _ in range(10):
        t = Thread(target=countdown, args=(2, ))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        print('joining')
        thread.join()

    print('done' * 10)

