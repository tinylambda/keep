from clickhouse_cityhash import cityhash

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    s = 'abc'
    logging.info('%s', cityhash.CityHash64(s))
    logging.info('%s', cityhash.CityHash128(s))

    logging.info('%s', cityhash.CityHash64WithSeed(s, seed=100))
    logging.info('%s', cityhash.CityHash128WithSeed(s, seed=100))
