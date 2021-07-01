import threading


def worker(n, sema):
    sema.acquire()
    print('Working', n)


if __name__ == '__main__':
    sema = threading.Semaphore(0)
    nworkers = 10
    threads = []

    for n in range(nworkers):
        t = threading.Thread(target=worker, args=(n, sema))
        threads.append(t)

    for t in threads:
        t.start()

    for _ in range(nworkers):
        sema.release()

    print('done')

