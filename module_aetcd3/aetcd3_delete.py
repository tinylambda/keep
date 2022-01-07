import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def client_access():
    async with aetcd3.client() as client:
        await client.delete_prefix('/test-services/BattleService')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(client_access())
