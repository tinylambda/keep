import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def client_access():
    async with aetcd3.client() as client:
        logging.info('do put')
        await client.put('foo', '1000010101')
        await asyncio.sleep(10)
        logging.info('%s', await client.get('foo'))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(client_access())
