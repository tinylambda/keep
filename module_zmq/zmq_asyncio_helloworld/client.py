import asyncio
import logging
import sys

import zmq.asyncio

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def request(context: zmq.asyncio.Context, connect_to):
    req_sock = context.socket(zmq.REQ)
    req_sock.connect(connect_to)

    for i in range(10):
        await req_sock.send(b"hello")
        reply = await req_sock.recv()
        logging.info("received: %s", reply)


if __name__ == "__main__":
    ctx = zmq.asyncio.Context()
    asyncio.run(request(ctx, sys.argv[1]))
