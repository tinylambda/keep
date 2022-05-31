import asyncio
import aioredis

from aioredis.pubsub import Receiver
from aioredis.abc import AbcChannel

CHANNEL_NAME = "api_def"
CHANNEL_NAME2 = "api_def2"

mpsc = Receiver(loop=asyncio.get_event_loop())


async def handle_msg():
    sub = await aioredis.create_redis("redis://localhost", db=0, password="rpassword")
    await sub.subscribe(mpsc.channel(CHANNEL_NAME), mpsc.channel(CHANNEL_NAME2))
    try:
        async for channel, msg in mpsc.iter():
            assert isinstance(channel, AbcChannel)
            print("Got {!r} in channel {!r}".format(msg, channel))
    finally:
        print("close...")
        await sub.unsubscribe(CHANNEL_NAME, CHANNEL_NAME2)
        mpsc.stop()
        sub.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(handle_msg())
    loop.create_task(handle_msg())
    loop.run_forever()
