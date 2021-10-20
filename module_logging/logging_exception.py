import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def raise_exception(n: int):
    return 100 / n


if __name__ == '__main__':
    logging.info('hello %s', 'world', exc_info=RuntimeError('hello exception'))

    try:
        raise_exception(0)
    except Exception as e:
        logging.info('hello exception', exc_info=e)
