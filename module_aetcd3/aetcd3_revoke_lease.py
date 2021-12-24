import asyncio
import logging
import sys

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

        logging.info('revoke lease %s', lease.id)
        await client.revoke_lease(lease_id=lease.id)  # the keys with this lease will be deleted

        value_tuple = await client.get('foo')
        value = value_tuple[0]
        logging.info('value is %s', value)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
