import asyncio
import string
import aioredis


async def go(r, key, value):
    await r.set(key, value)
    val = await r.get(key)
    print(f'Got {key} = {val}')


async def main(loop):
    r = await aioredis.create_redis_pool('redis://localhost', db=0, password='rpassword')
    try:
        return await asyncio.gather(*(
            go(r, i, j)
            for i, j in zip(string.ascii_uppercase, string.ascii_lowercase)
        ))
    finally:
        r.close()
        await r.wait_closed()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(main(loop))

