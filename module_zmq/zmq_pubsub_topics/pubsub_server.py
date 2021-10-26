import logging
import random
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)

    publisher.bind('tcp://*:5556')
    publisher.bind('ipc://weather.ipc')

    while True:
        zipcode = random.randint(0, 100000)
        temperature = random.randint(0, 215) - 80
        relhumidity = random.randint(0, 50) + 10

        message = f'{zipcode} {temperature} {relhumidity}'
        publisher.send_multipart([f'{zipcode}'.encode(), message.encode()])
