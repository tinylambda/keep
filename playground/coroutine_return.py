import asyncio


async def go():
    return 100


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(go())
    print(res)
