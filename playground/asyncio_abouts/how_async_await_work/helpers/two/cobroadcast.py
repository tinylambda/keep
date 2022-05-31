from coroutine import coroutine

from copipe import grep, printer, follow


@coroutine
def broadcast(targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)


if __name__ == "__main__":
    with open("/tmp/test.log") as f:
        follow(
            f,
            broadcast(
                [
                    grep("python", printer()),
                    grep("ply", printer()),
                    grep("swig", printer()),
                ]
            ),
        )
