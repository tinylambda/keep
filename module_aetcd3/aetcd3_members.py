import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def main():
    async with aetcd3.client() as client:
        async for member in client.members():
            logging.info('%s', member)
            logging.info('member id is %s', member.id)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
