import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    FILTER = b'30085'
    FILTER2 = b'30086'
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://localhost:5556')
    subscriber.setsockopt(zmq.SUBSCRIBE, FILTER)
    subscriber.setsockopt(zmq.SUBSCRIBE, FILTER2)

    total_temperature = 0
    N = 100

    for _ in range(N):
        topic, message = subscriber.recv_multipart()
        logging.info('received %s', message.decode('utf-8'))
        zipcode, temperature, relhumidity = map(int, message.split())
        total_temperature += temperature

    average_temperature = int(total_temperature / N)
    logging.info(f'avg temperature for {FILTER.decode()} is {average_temperature}')

