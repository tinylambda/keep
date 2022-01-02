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


async def simulate_event():
    async with aetcd3.client() as client:
        while True:
            await asyncio.sleep(3)
            await client.put('/user_server/server_x', '192.168.2.3')
            await client.put('/user_server/server_y', '192.168.2.88')
            await client.delete('/user_server/server_y')


async def main():
    async with aetcd3.client() as client:
        it, cancel = await client.watch_prefix('/user_server/')

        async for event in it:
            logging.info('detect event: %s; key is: %s', event, event.key)

        logging.info('done')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(simulate_event())
    loop.run_forever()
