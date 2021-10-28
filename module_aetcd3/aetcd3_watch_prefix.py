import asyncio
import logging
import sys

import aetcd3

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
change the value by commands:
# etcdctl put /user_server/server_x 10.10.1.1
# etcdctl put /user_server/server_x 10.10.1.2

to see what happens
"""


async def main():
    async with aetcd3.client() as client:
        await client.put('foo', 'bar')
        v = await client.get('foo')
        logging.info('value of foo is %s', v)

        events_iterator, cancel = await client.watch('foo')
        event_times = 0
        async for event in events_iterator:
            logging.info('event is %s', event)
            event_times += 1
            if event_times > 5:
                logging.info('cancelling event %s', event)
                await cancel()


if __name__ == '__main__':
    asyncio.run(main())
