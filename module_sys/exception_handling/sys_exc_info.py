import sys
import threading
import time


def do_something_with_exception():
    #  If the traceback is needed (for example, so it can be logged),
    #  explicitly delete the local variable (using del) to avoid cycles.
    exc_type, exc_value = sys.exc_info()[:2]
    print(
        'Handling {} exception with message "{}" in {}'.format(
            exc_type.__name__, exc_value, threading.current_thread().name
        )
    )


def cause_exception(delay):
    time.sleep(delay)
    raise RuntimeError("This is the error messages")


def thread_target(delay):
    try:
        cause_exception(delay)
    except RuntimeError:
        do_something_with_exception()


threads = [
    threading.Thread(target=thread_target, args=(0.3,)),
    threading.Thread(target=thread_target, args=(0.1,)),
]

for t in threads:
    t.start()

for t in threads:
    t.join()
