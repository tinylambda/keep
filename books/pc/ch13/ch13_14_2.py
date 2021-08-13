import signal
import resource
import os


def time_exceeded(signo, frame):
    print('time is up')
    raise SystemExit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


if __name__ == '__main__':
    limit_memory(100)
    l = []
    while True:
        l.append('s')
        print(len(l))

    set_max_runtime(10)
    while True:
        pass
