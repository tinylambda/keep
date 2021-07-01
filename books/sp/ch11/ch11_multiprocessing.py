import multiprocessing
import random


def compute(n):
    return sum([random.randint(1, 100) for i in range(1000000)])


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=8)
    print('results: %s' % pool.map(compute, range(8)))

