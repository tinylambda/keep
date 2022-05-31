import asyncio
import aioredis


class AIOContext:
    def __init__(self):
        self.redis = None
        self.multi_exec = None
        self.pipeline = None
        self.callback_data = {}

    async def __aenter__(self):
        self.redis = await aioredis.create_redis_pool(
            "redis://localhost", db=0, password="rpassword"
        )
        self.multi_exec = self.redis.multi_exec()
        self.pipeline = self.redis.pipeline()

        keys = [f"kx{i}" for i in range(2)]
        await self.redis.watch(*keys)
        futures = [self.pipeline.get(key) for key in keys]
        await self.pipeline.execute()
        result = await asyncio.gather(*futures)
        print(result)
        self.callback_data.update(dict(zip(keys, result)))

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            new_data = {}
            for k in self.callback_data:
                v = self.callback_data[k]
                v += b"___"
                new_data.update({k: v})

            for k, v in new_data.items():
                if v is None:
                    continue
                self.multi_exec.set(k, v)
                await asyncio.sleep(1)
            await self.multi_exec.execute()
        finally:
            await self.redis.unwatch()
            self.redis.close()
            await self.redis.wait_closed()

    def __enter__(self):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.__aenter__())

    def __exit__(self, exc_type, exc_val, exc_tb):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.__aexit__(exc_type, exc_val, exc_tb))


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
    with AIOContext():
        pass
