import asyncio
import aioredis

CHANNEL_NAME = "api_def"


async def handle_msg():
    sub = await aioredis.create_redis("redis://localhost", db=0, password="rpassword")
    res = await sub.subscribe(CHANNEL_NAME)
    ch = res[0]
    try:
        while await ch.wait_message():
            msg = await ch.get()
            print("Got msg:", msg)
    finally:
        print("close...")
        await sub.unsubscribe("api_def")
        sub.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(handle_msg())
    loop.create_task(handle_msg())
    loop.run_forever()
