import asyncio
import aioredis


async def go():
    r = await aioredis.create_redis_pool('redis://localhost', db=0, password='rpassword')
    while True:
        new_value = await r.blpop('q-key', 'q-key2')
        print(new_value)
        if new_value[1] == b'bye':
            break
    r.close()
    await r.wait_closed()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())

