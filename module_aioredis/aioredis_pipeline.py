import asyncio
import aioredis


async def set_key():
    redis = await aioredis.create_redis_pool(
        "redis://localhost", db=0, password="rpassword"
    )
    pipe = redis.pipeline()
    # fut1 = pipe.set('k1', 'v1')
    # fut2 = pipe.set('k2', 'v2')
    fut3 = pipe.get("k1")
    fut4 = pipe.get("k2")
    result = await pipe.execute()
    print(result)
    k1, k2 = await asyncio.gather(fut3, fut4)
    print(k1, k2)
    k1, k2 = await asyncio.gather(fut3, fut4)
    print(k1, k2)
    redis.close()
    await redis.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_key())
