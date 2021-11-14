import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def find_callatz(n: int):
    tries = 0
    value_seq = []

    while True:
        tries += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2

        value_seq.append(n)
        if n == 1:
            break
    return ','.join(map(str, value_seq))


if __name__ == '__main__':
    for num in range(1, 100):
        logging.info(find_callatz(num))
