from concurrent import futures
from multiprocessing import Event


def task(n):
    print(n)


if __name__ == '__main__':
    with futures.ProcessPoolExecutor(max_workers=2) as ex:
        print('main: starting')
        ex.submit(task, 1)
        ex.submit(task, 2)
        ex.submit(task, 3)
        ex.submit(task, 4)

    print('main: done')
