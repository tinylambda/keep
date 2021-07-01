import sys
import typing

CHUNK_SIZE = 8192


def reader(s, process_data: typing.Callable):
    for chunk in iter(lambda : s.recv(CHUNK_SIZE), b''):
        process_data(chunk)


if __name__ == '__main__':
    f = open('/etc/passwd')
    for chunk in iter(lambda : f.read(10), ''):
        n = sys.stdout.write(chunk)

