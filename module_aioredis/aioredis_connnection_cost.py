import os
import asyncio

import aioredis


async def test_redis_connection():
    redis = await aioredis.create_redis_pool(
        "redis://localhost", db=0, password="rpassword"
    )
    i = 0
    while True:
        with await redis as conn:
            print("Connection ID", id(conn))
            i += 1

        if i % 10 == 0:
            print("wait for next round")
            await asyncio.sleep(1)


if __name__ == "__main__":
    print(os.getpid())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_redis_connection())
