import asyncio
import aioredis


async def main():
    redis = await aioredis.create_redis_pool('redis://localhost', db=0, password='rpassword')

    async def trans():
        tr = redis.multi_exec()
        fut1 = tr.set('foo', '123')
        fut2 = tr.set('bar', '321')
        result = await tr.execute()
        return result

    res = await trans()
    redis.close()
    await redis.wait_closed()
    return res


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(main())
    print(res)
