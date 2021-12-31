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
        # await client.put('/user_server/server_x', '1')
        # await client.put('/user_server/server_y', '2')

        # use get
        value, metadata = await client.get('/user_server/server_x')
        logging.info('value: %s, metadata.version: %s, metadata.mod_revision: %s',
                     value, metadata.version, metadata.mod_revision)

        # use get_prefix
        async for value, metadata in client.get_prefix('/user_server'):
            logging.info('value: %s, metadata.version: %s, metadata.mod_revision: %s',
                         value, metadata.version, metadata.mod_revision)

if __name__ == '__main__':
    asyncio.run(main())
