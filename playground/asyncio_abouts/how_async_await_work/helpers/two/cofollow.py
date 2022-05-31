import time
from coroutine import coroutine


def follow(thefile, target):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


if __name__ == "__main__":
    with open("/tmp/test.log") as f:
        follow(f, printer())
