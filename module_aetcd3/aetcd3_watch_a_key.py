import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
use the following commands to change the key:
# etcdctl put foo 5
# etcdctl put foo 6
# etcdctl put foo 5
"""


async def main():
    async with aetcd3.client() as client:
        await client.put('foo', 'bar')
        v = await client.get('foo')
        logging.info('value of foo is %s', v)

        # events_iterator, cancel = await client.watch('foo')
        events_iterator, cancel = await client.watch('foo', start_revision=1)
        event_times = 0
        async for event in events_iterator:
            logging.info('event is %s', event)
            event_times += 1
            if event_times > 5:
                logging.info('cancelling event %s', event)
                await cancel()


if __name__ == '__main__':
    asyncio.run(main())
