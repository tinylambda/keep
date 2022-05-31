import threading


class SharedCounter:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        with self._value_lock:
            self._value -= delta


if __name__ == "__main__":
    from multiprocessing.dummy import Pool

    pool = Pool(8)
    sc = SharedCounter()
    pool.map(lambda x: sc.incr(), range(1000))
    print(getattr(sc, "_value"))

    print("-" * 64)

    sc = SharedCounter()
    for _ in range(1000):
        sc.incr()
    print(getattr(sc, "_value"))

    from concurrent.futures import ThreadPoolExecutor

    executor = ThreadPoolExecutor(max_workers=8)
    sc = SharedCounter()
    executor.map(lambda x: sc.incr(), range(1000))
    executor.shutdown(wait=True)
    print(getattr(sc, "_value"))
