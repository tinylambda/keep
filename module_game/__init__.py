import asyncio


async def main():
    pass


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    m = main()
    print(dir(m))
    loop.run_until_complete(m)

