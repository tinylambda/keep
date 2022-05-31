import asyncio
import logging
import sys

import zmq.asyncio

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def start_server(context: zmq.asyncio.Context, bind_to: str):
    rep_sock = context.socket(zmq.REP)
    rep_sock.bind(bind_to)

    while True:
        msg = await rep_sock.recv()
        logging.info("received: %s", msg)
        await rep_sock.send(b"world")


if __name__ == "__main__":
    ctx = zmq.asyncio.Context()
    asyncio.run(start_server(ctx, "tcp://*:5555"))
