import asyncio
import aioredis


async def set_key():
    redis = await aioredis.create_redis_pool(
        "redis://localhost", db=0, password="rpassword"
    )
    await redis.set("my-key", "value")
    val = await redis.get("my-key", encoding="utf-8")
    print(val)
    redis.close()
    await redis.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_key())
