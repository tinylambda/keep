from cityhash import CityHash32, CityHash64, CityHash128, CityHash64WithSeed, CityHash128WithSeed
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    s = 'abc'
    logging.info('%s', CityHash32(s))
    logging.info('%s', CityHash64(s))
    logging.info('%s', CityHash128(s))

    logging.info('%s', CityHash64WithSeed(s, seed=100))
    logging.info('%s', CityHash128WithSeed(s, seed=100))
