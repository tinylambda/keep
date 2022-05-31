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
        logging.info("lease id is %s", lease.id)

        await client.put("foo", "bar", lease)

        lease_info = await client.get_lease_info(lease_id=lease.id)
        logging.info("lease info is %s", lease_info)

        # foo will be deleted after 20 seconds
        while True:
            value_tuple = await client.get("foo")
            value = value_tuple[0]
            logging.info("value is %s", value)

            lease_info = await client.get_lease_info(lease_id=lease.id)
            ttl = getattr(lease_info, "TTL")
            granted_ttl = await lease.granted_ttl()
            logging.info("ttl is %s, granted_ttl is %s", ttl, granted_ttl)
            if ttl < 5:
                logging.info("refreshing lease!")
                await client.refresh_lease(lease_id=lease.id)

            if value is None:
                logging.info("value is None, break")
                break
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
