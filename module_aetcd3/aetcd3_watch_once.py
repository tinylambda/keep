import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
use the following commands to change the key:
# etcdctl put foo 5
"""


async def main():
    async with aetcd3.client() as client:
        await client.put("foo", "bar")
        event = await client.watch_once("foo")
        logging.info("get event %s", event)
        logging.info("done")


if __name__ == "__main__":
    asyncio.run(main())
