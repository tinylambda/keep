import logging
import sys
import time
import weakref

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(cache_hash=True, frozen=True)
class CacheHash:
    x = attr.ib()
    y = attr.ib()


@attr.s(cache_hash=False, frozen=True)
class NoCacheHash:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    cache_hash = CacheHash(100, 200)
    no_cache_hash = NoCacheHash(100, 200)

    N = 10000000
    start = time.time()
    for _ in range(N):
        hash(cache_hash)
    logging.info('cache hash cost %s s', time.time() - start)  # about 2.724s

    start = time.time()
    for _ in range(N):
        hash(no_cache_hash)
    logging.info('cache hash cost %s s', time.time() - start)  # about 3.375s
