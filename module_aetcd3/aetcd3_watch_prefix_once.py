import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
change the value by commands:
# etcdctl put /user_server/server_x 10.10.1.1

to see what happens
"""


async def main():
    async with aetcd3.client() as client:
        await client.put("/user_server/server_x", "")
        await client.put("/user_server/server_y", "")

        event = await client.watch_prefix_once("/user_server/")

        logging.info("event is %s", event)
        logging.info("done")


if __name__ == "__main__":
    asyncio.run(main())
