import asyncio
import aioredis

from module_aioredis.aioredis_sub import CHANNEL_NAME


async def main():
    pub = await aioredis.create_redis('redis://localhost', db=0, password='rpassword')
    for i in range(10):
        await pub.publish_json(CHANNEL_NAME, {'x': i})
        await pub.publish_json(CHANNEL_NAME + '2', {'x': i * 100})
    pub.close()
    await pub.wait_closed()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
