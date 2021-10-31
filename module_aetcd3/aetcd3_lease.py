import asyncio
import logging
import sys
import time

import aetcd3
from aetcd3 import Lease

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def main():
    async with aetcd3.client() as client:
        # create a lease with 20 seconds
        lease: Lease = await client.lease(20)
        logging.info('lease id is %s', lease.id)

        await client.put('foo', 'bar', lease)

        lease_info = await client.get_lease_info(lease_id=lease.id)
        logging.info('lease info is %s', lease_info)

        # foo will be deleted after 20 seconds
        while True:
            foo_value_obj = await client.get('foo')
            foo_value = foo_value_obj[0]
            logging.info('got value %s', foo_value)
            if foo_value is None:
                logging.info('foo_value is None, break')
                break
            time.sleep(1)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
