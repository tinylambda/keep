import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def client_access():
    async with aetcd3.client() as client:
        logging.info('set foo to bar')
        await client.put('foo', 'bar')
        v = await client.get('foo')
        logging.info('get foo: %s', v)
        await client.delete('foo')
        v = await client.get('foo')
        logging.info('get foo after delete: %s', v)
        await client.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(client_access())
