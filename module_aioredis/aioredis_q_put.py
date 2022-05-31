import asyncio
import aioredis


async def go():
    r = await aioredis.create_redis_pool(
        "redis://localhost", db=0, password="rpassword"
    )
    q_key = "q-key"
    for i in range(10):
        await r.rpush(q_key, i)
    await r.rpush(q_key, "bye")
    r.close()
    await r.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
