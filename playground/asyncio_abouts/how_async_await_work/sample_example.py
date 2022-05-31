import datetime
import heapq
import types
import time


class Task:
    def __init__(self, wait_until, coro):
        self.coro = coro
        self.waiting_until = wait_until

    def __eq__(self, other):
        return self.waiting_until == other.waiting_until

    def __lt__(self, other):
        return self.waiting_until < other.waiting_until


class SleepingLoop:
    def __init__(self, *coros):
        self._new = coros
        self._waiting = []

    def run_until_complete(self):
        # start all the coroutines
        for coro in self._new:
            wait_for = coro.send(None)
            heapq.heappush(self._waiting, Task(wait_for, coro))

        # keep running until there is no more work to do.
        while self._waiting:
            now = datetime.datetime.now()
            # get the coroutine with the soonest resumption time.
            task = heapq.heappop(self._waiting)
            if now < task.waiting_until:
                # we are ahead of schedule; wait until it's time to resume
                delta = task.waiting_until - now
                time.sleep(delta.total_seconds())
                now = datetime.datetime.now()

            try:
                # it is time to resume the coroutine
                wait_until = task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except StopIteration:
                # the coroutine is done
                pass


@types.coroutine
def sleep(seconds):
    now = datetime.datetime.now()
    wait_until = now + datetime.timedelta(seconds=seconds)
    # make all coroutines on the call stack pause; the need to use yield
    # necessitates this be generator-based and not a async-based coroutine.
    actual = yield wait_until
    # resume the execution stack, sending back how long we actually waited.
    return actual - now


async def countdown(label, length, *, delay=0):
    print(label, "waiting", delay, "seconds before starting countdown")
    delta = await sleep(delay)
    print(label, "starting after waiting", delta)
    while length:
        print(label, "T-minus", length)
        waited = await sleep(1)
        length -= 1
    print(label, "lift-off!")


def main():
    loop = SleepingLoop(
        countdown("A", 5), countdown("B", 3), countdown("C", 4, delay=1)
    )
    start = datetime.datetime.now()
    loop.run_until_complete()
    print("total elapsed time is", datetime.datetime.now() - start)


if __name__ == "__main__":
    main()
