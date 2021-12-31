import asyncio
import logging
import random
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def main(name: str):
    async with aetcd3.client() as client:
        logging.info('[%s]: trying to get the lock !', name)
        async with client.lock('/locks/role') as lock:
            logging.info('got lock name=%s, ttl=%s, uuid=%s, lease=%s, acquired=%s',
                         lock.name, lock.ttl, lock.uuid, lock.lease, await lock.is_acquired())
            # do something
            await asyncio.sleep(random.randint(1, 4))
            logging.info('[%s]: I am done', name)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main('felix'))
    loop.create_task(main('fanny'))
    loop.create_task(main('tom'))

    loop.run_forever()
