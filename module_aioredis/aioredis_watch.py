import asyncio
import aioredis


async def main():
    redis = await aioredis.create_redis_pool(
        "redis://localhost", db=0, password="rpassword"
    )
    keys = [f"k{i}" for i in range(3)]
    try:
        res = await redis.watch(*keys)
        pipe = redis.multi_exec()
        for k in keys:
            pipe.set(k, "xyz")
            print(k, " set!")
            # await asyncio.sleep(5)
        result = await pipe.execute()
        print("Done", result)
    finally:
        print("Unwatch")
        await redis.unwatch()
        redis.close()
        await redis.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
