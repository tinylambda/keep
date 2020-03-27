import asyncio
import aioredis


async def handle_msg():
    sub = await aioredis.create_redis('redis://localhost', db=0, password='rpassword')
    try:
        while True:
            res = await sub.subscribe('api_def')
            ch = res[0]
            msg = await ch.get()
            print('Got msg:', msg)
    finally:
        print('close...')
        await sub.unsubscribe('api_def')
        sub.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(handle_msg())
    loop.create_task(handle_msg())
    loop.run_forever()
