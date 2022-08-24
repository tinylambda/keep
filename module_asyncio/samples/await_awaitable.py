import asyncio
from typing import Awaitable, Generator


class MyAwaitable(Awaitable):
    def __init__(self):
        print("init")

    def __await__(self) -> Generator:
        async def closure():
            print("await")
            return self

        return closure().__await__()

    async def method(self):
        print("method")


async def main():
    m = MyAwaitable()
    obj = await m
    await obj.method()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
