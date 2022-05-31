import asyncio
import logging
import sys

import zmq.asyncio


logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def main():
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.REP)
    port_selected = socket.bind_to_random_port(
        "tcp://*", min_port=49152, max_port=65536, max_tries=64
    )
    logging.info("port selected: %s", port_selected)

    while True:
        message = await socket.recv()
        logging.info("received message %s of type %s", message, type(message))
        await socket.send(message)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
